from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from filters.mixins import FiltersMixin
from ticket.models import Ticket, Reward, Payment
from ticket.serializers.ticket import RevenueSerializer, TicketSerializer, CreateTicketAnonymousUserSerializer, CreateTicketLoggedUserSerializer
from ticket.paginations import TicketPagination, RevenueSellerPagination, RevenueManagerPagination
from ticket.permissions import CanCreateTicket, CanPayWinner, CanValidateTicket, CanCancelTicket, CanManipulateTicket
from user.permissions import IsSuperUser
from core.permissions import StoreIsRequired, UserIsFromThisStore
from user.models import TicketOwner
from core.models import CotationCopy, Cotation, Store
from utils.models import RewardRestriction
from utils import timezone as tzlocal
import datetime
from config import settings

class RevenueSellerView(FiltersMixin, ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = RevenueSerializer
    permission_classes = (
        StoreIsRequired, 
        IsSuperUser|CanManipulateTicket, 
        IsSuperUser|CanCreateTicket
    )
    pagination_class = RevenueSellerPagination

    filter_mappings = {
        'ticket_id':'pk',
        'store':'store__pk',
        'ticket_status':'status',
        'created_by': 'creator__username__icontains',
        'paid_by': 'payment__who_paid__username',        
        'start_creation_date':'creation_date__gte',
        'end_creation_date':'creation_date__lte',
        'payment_status':'payment__status',
        'start_payment_date': 'payment__date__gte',
        'end_payment_date': 'payment__date__lte',
        'available': 'available',
    }

    def get_queryset(self):
        date = datetime.date.today()
        start_week = date - datetime.timedelta(date.weekday())
        end_week = start_week + datetime.timedelta(7)        
        tickets = Ticket.objects.filter(payment__status=2, creation_date__range=[start_week, end_week]).exclude(status__in=[5,6])
        return tickets


class RevenueManagerView(FiltersMixin, ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = RevenueSerializer
    permission_classes = (
        StoreIsRequired, 
        IsSuperUser|CanManipulateTicket, 
        IsSuperUser|CanCreateTicket
    )
    pagination_class = RevenueManagerPagination

    filter_mappings = {
        'ticket_id':'pk',
        'store':'store__pk',
        'ticket_status':'status',
        'created_by': 'creator__username__icontains',
        'paid_by': 'payment__who_paid__username',
        'manager': 'payment__who_paid__seller__my_manager__username',
        'start_creation_date':'creation_date__gte',
        'end_creation_date':'creation_date__lte',
        'payment_status':'payment__status',
        'start_payment_date': 'payment__date__gte',
        'end_payment_date': 'payment__date__lte',
        'available': 'available',
    }

    def get_queryset(self):
        date = datetime.date.today()
        start_week = date - datetime.timedelta(date.weekday())
        end_week = start_week + datetime.timedelta(7)
        tickets = Ticket.objects.filter(payment__status=2, creation_date__range=[start_week, end_week]).exclude(status__in=[5,6])
        return tickets
        