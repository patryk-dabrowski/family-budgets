from django.urls import path

from budget.views import OwnBudgetListView

urlpatterns = [
    path('', OwnBudgetListView.as_view(), name='own_budget_list'),
]
