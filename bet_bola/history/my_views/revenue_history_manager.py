from rest_framework.viewsets import ModelViewSet
from history.permissions import BaseHistoryPermission
from history.serializers.revenue_history_manager import RevenueHistoryManagerSerializer
from history.models import RevenueHistoryManager

class RevenueHistoryManagerView(ModelViewSet):
    queryset = RevenueHistoryManager.objects.all()
    serializer_class = RevenueHistoryManagerSerializer
    permission_classes = [BaseHistoryPermission]
    