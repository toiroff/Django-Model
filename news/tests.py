from django.test import TestCase
from django.urls import reverse
from .models import *
# Create your tests here.
class NewsModelTest(TestCase):
    def setUp(self):
        News.objects.create(title="Mavzu",text="yangilik matni")

    def test_text_content(self):
        post = News.objects.get(id=1)
        expected_object_title = f'{News.title}'
        expected_object_text = f"{News.text}"
        self.assertEqual(expected_object_title, "Mavzu")
        self.assertEqual(expected_object_text, "yangilik matni")

class HomePageViewTest(TestCase):
    def setUp(self):
        News.objects.create(title="Mavzu 2",text="boshqa yangilik")

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code ,200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp, 'home.html')