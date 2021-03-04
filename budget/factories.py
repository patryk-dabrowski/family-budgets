import factory
from django.contrib.auth import get_user_model
from faker import Factory

from budget.models import BudgetCategory, Budget, BudgetList

faker = Factory.create()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.LazyAttribute(lambda _: faker.name())
    email = factory.LazyAttribute(lambda _: faker.email())


class BudgetCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BudgetCategory

    name = factory.LazyAttribute(lambda _: faker.word())


class BudgetListFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BudgetList

    author = factory.SubFactory(UserFactory)
    name = factory.LazyAttribute(lambda _: faker.sentence(nb_words=2))


class BudgetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Budget

    author = factory.SubFactory(UserFactory)
    budget_list = factory.SubFactory(BudgetListFactory)
    name = factory.LazyAttribute(lambda _: faker.sentence(nb_words=2))
    budget_type = 1
    price = factory.LazyAttribute(lambda _: faker.random_number())
    category = factory.SubFactory(BudgetCategoryFactory)
