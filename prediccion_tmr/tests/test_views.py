from django.test import TestCase
from django.urls import NoReverseMatch, reverse

# Create your tests here.
class ViewTests(TestCase):
    def setUp(self):
        self.urls = [
            'home',
        ]
    
    def test_get_method_return_200(self):
        """
        Test that all views with get method respond with status code 200.
        """
        for url_name in self.urls:
            try:
                url = reverse(url_name)
                response = self.client.get(url)
                self.assertEqual(
                    response.status_code, 200,
                    f"La vista {url_name} con el metodo GET no responde con 200"
                )
            except NoReverseMatch:
                self.fail(f"No se pudo resolver la URL {url_name}")
                
    def test_post_method_return_200(self):
        """
        Test that all views with post method respond with status code 200.
        """ 
        for url_name in self.urls:
            try:
                url = reverse(url_name)
                response = self.client.post(url)
                self.assertEqual(
                    response.status_code, 200,
                    f"La vista {url_name} con el metodo POST no responde con 200"
                )
            except NoReverseMatch:
                self.fail(f"No se pudo resolver la URL {url_name}")