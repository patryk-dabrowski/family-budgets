from rest_framework.permissions import BasePermission

from budget.models import BudgetList


class IsSharedBudgetPermittedToAccess(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        list_pk = view.kwargs['list_pk']
        return BudgetList.objects.filter(pk=list_pk, share_to=request.user).exists()


class IsOwnBudgetPermittedToAccess(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        list_pk = view.kwargs['list_pk']
        return BudgetList.objects.filter(pk=list_pk, author=request.user).exists()
