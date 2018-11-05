from .settings import *
from tests.base.base_unit import BaseUnitTest


class PropertyModelsTest(BaseUnitTest):

    def test_property_name(self):
        self.assertEquals(self.property.name, self.settings.TEST_PROPERTY_NAME)

    def test_name_max_length(self):
        max_length = self.property._meta.get_field('name').max_length
        self.assertEquals(max_length, TEST_PROPERTY_NAME_MAX_LENGTH)

    def test_picture(self):
        self.assertEquals(self.property.picture, self.settings.TEST_PICTURE)

    def test_string_representation(self):
        self.assertEquals(str(self.property), self.settings.TEST_PROPERTY_NAME)