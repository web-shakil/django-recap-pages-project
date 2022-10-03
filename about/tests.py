from django.test import SimpleTestCase


# Create your tests here.

class AboutPageTests(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
