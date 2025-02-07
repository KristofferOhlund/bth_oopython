"""
Classes for kmom03/lab2
"""

class Person:
    """Person class with a property decorator"""
    def __init__(self, name, ssn, adress=""):
        self.name = name
        self._ssn = ssn
        self.adress = adress


    @property
    def ssn(self):
        """Get private property"""
        return self._ssn


    def set_adress(self, adress):
        """Set adress"""
        self.adress = adress


    def __str__(self):
        if self.adress:
            return f"Name: {self.name} SSN: {self._ssn} {self.adress}"
        return f"Name: {self.name} SSN: {self._ssn}"


class Address:
    """Adress class"""
    def __init__(self, city, state, country):
        self.city = city
        self.state = state
        self.country = country


    def __str__(self):
        """Present Adress class"""
        return f"Address: {self.city} {self.state} {self.country}"


class Teacher(Person):
    """Teacher class"""
    def __init__(self, name, ssn, adress=""):
        super().__init__(name, ssn, adress)
        self.courses = []


    def add_course(self, course):
        """Add course to the list of courses"""
        self.courses.append(course)


    def __str__(self):
        """Override base __str__ method"""
        base_string = super().__str__()
        return f"{base_string} Courses: {', '.join(self.courses)}"


class Student(Person):
    """Student class"""
    def __init__(self, name, ssn, adress=""):
        super().__init__(name, ssn, adress)
        self.courses_grades = []


    def add_course_grade(self, course, grade):
        """Add course and grade to courses"""
        self.courses_grades.append((course, grade))


    def average_grade(self):
        """Calculate average grade"""
        grade_points = 0
        valid_grades = 0
        for course in self.courses_grades:
            if course[1] != "-":
                grade_points += int(course[1])
                valid_grades += 1

        return grade_points / valid_grades


person = Person("Kristoffer", "18282882")
print(person)