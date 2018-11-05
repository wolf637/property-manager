from .test_base import PropertyBaseTest
from django.urls import reverse

class PropertyModelsTest(PropertyBaseTest):


    def test_get_details(self):

        self.login()
        url = reverse('properties:property_details', args=(self.property.pk,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_unathenticated_user_gets_redirected_to_login(self):

        url = reverse('properties:property_details', args=(self.property.pk,))
        redirect_url = f'/login/?next={url}'
        response = self.client.get(url)
        self.assertRedirects(response, redirect_url)


