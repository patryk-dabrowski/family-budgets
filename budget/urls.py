from django.urls import path

from budget.views import OwnBudgetListCreateView, SharedBudgetListView, OwnBudgetDestroyView, OwnBudgetShareView

urlpatterns = [
    path('', OwnBudgetListCreateView.as_view(), name='own_budget_list_create'),
    path('<int:pk>/', OwnBudgetDestroyView.as_view(), name='own_budget_list_destroy'),
    path('<int:pk>/share/', OwnBudgetShareView.as_view(), name='own_budget_share'),
    path('shared/', SharedBudgetListView.as_view(), name='shared_budget_list'),
]
