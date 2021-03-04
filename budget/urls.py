from django.urls import path

from budget.views import OwnBudgetListCreateView, SharedBudgetListView, OwnBudgetDestroyView

urlpatterns = [
    path('', OwnBudgetListCreateView.as_view(), name='own_budget_list_create'),
    path('<int:pk>/', OwnBudgetDestroyView.as_view(), name='own_budget_list_destroy'),
    path('shared/', SharedBudgetListView.as_view(), name='shared_budget_list'),
]
