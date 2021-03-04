# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from budget.models import BudgetList
from budget.serializers import OwnBudgetListSerializer, SharedBudgetListSerializer


class BudgetListView(generics.ListAPIView):
    queryset = BudgetList.objects.all()
    serializer_class = None
    permission_classes = (IsAuthenticated,)


class OwnBudgetListView(BudgetListView):
    serializer_class = OwnBudgetListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)


class SharedBudgetListView(BudgetListView):
    serializer_class = SharedBudgetListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(share_to=self.request.user)
