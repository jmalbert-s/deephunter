from django.test import TestCase, Client
from django.test import TestCase, Client
from django.urls import reverse
from .models import Repo
from config.models import ApiKey

class RepoAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.repo1 = Repo.objects.create(
            name='Test Repo 1',
            url='https://github.com/test/repo1'
        )
        self.repo2 = Repo.objects.create(
            name='Test Repo 2',
            url='https://github.com/test/repo2',
            is_private=True,
            token='secret'
        )
        self.api_key = ApiKey.objects.create(name='Test Key', key='testkey123', key_type='READ')

    def test_get_repos(self):
        response = self.client.get(reverse('api_repos'), HTTP_AUTHORIZATION=f'Bearer {self.api_key.key}')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data['data']), 2)

    def test_get_repo_detail(self):
        response = self.client.get(reverse('api_repo_detail', args=[self.repo1.pk]), HTTP_AUTHORIZATION=f'Bearer {self.api_key.key}')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['data']['name'], 'Test Repo 1')
        self.assertFalse(data['data']['is_private'])
