from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Ad, Author


class AdAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name="Тест Автор", profile_link="http://example.com", city="Тест Город")
        self.ad = Ad.objects.create(
            title="Тест Объявление",
            ad_id=123456,
            views_count=100,
            position=1,
            author=self.author
        )

    def test_get_ad(self):
        response = self.client.get(f'/api/ads/{self.ad.ad_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.ad.title)
        self.assertEqual(response.data['ad_id'], self.ad.ad_id)
        self.assertEqual(response.data['views_count'], self.ad.views_count)
        self.assertEqual(response.data['position'], self.ad.position)
        self.assertEqual(response.data['author']['name'], self.author.name)
        self.assertEqual(response.data['author']['profile_link'], self.author.profile_link)
        self.assertEqual(response.data['author']['city'], self.author.city)

    def test_get_nonexistent_ad(self):
        response = self.client.get('/api/ads/999999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
