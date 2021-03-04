from django.urls import path

from budget.views import OwnBudgetListCreateView, SharedBudgetListView, OwnBudgetRetrieveUpdateDestroyView, \
    OwnBudgetShareView, OwnBudgetItemsListCreateView

urlpatterns = [
    path('', OwnBudgetListCreateView.as_view(), name='own_budget_list_create'),
    path('<int:pk>/', OwnBudgetRetrieveUpdateDestroyView.as_view(), name='own_budget_list_retrieve_update_destroy'),
    path('<int:pk>/share/', OwnBudgetShareView.as_view(), name='own_budget_share'),
    path('<int:list_pk>/items/', OwnBudgetItemsListCreateView.as_view(), name='own_budget_items'),
    path('shared/', SharedBudgetListView.as_view(), name='shared_budget_list'),
]
