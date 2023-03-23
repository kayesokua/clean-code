from collections import defaultdict

class MyCalendar:
    """
    A calendar that can store events and return them based on the date.
    """

    def __init__(self):
        self.events = defaultdict(list)

    def day_of_year(self, month, day_of_month, year):
        days_per_month = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

        # Check if the date is valid
        if month < 1 or month > 12 or day_of_month < 1 or day_of_month > 31:
            return -1

        # Check if the input year is a leap year and adjust day of year if necessary
        if month > 2 and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
            day_of_year = days_per_month[month - 1] + day_of_month + 1
        else:
            day_of_year = days_per_month[month - 1] + day_of_month

        return day_of_year

    def add_event(self, name, month, day_of_month, year):
        day_of_year = self.day_of_year(month, day_of_month, year)
        if name:
            self.events[day_of_year].append(name)

    def remove_event(self, name, month, day_of_month, year):
        day_of_year = self.day_of_year(month, day_of_month, year)
        if day_of_year in self.events:
            self.events[day_of_year].remove(name)
            if not self.events[day_of_year]:
                del self.events[day_of_year]

    def get_events(self, month, day_of_month, year):
        day_of_year = self.day_of_year(month, day_of_month, year)
        return self.events.get(day_of_year)