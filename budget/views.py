from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from budget.models import BudgetList, Budget, BudgetCategory
from budget.permissions import IsSharedBudgetPermittedToAccess, IsOwnBudgetPermittedToAccess
from budget.serializers import OwnBudgetListSerializer, SharedBudgetListSerializer, BudgetSerializer, \
    BudgetCategorySerializer


class BudgetListView(generics.ListAPIView):
    queryset = BudgetList.objects.all()
    serializer_class = None
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)


class OwnBudgetRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BudgetList.objects.all()
    serializer_class = OwnBudgetListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)


class OwnBudgetListCreateView(BudgetListView, generics.CreateAPIView):
    serializer_class = OwnBudgetListSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class SharedBudgetListView(BudgetListView):
    serializer_class = SharedBudgetListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(share_to=self.request.user)


class OwnBudgetShareView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        share_to = request.data.get('share_to', [])
        instance = get_object_or_404(BudgetList, pk=pk, author=request.user)
        User = get_user_model()
        users = User.objects.filter(email__in=share_to)
        instance.share_to.set(users)
        return Response({})


class OwnBudgetItemsListCreateView(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = (IsOwnBudgetPermittedToAccess,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filterset_fields = ('category', 'budget_type',)
    search_fields = ('name',)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(budget_list=self.kwargs['list_pk'])

    def perform_create(self, serializer):
        budget_list = get_object_or_404(BudgetList, pk=self.kwargs['list_pk'], author=self.request.user)
        serializer.save(author=self.request.user, budget_list=budget_list)


class OwnBudgetItemsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = (IsOwnBudgetPermittedToAccess,)

    def get_queryset(self):
        queryset = super().get_queryset()
        budget_list = get_object_or_404(BudgetList, pk=self.kwargs['list_pk'])
        return queryset.filter(author=self.request.user, budget_list=budget_list)


class SharedBudgetItemsListCreateView(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = (IsSharedBudgetPermittedToAccess,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filterset_fields = ('category', 'budget_type',)
    search_fields = ('name',)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(budget_list=self.kwargs['list_pk'])

    def perform_create(self, serializer):
        budget_list = get_object_or_404(BudgetList, pk=self.kwargs['list_pk'])
        serializer.save(author=self.request.user, budget_list=budget_list)


class SharedBudgetItemsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = (IsSharedBudgetPermittedToAccess,)

    def get_queryset(self):
        queryset = super().get_queryset()
        budget_list = get_object_or_404(BudgetList, pk=self.kwargs['list_pk'])
        return queryset.filter(budget_list=budget_list)

    def update(self, request, *args, **kwargs):
        self._check_permission(kwargs, request)
        return super(SharedBudgetItemsRetrieveUpdateDestroyView, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self._check_permission(kwargs, request)
        return super(SharedBudgetItemsRetrieveUpdateDestroyView, self).destroy(request, *args, **kwargs)

    def _check_permission(self, kwargs, request):
        queryset = self.get_queryset()
        if not queryset.filter(author=request.user, pk=kwargs['pk']).exists():
            self.permission_denied(request)


class CategoriesBaseView:
    queryset = BudgetCategory.objects.all()
    serializer_class = BudgetCategorySerializer
    permission_classes = (IsAuthenticated,)


class CategoriesListCreateView(CategoriesBaseView, generics.ListCreateAPIView):
    pass


class CategoriesRetrieveUpdateDestroyView(CategoriesBaseView, generics.RetrieveUpdateDestroyAPIView):
    pass
