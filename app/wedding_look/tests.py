from django.test import TestCase

from django.urls import reverse

class IndexViewTestCase(TestCase):
    def test_view(self):
        path = reverse('index')
        response = self.client.get(path)
        print(response)
