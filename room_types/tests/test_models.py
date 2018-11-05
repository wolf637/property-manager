from django.test import TestCase
from room_types.models import Bed, RoomType
from .settings import *


class RoomTypesTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.bed = Bed(name=TEST_BED_NAME, occupancy=TEST_BED_OCCUPANCY)
        cls.room_type = RoomType(name=TEST_ROOMTYPE_NAME,
                                 image=TEST_ROOMTYPE_IMAGE,
                                 bed=cls.bed,
                                 num_beds=TEST_NUMBEDS,
                                 rate=TEST_ROOM_RATE)


    def test_roomtype_name(self):
        self.assertEquals(self.room_type.name, TEST_ROOMTYPE_NAME)

    def test_roomtype_name_max_length(self):
        max_length = self.room_type._meta.get_field('name').max_length
        self.assertEquals(max_length, TEST_ROOMTYPE_NAME_MAX_LENGTH)

    def test_roomtype_image(self):
        self.assertEquals(self.room_type.image, TEST_ROOMTYPE_IMAGE)

    def test_roomtypes_bed(self):
        self.assertEquals(self.room_type.bed.name, TEST_BED_NAME)
        self.assertEquals(self.room_type.bed.occupancy, TEST_BED_OCCUPANCY)

    def test_roomtypes_numbeds(self):
        self.assertEquals(self.room_type.num_beds, TEST_NUMBEDS)

    def test_roomtypes_rate(self):
        self.assertEquals(self.room_type.rate, TEST_ROOM_RATE)


    def test_roomtype_rate_default(self):

        new_room_type = RoomType(name=TEST_ROOMTYPE_NAME,
                                 image=TEST_ROOMTYPE_IMAGE,
                                 bed=self.bed,
                                 num_beds=TEST_NUMBEDS)
        self.assertEquals(new_room_type.rate, TEST_DEFAULT_RATE)


    def test_roomtype_numbeds_default(self):

        new_room_type = RoomType(name=TEST_ROOMTYPE_NAME,
                                 image=TEST_ROOMTYPE_IMAGE,
                                 bed=self.bed,
                                 rate=TEST_ROOM_RATE)

        self.assertEquals(new_room_type.num_beds, TEST_DEFAULT_NUMBEDS)


    def test_roomtype_string_representation(self):
        self.assertEquals(str(self.room_type), TEST_ROOMTYPE_NAME)


    def test_roomtype_occupancy(self):
        occupancy = self.room_type.bed.occupancy * self.room_type.num_beds
        self.assertEquals(self.room_type.occupancy(), occupancy)


class BedTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.bed = Bed(name=TEST_BED_NAME, occupancy=TEST_BED_OCCUPANCY)


    def test_name(self):
        self.assertEquals(self.bed.name, TEST_BED_NAME)

    def test_name_max_length(self):
        max_length = self.bed._meta.get_field('name').max_length
        self.assertEquals(max_length, TEST_BED_NAME_MAX_LENGTH)

    def test_bed_occupancy(self):
        self.assertEquals(self.bed.occupancy, TEST_BED_OCCUPANCY)

    def test_bed_string_representation(self):
        self.assertEquals(str(self.bed), TEST_BED_NAME)
