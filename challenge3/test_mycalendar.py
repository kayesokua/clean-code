import unittest
from mycalendar import MyCalendar


class TestMyCalendar(unittest.TestCase):
    def test_day_of_year(self):
        calendar = MyCalendar()
        self.assertEqual(calendar.day_of_year(1, 1, 2023), 1)
        self.assertEqual(calendar.day_of_year(2, 1, 2023), 32)
        self.assertEqual(calendar.day_of_year(3, 1, 2023), 60)
        self.assertEqual(calendar.day_of_year(4, 1, 2023), 91)
        self.assertEqual(calendar.day_of_year(5, 1, 2023), 121)
        self.assertEqual(calendar.day_of_year(6, 1, 2023), 152)
        self.assertEqual(calendar.day_of_year(7, 1, 2023), 182)
        self.assertEqual(calendar.day_of_year(8, 1, 2023), 213)
        self.assertEqual(calendar.day_of_year(9, 1, 2023), 244)
        self.assertEqual(calendar.day_of_year(10, 1, 2023), 274)
        self.assertEqual(calendar.day_of_year(11, 1, 2023), 305)
        self.assertEqual(calendar.day_of_year(12, 1, 2023), 335)

    def test_add_event(self):
        calendar = MyCalendar()
        calendar.add_event("Meeting", 3, 10, 2023)
        self.assertEqual(calendar.get_events(3, 10, 2023), ["Meeting"])
        calendar.add_event("Party", 3, 10, 2023)
        self.assertEqual(calendar.get_events(3, 10, 2023), ["Meeting", "Party"])
        calendar.add_event("", 3, 11, 2023)
        self.assertIsNone(calendar.get_events(3, 11, 2023))

    def test_remove_event(self):
        calendar = MyCalendar()
        calendar.add_event("Meeting", 3, 10, 2023)
        calendar.add_event("Party", 3, 10, 2023)
        calendar.add_event("Lunch", 3, 11, 2023)
        calendar.remove_event("Meeting", 3, 10, 2023)
        self.assertEqual(calendar.get_events(3, 10, 2023), ["Party"])
        calendar.remove_event("Lunch", 3, 11, 2023)
        self.assertIsNone(calendar.get_events(3, 11, 2023))
        calendar.remove_event("Nonexistent Event", 3, 10, 2023)
        self.assertEqual(calendar.get_events(3, 10, 2023), ["Party"])

    def test_get_events(self):
        calendar = MyCalendar()
        self.assertIsNone(calendar.get_events(1, 1, 2023))
        calendar.add_event("Event 1", 1, 1, 2023)
        self.assertEqual(calendar.get_events(1, 1, 2023), ["Event 1"])


if __name__ == "__main__":
    unittest.main()