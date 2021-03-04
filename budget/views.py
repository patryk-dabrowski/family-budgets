# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from budget.models import BudgetList
from budget.serializers import BudgetListSerializer


class OwnBudgetListView(generics.ListAPIView):
    queryset = BudgetList.objects.all()
    serializer_class = BudgetListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset
