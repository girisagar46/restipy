from django.test import TestCase, RequestFactory
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from django.conf import settings as s

from restipy import views


class TestAllAPIView(TestCase):
    def setUp(self) -> None:
        self.env_view_url = reverse('env_view')
        self.info_view_url = reverse('info_view')
        self.health_view_url = reverse('health_view')
        self.endpoint0_view_url = reverse('endpoint0_view')
        self.factory = APIRequestFactory()

    def test_home_view(self):
        view = views.Environment.as_view()
        request = self.factory.get(self.env_view_url)
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['version'], s.VERSION)

    def test_info_view(self):
        view = views.Info.as_view()
        request = self.factory.get(self.info_view_url)
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['version'], s.VERSION)

    def test_health_view(self):
        view = views.Health.as_view()
        request = self.factory.get(self.health_view_url)
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data['healthy'], bool)

    def test_endpoint0_view(self):
        view = views.Endpoint0.as_view()
        request = self.factory.get(self.endpoint0_view_url)
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['version'], s.VERSION)

    def tearDown(self) -> None:
        del self
