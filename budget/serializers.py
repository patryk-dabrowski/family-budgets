from django.contrib.auth import get_user_model
from rest_framework import serializers

from budget.models import BudgetList, Budget, BudgetCategory


class BudgetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetList
        fields = ('id', 'name', 'created_at', 'updated_at',)


class OwnBudgetListSerializer(BudgetListSerializer):
    class Meta:
        model = BudgetListSerializer.Meta.model
        fields = BudgetListSerializer.Meta.fields + ('share_to',)


class SharedBudgetListSerializer(BudgetListSerializer):
    pass


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email',)


class BudgetSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Budget
        fields = ('id', 'author', 'name', 'budget_type', 'price', 'category', 'created_at', 'updated_at')


class BudgetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetCategory
        fields = ('id', 'name',)
