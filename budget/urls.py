from django.urls import path

from budget.views import OwnBudgetListCreateView, SharedBudgetListView, OwnBudgetRetrieveUpdateDestroyView, \
    OwnBudgetShareView, OwnBudgetItemsListCreateView, OwnBudgetItemsRetrieveUpdateDestroyView, \
    SharedBudgetItemsListCreateView, SharedBudgetItemsRetrieveUpdateDestroyView, CategoriesListCreateView, \
    CategoriesRetrieveUpdateDestroyView

urlpatterns = [
    path('', OwnBudgetListCreateView.as_view(), name='own_budget_list_create'),
    path('<int:pk>/', OwnBudgetRetrieveUpdateDestroyView.as_view(), name='own_budget_list_retrieve_update_destroy'),
    path('<int:pk>/share/', OwnBudgetShareView.as_view(), name='own_budget_share'),
    path('<int:list_pk>/items/', OwnBudgetItemsListCreateView.as_view(), name='own_budget_items_list_create'),
    path('<int:list_pk>/items/<int:pk>/', OwnBudgetItemsRetrieveUpdateDestroyView.as_view(),
         name='own_budget_items_retrieve_update_destroy'),
    path('shared/', SharedBudgetListView.as_view(), name='shared_budget_list'),
    path('shared/<int:list_pk>/items/', SharedBudgetItemsListCreateView.as_view(),
         name='shared_budget_items_list_create'),
    path('shared/<int:list_pk>/items/<int:pk>/', SharedBudgetItemsRetrieveUpdateDestroyView.as_view(),
         name='shared_budget_items_retrieve_update_destroy'),
    path('categories/', CategoriesListCreateView.as_view(), name='category_list_create'),
    path('categories/<int:pk>/', CategoriesRetrieveUpdateDestroyView.as_view(),
         name='category_retrieve_update_destroy'),
]
