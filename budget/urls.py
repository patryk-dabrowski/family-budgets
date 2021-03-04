from django.urls import path

from budget.views import OwnBudgetListView, SharedBudgetListView

urlpatterns = [
    path('', OwnBudgetListView.as_view(), name='own_budget_list'),
    path('shared/', SharedBudgetListView.as_view(), name='shared_budget_list'),
]
