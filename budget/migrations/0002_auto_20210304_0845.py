# Generated by Django 3.1.7 on 2021-03-04 08:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgetlist',
            name='share_to',
            field=models.ManyToManyField(blank=True, related_name='shared_budget_list', to=settings.AUTH_USER_MODEL),
        ),
    ]
