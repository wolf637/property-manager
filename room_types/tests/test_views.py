from tests.base.base_unit import BaseUnitTest
from .settings import *
from room_types.models import Bed, RoomType
from django.urls import reverse
from io import BytesIO

class RoomTypeViewTest(BaseUnitTest):

    def test_create_valid_room_type(self):

        self.login()
        url = reverse('room_types:create_room_type')
        payload = self._create_roomtype()
        response = self.client.post(path=url, data=payload)
        redirect_url = '/room_types/1'
        self.assertRedirects(response, redirect_url)
        self.logout()

    def _create_roomtype(self):
        bed = Bed.objects.create(name=TEST_BED_NAME, occupancy=TEST_BED_OCCUPANCY)
        img = BytesIO(b'test_roomtype_image.png')
        img.name = TEST_ROOMTYPE_IMAGE

        payload = {'room_type_name': TEST_ROOMTYPE_NAME,
                   'bed_type': bed.id,
                   'num_beds': TEST_NUMBEDS,
                   'rate': TEST_ROOM_RATE,
                   'room_img': img}
        return payload

    def test_unathenticated_user_creating_roomtype_gets_redirected_to_login(self):

        url = reverse('room_types:create_room_type')
        redirect_url = '/login/?next={url}'.format(url=url)
        response = self.client.get(url)
        self.assertRedirects(response, redirect_url)

    def test_get_roomtype_details(self):

        self.login()
        bed = Bed.objects.create(name=TEST_BED_NAME, occupancy=TEST_BED_OCCUPANCY)
        new_room_type = RoomType.objects.create(name=TEST_ROOMTYPE_NAME,
                                 image=TEST_ROOMTYPE_IMAGE,
                                 bed=bed,
                                 num_beds=TEST_NUMBEDS,
                                 rate=TEST_ROOM_RATE)
        url = reverse('room_types:room_type_details', args=(new_room_type.pk,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('room_types/details.html')
        self.assertEquals(response.context['type'], new_room_type)
        self.logout()