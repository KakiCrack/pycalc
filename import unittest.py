import unittest
from resa import bookMeetingRoom

class MeetingRoomTest(unittest.TestCase):

    def test_should_book_small_room(self):
        self.assertEqual("smallRoom", bookMeetingRoom(5))

    def test_should_book_medium_room(self):
        self.assertEqual("mediumRoom", bookMeetingRoom(20))

    def test_should_book_large_room(self):
        self.assertEqual("largeRoom", bookMeetingRoom(40))

    def test_should_refuse_reservation(self):
        self.assertEqual("refuse", bookMeetingRoom(60))

    def test_should_throw_error_if_participants_less_than_one(self):
        with self.assertRaises(ValueError):
            bookMeetingRoom(0)

if __name__ == "__main__":
    unittest.main()



