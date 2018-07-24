from .base import TestClassBase

class TestReservations(TestClassBase):


    # TODO Keep track of all test object so they can be removed on tear_down_class
    def test_create_reservation(self):

        # Go to reservations list

        # Start creating reservation

        # Save reservation

        # Verify that reservation is in the list

        # Verify that reservation is accessible via reservation details with correct attributes

        pass

    # TODO Make it data driven
    def test_update_reservation(self):

        # Create reservation

        # Update reservation with new attributes

        # Save reservation

        # Verify new attributes on the reservations list

        # Verify new attributes on reservation details

        pass

    def test_delete_reservation(self):

        # Create reservation

        # Verify that it is created

        # Delete reservation

        # Verify that reservation is not in the list

        # Verify that reservation is not accessible via url

        # Verify that room freed is available now

        pass