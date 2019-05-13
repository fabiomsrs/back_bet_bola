
from rest_framework import serializers
from rest_framework.response import Response
from ticket.serializers.reward import RewardSerializer, RewardSerializer
from ticket.serializers.payment import PaymentSerializerWithSeller, PaymentSerializer
from core.serializers.cotation import CotationTicketSerializer
from user.serializers.anonymous import AnonymousUserSerializer
from ticket.paginations import TicketPagination
from utils.models import TicketCustomMessage
from utils.utils import general_configurations
from utils import timezone as tzlocal
from ticket.models import Ticket
from user.models import CustomUser
from core.models import Store, Cotation

class TicketSerializer(serializers.HyperlinkedModelSerializer):
	
	user = serializers.SlugRelatedField(queryset = CustomUser.objects.all(),slug_field='first_name')
	normal_user = serializers.SlugRelatedField(queryset = CustomUser.objects.all(),slug_field='first_name')
	seller = serializers.SlugRelatedField(read_only=True, slug_field='first_name')
	payment = PaymentSerializerWithSeller()
	reward = RewardSerializer()
	store = serializers.SlugRelatedField(queryset = Store.objects.all(), slug_field='id')
	cotation_sum = serializers.SerializerMethodField()
	status = serializers.SerializerMethodField()
	cotations = CotationTicketSerializer(many=True)
	creation_date = serializers.DateTimeField(format='%d/%m/%Y %H:%M')


	class Meta:
		model = Ticket
		fields = ('id','user','seller','normal_user','cotations','cotation_sum','creation_date','reward','payment','value','visible','status','store')

	def get_cotation_sum(self, obj):
		return obj.cotation_sum()
	
	def get_status(self, obj):
		return obj.get_status_display()



class CreateTicketAnonymousUserSerializer(serializers.HyperlinkedModelSerializer):	
	normal_user = AnonymousUserSerializer()
	creation_date = serializers.DateTimeField(read_only=True)	
	payment = PaymentSerializer(read_only=True)	
	reward = RewardSerializer(read_only=True)
	cotations = serializers.PrimaryKeyRelatedField(many=True, queryset=Cotation.objects.all(), required=True)	

	def update(self, instance, validated_data):
		normal_user = validated_data.pop('normal_user')		
		value = validated_data.pop('value')				
		cotations = validated_data.pop('cotations')		
		cotation_ids = [cotation.id for cotation in cotations]

		ticket = Ticket.objects.get(id=str(instance))
		ticket.value = value		
		ticket.cotations.clear()

		for cotation in  Cotation.objects.in_bulk(cotation_ids):
			ticket.cotations.add(cotation)
		

		ticket.save()			
		return ticket
		

	def validate_value(self, value):
		store = self.context['request'].GET.get('store')
		configurations = general_configurations(store)
		
		if value < configurations["min_bet_value"]:
			if value <= 0:	                       
				raise serializers.ValidationError("Valor da aposta inválido.")	        	       
			raise serializers.ValidationError("A aposta mínima é: R$ " + str(configurations["min_bet_value"]))	
		elif value > configurations["max_bet_value"]:
			raise serializers.ValidationError("A aposta ultrapassou o valor maximo de R$ " + str(configurations["max_bet_value"]))
		return value	

	def validate_cotations(self, cotations):
		store = self.context['request'].GET.get('store')		
		game_list = [cotation.game for cotation in cotations]
		configurations = general_configurations(store)		
		
		if len(cotations) < configurations["min_number_of_choices_per_bet"]:			
			raise serializers.ValidationError("Desculpe, Aposte em pelo menos " + str(configurations["min_number_of_choices_per_bet"]) + " jogo.")
		
		if len(cotations) > configurations["max_number_of_choices_per_bet"]:			
			raise serializers.ValidationError("Desculpe, O número máximo de " + str(configurations["max_number_of_choices_per_bet"]) + " apostas por bilhete foi excedido.")

		if game_list.__len__() != list(set(game_list)).__len__():
			raise serializers.ValidationError("Desculpe, não é permitido mais de uma aposta no mesmo jogo.")

		for cotation in cotations:								
			try:													
				if cotation.game.start_date < tzlocal.now():														
					raise serializers.ValidationError("Desculpe, o jogo " + cotation.game.name + " já começou, remova-o")
			except Cotation.DoesNotExist:				
				raise serializers.ValidationError("Erro, uma das cotas enviadas não existe.")	

		return cotations

	class Meta:
		model = Ticket
		fields = ('id','normal_user','creation_date','reward','cotations','payment','value')


class CreateTicketLoggedUserSerializer(CreateTicketAnonymousUserSerializer):	

	def __init__(self, *args, **kwargs):
		super(CreateTicketLoggedUserSerializer, self).__init__(*args, **kwargs)
		request = kwargs['context']['request']		
		if request.user.has_perm('user.be_punter'):			
			self.fields['normal_user'] = AnonymousUserSerializer(read_only=True)

	class Meta:
		model = Ticket
		fields = ('id','normal_user','creation_date','reward','cotations','payment','value')




class TicketCustomMessageSerializer(serializers.HyperlinkedModelSerializer):

	store = serializers.SlugRelatedField(queryset = Store.objects.all(),slug_field='id')

	class Meta:
		model =  TicketCustomMessage
		fields = ('text','store')

