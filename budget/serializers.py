from rest_framework import serializers

from budget.models import BudgetList, Budget


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


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ('id', 'name', 'budget_type', 'price', 'category', 'created_at', 'updated_at')
