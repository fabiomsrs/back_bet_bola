from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime
from .manager import GamesManager, CotationsManager
from user.models import Seller
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Q
import decimal
from django.conf import settings
import utils.timezone as tzlocal


class BetTicket(models.Model):

    BET_TICKET_STATUS = (
        ('Aguardando Resultados', 'Aguardando Resultados'),
        ('Não Venceu', 'Não Venceu'),
        ('Venceu', 'Venceu'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='my_bet_tickets',null=True, on_delete=models.SET_NULL, verbose_name='Apostador')
    random_user = models.ForeignKey('user.RandomUser', null=True, on_delete=models.SET_NULL, verbose_name='Cliente')
    cotations = models.ManyToManyField('Cotation', related_name='bet_ticket', verbose_name='Cota')
    cotation_value_total = models.FloatField(verbose_name='Cota Total da Aposta')
    creation_date = models.DateTimeField(verbose_name='Data da aposta')	
    reward = models.ForeignKey('Reward', null=True, on_delete=models.SET_NULL, verbose_name='Recompensa')
    payment = models.OneToOneField('Payment', null=True, on_delete=models.SET_NULL, verbose_name='Pagamento')
    value = models.FloatField(verbose_name='Valor Apostado')
    bet_ticket_status = models.CharField(max_length=80, choices=BET_TICKET_STATUS,default=BET_TICKET_STATUS[0][1],verbose_name='Status')


    def __str__(self):
        return str(self.pk)


    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
        permissions = (
            ('can_validate_payment', "Can validate user ticket"),
            ('can_reward', "Can reward a user"),
        )

    def validate_ticket(self, user):
        if user.seller.can_sell_ilimited:
            if self.value > user.seller.credit_limit:                
                return False
            user.seller.credit_limit -= self.value 
            user.seller.save()

        self.payment.status_payment = Payment.PAYMENT_STATUS[1][1]
        self.payment.payment_date = tzlocal.now()
        self.payment.who_set_payment = Seller.objects.get(pk=user.pk)
        self.payment.save()
        return True


    def reward_ticket(self, user):
        self.reward.status_reward = Payment.REWARD_STATUS[1][1]
        self.reward.reward_date = tzlocal.now()
        self.reward.who_rewarded = Seller.objects.get(pk=user.pk)
        self.reward.save()


    def cotation_sum(self):
        return round(self.cotation_value_total, 2)


    def update_ticket_status(self):
        
        if not self.check_if_waiting_results():
            if self.cotations.filter(winning=False).count() > 0:
                self.bet_ticket_status = BetTicket.BET_TICKET_STATUS[1][1]
                self.save()
            else:
                self.bet_ticket_status = BetTicket.BET_TICKET_STATUS[2][1]
                self.save()
            

    def check_if_waiting_results(self):
        return self.cotations.filter(winning=None).count() > 0



class Game(models.Model):

    GAME_STATUS = (
        ('NS', 'Não Iniciado'),
        ('LIVE','Ao Vivo'),
        ('HT', 'Meio Tempo'),
        ('FT', 'Tempo Total')	,	
        ('ET', 'Tempo Extra'),
        ('PEN_LIVE', 'Penaltis'),
        ('AET', 'Terminou após tempo extra'),
        ('BREAK', 'Esperando tempo extra'),
        ('FT_PEN', 'Tempo total após os penaltis'),
        ('CANCL', 'Cancelado'),
        ('POSTP', 'Adiado'),
        ('INT', 'Interrompindo'),
        ('ABAN', 'Abandonado'),
        ('SUSP', 'Suspendido'),
        ('AWARDED', 'Premiado'),
        ('DELAYED', 'Atrasado'),
        ('TBA', 'A ser anunciado'),
        ('WO', 'WO'),
    )

    name = models.CharField(max_length=80, verbose_name='Nome do Jogo')	
    start_game_date = models.DateTimeField(verbose_name='Início da Partida')
    championship = models.ForeignKey('Championship',related_name='my_games',null=True, on_delete=models.SET_NULL,verbose_name='Campeonato')
    status_game = models.CharField(max_length=80,default=GAME_STATUS[0][1], choices=GAME_STATUS,verbose_name='Status do Jogo')
    odds_calculated = models.BooleanField()	
    ht_score = models.CharField(max_length=80, null=True, verbose_name='Placar até o meio-tempo')
    ft_score = models.CharField(max_length=80, null=True, verbose_name='Placar no final do Jogo', help_text="Placar final Ex: 3-5 (Casa-Visita)")
    odds_processed = models.BooleanField(default=False)

    objects = GamesManager()	

    class Meta:
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'


    def __str__(self):
        return self.name	


class Championship(models.Model):

    name = models.CharField(max_length=80, verbose_name='Nome', help_text='Campeonato')
    country = models.ForeignKey('Country', related_name='my_championships',null=True, on_delete=models.SET_NULL, verbose_name='Pais')
    priority = models.IntegerField(default=1)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Campeonato'
        verbose_name_plural = 'Campeonatos'


class Country(models.Model):

    name = models.CharField(max_length=45, verbose_name='País')
    priority = models.IntegerField(default=1)

class Reward(models.Model):

    REWARD_STATUS = (
        ('Aguardando Resultados', 'Aguardando Resultados'),
        ('O apostador foi pago', 'O apostador foi pago'),
        ('Esse ticket não venceu', 'Esse ticket não venceu'),
        ('Venceu, Aguardando pagamento', 'Venceu, Aguardando pagamento'),
    )

    who_rewarded = models.ForeignKey('user.Seller', null=True, on_delete=models.SET_NULL)
    reward_date = models.DateTimeField(null=True)
    value = models.FloatField(default=0)
    status_reward = models.CharField(max_length=80, choices=REWARD_STATUS, default=REWARD_STATUS[0][1])

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = 'Recompensa'
        verbose_name_plural = 'Recompensas'


class Market(models.Model):

    name = models.CharField(max_length=100, verbose_name='Tipo de Aposta')
    
    def __str__(self):
        return str(self.name)
    
    def natural_key(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo de Aposta'
        verbose_name_plural = 'Tipo de Aposta'


class Cotation(models.Model):

    name = models.CharField(max_length=80, verbose_name='Nome da Cota')
    original_value = models.FloatField(default=0,verbose_name='Valor Original')
    value = models.FloatField(default=0, verbose_name='Valor Modificado')
    game = models.ForeignKey('Game', related_name='cotations', null=True, on_delete=models.SET_NULL, verbose_name='Jogo')	
    winning = models.NullBooleanField(verbose_name='Vencedor ?')
    is_standard = models.BooleanField(default=False, verbose_name='Cota Padrão ?')
    kind = models.ForeignKey(Market, related_name='cotations', null=True, on_delete=models.SET_NULL, verbose_name='Tipo da Cota')
    total = models.FloatField(blank=True, null=True)
    objects = GamesManager()

    def __str__(self):
        return str(self.value)


    class Meta:
        verbose_name = 'Cota'
        verbose_name_plural = 'Cotas'


    def save(self):
        if not Cotation.objects.filter(name=self.name, kind=self.kind, game=self.game).exists():
            #print("Cotation:" + str(self.game.name))
            if not self.is_excluded_cotation(self.name, self.kind):
                super().save()
                #print("Saving Cota:" + str(self.name) + " Tipo:" + str(self.kind))
            else:
                pass
                #print("[NOT] Cota:" + str(self.name) + " Tipo:" + str(self.kind))
        else:
            Cotation.objects.filter(name=self.name, kind=self.kind, game=self.game).update(value=self.value)
            #print("UPDATE Cota:" + str(self.name) + " Tipo:" + str(self.kind))


    def is_excluded_cotation(self, cotation_name, kind):

        is_excluded = False

        #print("ID: "+ str(kind.pk) + " Cota: " + cotation_name + " Tipo: " + str(kind.name))

        if kind.pk == 38:
            excluded_cotations = [
                'Acima 0.5',
                'Abaixo 2.5',
                'Abaixo 3.5',
                'Abaixo 4.5',
                'Abaixo 5.5',
                'Abaixo 3.0',
                'Abaixo 4.0',
                'Abaixo 5.0',
            ]

            if cotation_name in excluded_cotations:
                is_excluded = True

        elif kind.pk == 12:
            excluded_cotations = [
                'Acima 0.5', 
                'Abaixo 4.5',
                'Abaixo 5.5',
                'Abaixo 6.5',
                'Abaixo 7.5',
                'Abaixo 8.5',
                'Abaixo 9.5',
                'Abaixo 4.0',
                'Abaixo 5.0',
                'Abaixo 6.0',
                'Abaixo 7.0',
                'Abaixo 8.0',
                'Abaixo 9.0',
                'Abaixo 4.75',
                'Abaixo 5.75',
                'Abaixo 6.75',
                'Abaixo 7.75',
                'Abaixo 8.75',
                'Abaixo 9.75',
            ]
            
            if cotation_name in excluded_cotations:
                is_excluded = True

        elif kind.pk == 976204:
            excluded_cotations = [
                'Abaixo 2.0',
                'Abaixo 3.0',
                'Abaixo 4.0',
                'Abaixo 5.0',
                'Abaixo 2.5',
                'Abaixo 3.5',
                'Abaixo 4.5',
                'Abaixo 5.5',
            ]

            if cotation_name in excluded_cotations:
                is_excluded = True

        elif kind.pk == 976198:
            excluded_cotations = [
                'Abaixo 2.0',
                'Abaixo 3.0',
                'Abaixo 4.0',
                'Abaixo 5.0',
                'Abaixo 2.5',
                'Abaixo 3.5',
                'Abaixo 4.5',
                'Abaixo 5.5',
            ]
            
            if cotation_name in excluded_cotations:
                is_excluded = True

        elif kind.pk == 47:
            excluded_cotations = [
                'Acima 0.5',
                'Abaixo 2.5',
                'Abaixo 3.5',
                'Abaixo 4.5',
                'Abaixo 5.5',
                'Abaixo 3.0',
                'Abaixo 4.0',
                'Abaixo 5.0',
            ]

            if cotation_name in excluded_cotations:
                is_excluded = True


        #elif kind.pk == 63:
        #    is_excluded = True

        #print("Excluded?: " + str(is_excluded))
        #input("Continuar")

        return is_excluded

class Payment(models.Model):

    PAYMENT_STATUS = (
        ('Aguardando Pagamento do Ticket', 'Aguardando Pagamento do Ticket'),
        ('Pago', 'Pago'),
    )

    who_set_payment = models.ForeignKey('user.Seller', null=True, on_delete=models.SET_NULL)
    status_payment = models.CharField(max_length=80, choices=PAYMENT_STATUS, default=PAYMENT_STATUS[0][1])
    payment_date = models.DateTimeField(null=True)
    seller_was_rewarded = models.BooleanField(default=False)

    def __str__(self):
        return self.status_payment


    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'

