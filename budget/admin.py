from django.contrib import admin

# Register your models here.
from budget.models import BudgetList, BudgetCategory, Budget


@admin.register(BudgetList)
class BudgetListAdmin(admin.ModelAdmin):
    pass


@admin.register(BudgetCategory)
class BudgetCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    pass
