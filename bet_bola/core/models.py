from django.db import models
from django.core.exceptions import ValidationError
from .manager import GamesManager,CotationsManager
from datetime import datetime
from user.models import Seller
import requests
import decimal
# Create your models here.

TOKEN='ndvsLZTo8pZxduyPtIHRkGRMkGpem2uHIGYwaz9sZxzppz6EZUhSjsv7g9Ru'

BET_TICKET_STATUS = (
		('WAITING_RESULT', 'Aguardando Resultados.'),
		('NOT_WON', 'Não Venceu.'),
		('WON', 'Venceu.'),
	)

REWARD_STATUS = (
		('WAITING_RESULTS', 'Aguardando Resultados.'),
		('PAID', 'Finalizado, O apostador foi pago.'),
		('NOT_WON', 'Esse ticket não venceu.'),
		('WON', 'Venceu, Aguardando pagamento.'),
	)

GAME_STATUS = (
		('NS', 'Not Started'),
		('LIVE','Live'),
		('HT', 'Half-time'),
		('FT', 'Full-Time')	,	
		('ET', 'Extra-Time'),
		('PEN_LIVE', 'Penalty Shootout'),
		('AET', 'Finished after extra time'),
		('BREAK', 'Match finished, waiting for extra time to start'),
		('FT_PEN', 'Full-Time after penalties'),
		('CANCL', 'Cancelled'),
		('POSTP', 'PostPhoned'),
		('INT',	'Interrupted'),
		('ABAN', 'Abandoned'),
		('SUSP', 'Suspended'),
		('AWARDED', 'Awarded'),
		('DELAYED', 'Delayed'),
		('TBA', 'To Be Announced (Fixture will be updated with exact time later)'),
		('WO', 'Walkover (Awarding of a victory to a contestant because there are no other contestants)'),
	)


PAYMENT_STATUS = (
		('WATING_PAYMENT', 'Aguardando Pagamento do Ticket.'),
		('PAID', 'Pago.'),
	)
		

class BetTicket(models.Model):	
	punter = models.ForeignKey('user.Punter', related_name='my_bet_tickets')
	seller = models.ForeignKey('user.Seller', null=True, related_name='bet_tickets_validated_by_me')
	cotations = models.ManyToManyField('Cotation', related_name='my_bet_tickets')
	creation_date = models.DateTimeField(auto_now_add=True)	
	reward = models.ForeignKey('Reward', default=None)
	payment = models.OneToOneField('Payment', default=None)
	value = models.DecimalField(max_digits=6, decimal_places=2)
	bet_ticket_status = models.CharField(max_length=80, choices=BET_TICKET_STATUS,default=BET_TICKET_STATUS[0][1])


	def ticket_valid(self, user):
		self.payment.status_payment = PAYMENT_STATUS[0][1]
		self.payment.who_set_payment = Seller.objects.get(pk=user.pk)
		self.payment.save()

	def reward_payment(self, user):
		self.reward.status_reward = REWARD_STATUS[0][1]
		self.reward.who_rewarded = Seller.objects.get(pk=user.pk)
		self.reward.save()

	def cota_total(self):
		cota_total = 0
		
		for cotation in self.cotations.all():
			cota_total += cotation.value
		
		return cota_total

	def __str__(self):
		return str(self.pk)

	class Meta:
		permissions = (
				('can_validate_payment', "Can validate user ticket"),
				('can_reward', "Can reward a user"),
			)


class Game(models.Model):
	name = models.CharField(max_length=80)	
	start_game_date = models.DateTimeField()
	championship = models.ForeignKey('Championship',related_name='my_games')
	status_game = models.CharField(max_length=80,default=GAME_STATUS[0][1], choices=GAME_STATUS)
	objects = GamesManager()
	
	@staticmethod
	def consuming_api():
		first_date = str(datetime.now().year) + "-" +str(datetime.now().month) + "-" + str((datetime.now().day - 1))
		second_date = str(datetime.now().year) + "-" +str(datetime.now().month) + "-" + str((datetime.now().day))

		r = requests.get("https://soccer.sportmonks.com/api/v2.0/fixtures/between/"+first_date+"/"+second_date+"?api_token="+TOKEN+"&include=localTeam,visitorTeam")
		
		for game in r.json().get('data'):
			if Championship(pk = game["league_id"]) in Championship.objects.all():
				if Game(pk = game["id"]) in Game.objects.all():
					g = Game.objects.get(pk = game["id"])
					g.status_game = game['time']['status']
					g.save()
					
				else:
					Game(pk=game['id'],
						start_game_date=datetime.strptime(game["time"]["starting_at"]["date_time"], "%Y-%m-%d %H:%M:%S"),
						name=game['localTeam']['data']['name']+" x " +game['visitorTeam']['data']['name'], championship=Championship.objects.get(pk=game["league_id"]), status_game=game['time']["status"]).save() 

	def __str__(self):
		return self.name	


class Championship(models.Model):
	name = models.CharField(max_length=80)

	@staticmethod
	def consuming_api():
		r = requests.get("https://soccer.sportmonks.com/api/v2.0/leagues/?api_token="+TOKEN)
		
		for championship in r.json().get('data'):
			Championship(pk=championship['id'],name = championship['name']).save()

	def __str__(self):
		return self.name


class Reward(models.Model):
	who_rewarded = models.ForeignKey('user.Seller', null=True)	
	reward_date = models.DateTimeField(null=True)
	value = models.DecimalField(max_digits=6, decimal_places=2)
	status_reward = models.CharField(max_length=80, choices=REWARD_STATUS, default=REWARD_STATUS[0][1])


class Cotation(models.Model):
	name = models.CharField(max_length=80)
	value = models.FloatField()	
	game = models.ForeignKey('Game', related_name='cotations')	
	winning = models.BooleanField(default=False)
	is_standard = models.BooleanField(default=False)
	kind = models.CharField(max_length=100)
	objects = GamesManager()
	
	@staticmethod
	def consuming_api():
		for game in Game.objects.all():
			cont = 0
			r = requests.get("https://soccer.sportmonks.com/api/v2.0/odds/fixture/"+str(game.pk)+"/bookmaker/2?api_token="+TOKEN)			
			# if r.json().get('data').__len__() >= 1:
			# 	if r.json().get('data')[0]['bookmaker']['data'].__len__() >= 1:
			# 		for cotation in r.json().get('data')[0]['bookmaker']['data'][0]['odds']['data']:				
			# 			Cotation(name=cotation['label'],value=cotation['value'],game=game, is_standard = True).save()									
			for kind in r.json().get('data'):
				kind_name = kind['name']				
				for cotation in kind['bookmaker']['data'][0]['odds']['data']:
					if cont == 0:
						Cotation(name=cotation['label'],value=cotation['value'],game=game, is_standard = True, kind = kind_name).save()						
					else:
						Cotation(name=cotation['label'],value=cotation['value'],game=game, is_standard = False, kind = kind_name).save()
				cont+=1



	def __str__(self):
		return str(self.value)


class Payment(models.Model):
	who_set_payment = models.ForeignKey('user.Seller', null=True)
	status_payment = models.CharField(max_length=80, choices=PAYMENT_STATUS, default=PAYMENT_STATUS[0][1])
	payment_date = models.DateTimeField(null=True)
