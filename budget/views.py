from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from budget.models import BudgetList
from budget.serializers import OwnBudgetListSerializer, SharedBudgetListSerializer


class BudgetListView(generics.ListAPIView):
    queryset = BudgetList.objects.all()
    serializer_class = None
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)


class OwnBudgetDestroyView(generics.DestroyAPIView):
    queryset = BudgetList.objects.all()
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
