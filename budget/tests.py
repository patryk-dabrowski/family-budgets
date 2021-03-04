from django.urls import reverse
from rest_framework.test import APITestCase

from budget.factories import UserFactory, BudgetListFactory, BudgetFactory


class SharedBudgetListViewTest(APITestCase):
    def setUp(self) -> None:
        self.users = UserFactory.create_batch(3)
        self.budget_list = BudgetListFactory(author=self.users[0])
        self.budget_list.share_to.add(self.users[1])
        BudgetFactory.create_batch(5, budget_list=self.budget_list)
        self.url = reverse('shared_budget_items_list_create', args=[self.budget_list.pk])

    def test_list_shown_for_shared(self):
        self.client.force_authenticate(self.users[1])
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('count'), 5)

    def test_access_denied_for_others(self):
        self.client.force_authenticate(self.users[2])
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 403)
