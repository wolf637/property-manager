from .base import TestClassBase

class TestReservations(TestClassBase):


    def test_create_new_room_with_existing_room_type(self):

        # Go to rooms list

        # Push 'Create new room button'

        # Fill out form

        # Push 'Create' button

        # Verify that landed on the rooms list

        # Verify that new room is there

        # Click on room name

        # Verify that all details are in the room details
        pass

    def test_create_new_room_with_new_room_type(self):
        # Go to rooms list

        # Push 'Create new room button'

        # Create new room type

        # Fill the rest of form out

        # Push 'Create' button

        # Verify that landed on the rooms list

        # Verify that new room is there

        # Click on room name

        # Verify that all details are in the room details
        pass


    # TODO Make it data driven
    def test_change_room_attributes(self):

        # Take test room, get its attribute

        # Edit attribute

        # Save changes

        # Go to room details => Verify that changes are saved

        # Make sure user logged in
        pass

    def test_delete_room(self):

        # Create test room

        # Verify that room is visible on the list

        # Verify that has expected attributes

        # Delete the room

        # Verify that rooms is not details

        # Not accessible via url

        # Total number of rooms changed

        pass