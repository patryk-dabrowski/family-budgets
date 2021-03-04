from django.contrib.auth import get_user_model
from django.db import models


class BudgetList(models.Model):
    author = models.ForeignKey(get_user_model(), related_name='budget_list', on_delete=models.CASCADE)
    share_to = models.ManyToManyField(get_user_model(), related_name='shared_budget_list', blank=True)
    name = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.author})"


class BudgetCategory(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Budget(models.Model):
    BUDGET_INCOME_TYPE = 1
    BUDGET_EXPENSE_TYPE = 2
    BUDGET_TYPES = (
        (BUDGET_INCOME_TYPE, 'income',),
        (BUDGET_EXPENSE_TYPE, 'expense',),
    )

    author = models.ForeignKey(get_user_model(), related_name='budget_item', on_delete=models.CASCADE)
    budget_list = models.ForeignKey(BudgetList, related_name='budget_item', on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    budget_type = models.PositiveSmallIntegerField(choices=BUDGET_TYPES)
    price = models.FloatField()
    category = models.ForeignKey(BudgetCategory, related_name='budget_item', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
