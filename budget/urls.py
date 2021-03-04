from django.urls import path

from budget.views import OwnBudgetListCreateView, SharedBudgetListView

urlpatterns = [
    path('', OwnBudgetListCreateView.as_view(), name='own_budget_list_create'),
    path('shared/', SharedBudgetListView.as_view(), name='shared_budget_list'),
]
