"""Module for practicing classes"""


class Cat:
    """Class representing a class"""
    nr_of_paws = 4

    def __init__(self, eye_color, name, lives_left=-1):
        self.eye_color = eye_color
        self.name = name
        self._lives_left = lives_left

    def set_lives_left(self, lives):
        """Method for getting lives left"""
        self._lives_left = lives

    def get_lives_left(self):
        """Method for setting lives left"""
        return self._lives_left

    def description(self):
        """Method for describing the cat instance"""
        long_string = (f"My cat's name is {self.name},"
                      f" has {self.eye_color} eyes and "
                      f"{self._lives_left} lives left to live.")
        return long_string



class Duration:
    """Class for representing Durating in hours-minutes-seconds"""

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def display(self):
        """Method for displaying current duration.
        If number < 10, adds a leading 0."""
        display_list = []
        for number in [self.hours, self.minutes, self.seconds]:
            if number < 10:
                display_list.append("0" + str(number))
            else:
                display_list.append(str(number))
        display_string = "-".join(display_list)

        return display_string

    @staticmethod
    def duration_to_sec(duration):
        """Static method for converting a duration string in format hh-mm-ss to total 
        number of seconds, as int."""
        hh, mm, ss = duration.split("-")
        time_in_seconds = 0
        time_in_seconds += int(hh) * 3600
        time_in_seconds += int(mm) * 60
        time_in_seconds += int(ss)
        return time_in_seconds


    def __add__(self, other):
        """Method for overloading the + operator. 
        Sums the total number of seconds of two duration objects."""
        return Duration.duration_to_sec(self.display()) + Duration.duration_to_sec(other.display())


    def __iadd__(self, other):
        """Method for overloading the += operator.
        Update the sum of its own units and the other objects units, if
        minutes are higher then 60, add 1 hour, if seconds is higher then 60, add 1 minut."""
        self.hours += other.hours
        self.minutes += other.minutes
        self.seconds += other.seconds

        # while self.seconds > 59:
        #     self.minutes += 1
        #     self.seconds -= 60

        # while self.minutes > 59:
        #     self.hours += 1
        #     self.minutes -= 60


        # hours = self.hours + other.hours
        # minutes = self.minutes + other.minutes
        # seconds = self.seconds + other.seconds

        # while seconds < 59:
        #     minutes += 1

        # while minutes > 59:
        #     hours += 1

        # # Update self
        # self.hours = hours
        # self.minutes = minutes
        # self.seconds = seconds


duration2 = Duration(36, 23, 1)
duration3 = Duration(2, 11, 34)

duration2 += duration3