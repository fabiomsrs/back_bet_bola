from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from filters.mixins import FiltersMixin
from ticket.models import Ticket
from cashier.serializers.cashier import (
    SellerCashierSerializer, SellersCashierSerializer, 
    ManagerCashierSerializer, ManagersCashierSerializer, ManagerSpecificCashierSerializer
)
from history.paginations import (
    SellerCashierPagination, ManagerCashierPagination, 
    SellersCashierPagination, ManagersCashierPagination, ManagerSpecificCashierPagination
)
from user.models import Seller, Manager, CustomUser
from history.models import ManagerCashierHistory, SellerCashierHistory
from history.permissions import (
    CashierCloseManagerPermission, ManagerCashierPermission, 
    CashierCloseSellerPermission, SellerCashierPermission
)
from user.permissions import IsManager
import json, datetime, decimal


class SellersCashierView(FiltersMixin, ModelViewSet):
    queryset = Seller.objects.filter(payment__status=2).distinct()
    serializer_class = SellersCashierSerializer
    permission_classes = [SellerCashierPermission]
    pagination_class = SellersCashierPagination

    def list(self, request, pk=None):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(queryset, many=True)            
            return self.get_paginated_response(serializer.data)                                        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    def get_queryset(self):
        user = self.request.user
        if user.user_type == 2:
            return self.queryset.filter(pk=user.pk,my_store=self.request.user.my_store)
        elif user.user_type == 3:
            return self.queryset.filter(my_manager__pk=user.pk,my_store=self.request.user.my_store)            
        return self.queryset.filter(my_store=self.request.user.my_store)


    @action(methods=['post'], detail=False, permission_classes = [CashierCloseSellerPermission])
    def close_seller(self, request, pk=None):          
        data = json.loads(request.POST.get('data'))
        sellers_ids = data.get('sellers_ids')
        start_creation_date = data.get('start_creation_date')
        end_creation_date = data.get('end_creation_date') 
               
        for seller in Seller.objects.filter(id__in=sellers_ids):
            if request.user.user_type == 3 and not request.user.manager.manager_assoc.filter(pk=seller.pk):
                continue
            
            serializer = SellersCashierSerializer(seller, context={"request":request})
            data = serializer.data

            if not data['comission'] == 0 or not data['entry'] == 0 or not data['out'] == 0:
                revenue_history_seller = SellerCashierHistory(register_by=request.user, 
                seller=seller, 
                entry=decimal.Decimal(data['entry']),
                comission=decimal.Decimal(data['comission']),
                total_out=decimal.Decimal(data['total_out']),
                bonus_premio=decimal.Decimal(data['won_bonus']),
                profit= decimal.Decimal(decimal.Decimal(data['entry']) - decimal.Decimal(data['total_out'])),
                store=request.user.my_store)           
                
                tickets = Ticket.objects.filter(Q(payment__status=2, payment__who_paid__pk=seller.pk,store=self.request.user.my_store) & 
                (Q(closed_in_for_seller=False) | Q(closed_out_for_seller=False, status__in=[4,2]))).exclude(Q(status__in=[5,6]) | Q(available=False))        

                if tickets.exists():
                    if start_creation_date:
                        start_creation_date_refactored = datetime.datetime.strptime(start_creation_date, '%d/%m/%Y').strftime('%Y-%m-%d')
                        tickets = tickets.filter(creation_date__date__gte=start_creation_date_refactored)
                    if end_creation_date:
                        end_creation_date_refactored = datetime.datetime.strptime(end_creation_date, '%d/%m/%Y').strftime('%Y-%m-%d')
                        tickets = tickets.filter(creation_date__date__lte=end_creation_date_refactored)                                       

                    revenue_history_seller.save()
                    revenue_history_seller.tickets_registered.set(tickets)    

                    if not seller.my_manager:
                        tickets.filter(status__in=[4,2]).update(closed_out_for_seller=True, closed_out_for_manager=True)
                        tickets.update(closed_in_for_seller=True, closed_in_for_manager=True)
                    else:
                        tickets.filter(status__in=[4,2]).update(closed_out_for_seller=True)
                        tickets.update(closed_in_for_seller=True)
                        

                    for ticket in tickets:
                        if ticket.status == 4:
                            ticket.status = 2
                            ticket.save()

        return Response({
            'success': True,
            'message': 'Realizado com Sucesso :)'
        })
    

class ManagersCashierView(FiltersMixin, ModelViewSet):
    queryset = Manager.objects.filter(manager_assoc__payment__status=2).distinct()
    serializer_class = ManagersCashierSerializer
    permission_classes = [ManagerCashierPermission]
    pagination_class = ManagersCashierPagination

    def list(self, request, pk=None):        
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(queryset, many=True)            
            return self.get_paginated_response(serializer.data)                        

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    def get_queryset(self):
        user = self.request.user
        if user.user_type == 3:
            return Manager.objects.filter(pk=user.pk)

        queryset = self.queryset        
        return queryset.filter(my_store=user.my_store)

    
    @action(methods=['post'], detail=False, permission_classes = [CashierCloseManagerPermission])
    def close_manager(self, request, pk=None):
        data = json.loads(request.POST.get('data'))
        managers_ids = data.get('managers_ids')
        data = json.loads(request.POST.get('data'))    
        start_creation_date = data.get('start_creation_date')
        end_creation_date = data.get('end_creation_date')                                

        for manager in Manager.objects.filter(id__in=managers_ids):            
            serializer = ManagersCashierSerializer(manager, context={"request":request})
            data = serializer.data
            
            if not data['comission'] == 0 or not data['entry'] == 0 or not data['out'] == 0:
                revenue_history_manager = ManagerCashierHistory(register_by=request.user, 
                manager=manager, 
                entry=decimal.Decimal(data['entry']),
                comission=decimal.Decimal(data['comission']),
                total_out=decimal.Decimal(data['total_out']),
                profit= decimal.Decimal(data['entry'] - data['total_out']),
                store=request.user.my_store)

                tickets = Ticket.objects.filter(Q(payment__status=2, payment__who_paid__seller__my_manager__pk=manager.pk,store=self.request.user.my_store) &
                (Q(closed_in_for_manager=False) | Q(closed_out_for_manager=False, status__in=[4,2]))).exclude(Q(status__in=[5,6]) | Q(available=False))        
                
                if tickets.exists():
                    if start_creation_date:
                        start_creation_date = datetime.datetime.strptime(start_creation_date, '%d/%m/%Y').strftime('%Y-%m-%d')
                        tickets = tickets.filter(creation_date__date__gte=start_creation_date)
                    if end_creation_date:
                        end_creation_date = datetime.datetime.strptime(end_creation_date, '%d/%m/%Y').strftime('%Y-%m-%d')
                        tickets = tickets.filter(creation_date__date__lte=end_creation_date)        
                    
                    revenue_history_manager.save()
                    revenue_history_manager.tickets_registered.set(tickets)
                    
                    tickets.filter(status__in=[2,4]).update(closed_out_for_manager=True)
                    tickets.update(closed_in_for_manager=True)

        return Response({
            'success': True,
            'message': 'Realizado com Sucesso :)'
        })                


class SellerCashierView(FiltersMixin, ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerCashierSerializer  
    permission_classes = [SellerCashierPermission]  
    pagination_class = SellerCashierPagination

    filter_mappings = {        
        'paid_by': 'pk',        
    }        

    def list(self, request, pk=None):        
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = self.get_serializer(queryset, many=True)            
            return self.get_paginated_response(serializer.data)                        

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):                
        seller = self.request.GET.get('paid_by')        
        if seller:
            return CustomUser.objects.filter(pk=seller)
        elif self.request.user.user_type == 2:
            return CustomUser.objects.filter(pk=self.request.user.pk)

        return CustomUser.objects.none()
                

class ManagerCashierView(FiltersMixin, ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = ManagerCashierSerializer
    permission_classes = [ManagerCashierPermission]
    pagination_class = ManagerCashierPagination

    filter_mappings = {        
        'manager': 'pk',                
    }    
        
    def list(self, request, pk=None):        
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = self.get_serializer(queryset, many=True)            
            return self.get_paginated_response(serializer.data)                        

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):        
        manager = self.request.GET.get('manager')        
        if manager:
            return CustomUser.objects.filter(pk=manager)        
        elif self.request.user.user_type == 3:
            return CustomUser.objects.filter(pk=self.request.user.pk)

        return CustomUser.objects.none()



class ManagerSpecificCashierView(FiltersMixin, ModelViewSet):
    queryset = Seller.objects.filter(payment__status=2).distinct()
    serializer_class = ManagerSpecificCashierSerializer
    permission_classes = [IsManager]    
    pagination_class = ManagerSpecificCashierPagination


    def list(self, request, pk=None):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(queryset, many=True)            
            return self.get_paginated_response(serializer.data)                                        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    def get_queryset(self):
        user = self.request.user        
        return self.queryset.filter(my_manager__pk=user.pk,my_store=self.request.user.my_store)
