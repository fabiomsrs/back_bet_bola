from django.contrib import admin
from user.models import CustomUser
from .models import SellerSalesHistory,ManagerTransactions,RevenueHistorySeller,RevenueHistoryManager, PunterPayedHistory, TicketCancelationHistory
from user.models import CustomUser
from django.utils.translation import gettext_lazy as _


@admin.register(SellerSalesHistory)
class SellerSalesHistoryAdmin(admin.ModelAdmin):
    search_fields = ['seller__username','seller__first_name']
    list_display = ('pk','seller','bet_ticket','sell_date','value','seller_before_balance','seller_after_balance')
    list_display_links = ('pk','seller')
    list_per_page = 20

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        elif request.user.has_perm('user.be_seller'):
            return SellerSalesHistory.objects.filter(seller=request.user.seller)
        
        elif request.user.has_perm('user.be_manager'):
            return SellerSalesHistory.objects.filter(seller__my_manager=request.user.manager)
    
    #def get_list_filter(self, request):
    #    if request.user.is_superuser:
    #        return ('seller','sell_date')



@admin.register(ManagerTransactions)
class ManagerTransactionsAdmin(admin.ModelAdmin):
    search_fields = ['manager__username','manager__first_name','seller__username','seller__first_name']
    list_display = ('pk','manager','seller','transaction_date','transferred_amount','manager_before_balance','manager_after_balance','seller_before_balance','seller_after_balance')
    list_display_links = ('pk','manager')
    list_per_page = 20


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        elif request.user.has_perm('user.be_seller'):
            return ManagerTransactions.objects.filter(seller=request.user.seller)

        elif request.user.has_perm('user.be_manager'):
            return ManagerTransactions.objects.filter(manager=request.user.manager)

    #def get_list_filter(self, request):
    #    if request.user.is_superuser:
    #        return ('manager','seller','transaction_date')
        

@admin.register(RevenueHistorySeller)
class RevenueHistorySellerAdmin(admin.ModelAdmin):
    search_fields = ['seller__username','seller__first_name']
    list_display = ('pk','who_reseted_revenue','seller','revenue_reseted_date','final_revenue','get_commission','earned_value', 'final_out_value', 'profit')
    list_display_links = ('pk','seller')
    list_per_page = 20


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        elif request.user.has_perm('user.be_seller'):
            return RevenueHistorySeller.objects.filter(seller=request.user.seller)

        elif request.user.has_perm('user.be_manager'):
            return RevenueHistorySeller.objects.filter(seller__my_manager=request.user.manager)

    #def get_list_filter(self, request):
    #    if request.user.is_superuser:
    #        return ('who_reseted_revenue','seller','revenue_reseted_date')
        


@admin.register(RevenueHistoryManager)
class RevenueHistoryManagerAdmin(admin.ModelAdmin):
    search_fields = ['manager__username','manager__first_name']
    list_display = ('pk','who_reseted_revenue','manager','revenue_reseted_date','final_revenue','get_commission','earned_value','final_out_value', 'profit')
    list_display_links = ('pk','manager')
    list_per_page = 20


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs
        if request.user.is_superuser:
            return qs

        elif request.user.has_perm('user.be_manager'):
            return RevenueHistoryManager.objects.filter(manager=request.user.manager)


    #def get_list_filter(self, request):
    #    if request.user.is_superuser:
    #        return ('who_reseted_revenue','manager','revenue_reseted_date')



@admin.register(PunterPayedHistory)
class PunterPayedHistoryAdmin(admin.ModelAdmin):
    search_fields = ['punter_payed','seller__username','seller__first_name', 'ticket_winner__id']
    list_display = ('pk','punter_payed','seller','ticket_winner','payment_date','payed_value')
    list_display_links = ('pk','punter_payed')
    list_per_page = 20


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs
        if request.user.is_superuser:
            return qs
        elif request.user.has_perm('user.be_seller'):
            return PunterPayedHistory.objects.filter(seller=request.user.seller)

        elif request.user.has_perm('user.be_manager'):
            return PunterPayedHistory.objects.filter(seller__my_manager=request.user.manager)


        
    #def get_list_filter(self, request):
    #    if request.user.is_superuser:
    #        return ('seller','payment_date')


@admin.register(TicketCancelationHistory)
class TicketCancelationHistoryHistoryAdmin(admin.ModelAdmin):
    search_fields = ['who_cancelled','ticket_cancelled__id']
    list_display = ('pk','ticket_cancelled','who_cancelled','cancelation_date','seller_of_payed')
    fields = ('ticket_cancelled','who_cancelled','seller_of_payed')
    autocomplete_fields = ('ticket_cancelled','seller_of_payed')
    list_display_links = ('pk','ticket_cancelled')
    list_per_page = 20
