from rest_framework import serializers

from budget.models import BudgetList


class BudgetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetList
        fields = ('id', 'name', 'share_to', 'created_at', 'updated_at',)
