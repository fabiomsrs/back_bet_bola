
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


class RevenueSerializer(serializers.HyperlinkedModelSerializer):
			
	payment = PaymentSerializerWithSeller()
	reward = RewardSerializer()	
	creator = serializers.SlugRelatedField(read_only=True, slug_field='username')
	status = serializers.SerializerMethodField()	
	comission = serializers.SerializerMethodField()	
	bet_type = serializers.SerializerMethodField()	
	manager = serializers.SerializerMethodField()
	won_bonus = serializers.SerializerMethodField()
	creation_date = serializers.DateTimeField(format='%d/%m/%Y %H:%M')


	class Meta:
		model = Ticket
		fields = ('id','creation_date','creator','reward','won_bonus','bet_type','manager','comission','payment','bet_value','status')

	
	def get_won_bonus(self, obj):
		return obj.won_bonus()

	def get_status(self, obj):
		return obj.get_status_display()
	
	def get_comission(self, obj):		
		user_type = obj.payment.who_paid.user_type
		comission = None
		
		if user_type == 2:
			comission = obj.payment.who_paid.seller.comissions
			key_value = {1:comission.simple,2:comission.double,3:comission.triple,4:comission.fourth,5:comission.fifth,6:comission.sixth}				

			return str(float(key_value.get(obj.cotations.count(), comission.sixth_more) * obj.bet_value / 100))
		
		return "0.0"

	def get_bet_type(self, obj):
		key_value = {1:"simple",2:"double",3:"triple",4:"fourth",5:"fifth",6:"sixth"}
		return str(key_value.get(obj.cotations.count(), "sixth_more")) 				
	
	def get_manager(self, obj):		
		user_type = obj.payment.who_paid.user_type		
		if user_type == 2:
			manager = obj.payment.who_paid.seller.my_manager
			if manager:
				return {"username":manager.username,"comission_based_on_profit":manager.comission_based_on_profit}
		return None



class TicketSerializer(serializers.HyperlinkedModelSerializer):
	
	owner = serializers.SlugRelatedField(read_only=True,slug_field='first_name')
	creator = serializers.SlugRelatedField(read_only=True, slug_field='username')
	payment = PaymentSerializerWithSeller()
	reward = RewardSerializer()
	cotation_sum = serializers.SerializerMethodField()
	status = serializers.SerializerMethodField()
	cotations = CotationTicketSerializer(many=True)
	creation_date = serializers.DateTimeField(format='%d/%m/%Y %H:%M')


	class Meta:
		model = Ticket
		fields = ('id','owner','creator','cotations','cotation_sum','creation_date','reward','payment','bet_value','available','status')

	def get_cotation_sum(self, obj):
		return obj.cotation_sum()
	
	def get_status(self, obj):
		return obj.get_status_display()



class CreateTicketAnonymousUserSerializer(serializers.HyperlinkedModelSerializer):	
	owner = AnonymousUserSerializer()
	creation_date = serializers.DateTimeField(read_only=True)	
	payment = PaymentSerializer(read_only=True)	
	reward = RewardSerializer(read_only=True)
	cotations = serializers.PrimaryKeyRelatedField(many=True, queryset=Cotation.objects.all(), required=True)
			

	def validate_bet_value(self, value):
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
		fields = ('id','owner','creation_date','reward','cotations','payment','bet_value')


class CreateTicketLoggedUserSerializer(CreateTicketAnonymousUserSerializer):	

	def __init__(self, *args, **kwargs):
		super(CreateTicketLoggedUserSerializer, self).__init__(*args, **kwargs)
		request = kwargs['context']['request']		
		if request.user.has_perm('user.be_punter'):			
			self.fields['normal_user'] = AnonymousUserSerializer(read_only=True)

	class Meta:
		model = Ticket
		fields = ('id','owner','creation_date','reward','cotations','payment','bet_value')




class TicketCustomMessageSerializer(serializers.HyperlinkedModelSerializer):

	store = serializers.SlugRelatedField(queryset = Store.objects.all(),slug_field='id')

	class Meta:
		model =  TicketCustomMessage
		fields = ('text','store')

