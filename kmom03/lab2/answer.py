#!/usr/bin/env python3
"""
21f557b505249f8d2d562caa07d91e92
oopython
lab2
v2
kroh24
2025-02-06 20:31:20
v4.0.0 (2019-03-05)

Generated 2025-02-06 21:31:20 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""
import classes

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 2 - oopython
#
# If you need to peek at examples or just want to know more, take a look at
# the [Python documentation](https://docs.python.org/3/library/index.html).
# Here you will find everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Class relationships
#
# Practice on creating classes and relationships between them in python.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (2 points)
#
# Create a new file, put your code for the classes in it, call it
# **classes.py**.
#
# Create a new class named **Person**.  Give the class the instance
# attributes "name" and "ssn". Make "ssn" a private attribute. The values for
# the attributes should be sent to the constructor as arguments.
# Create a *get* property for "ssn".
#
# In the code below create a new variable called **per** and set it to a new
# instance of Person. Give it the name `Zimba` and ssn `619172-0731`.
#
#
# Answer with per\'s getter for ssn.
#
# Write your code below and put the answer into the variable ANSWER.
#

per = classes.Person("Zimba", "619172-0731")




ANSWER = per.ssn

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (2 points)
#
# Create a new class named **Address**.  Give the class the instance
# attributes "city", "state" and "country". The values for the attributes
# should be sent to the constructor as arguments.
# Create the magic method **_\_str_\_**, in Address, it should return
# `"Address: <city> <state> <country>"` (replace the \<city\> with the value
# of the attribute city...).
#
# Create a new instance of the class Address. Initiate it with the city
# `Imre`, the state `Vansterland` and the country `Tear` and store it in a
# variable called **per_address**.
#
# Now, go back and add the instance attribute **address** to your Person
# class. It's value should be sent as argument to constructor, give it a
# default value of and empty string, `""`.
# Create a set method for the attribute "address".
#
# Create the magic method **_\_str_\_** for Person, it should return `"Name:
# <name> SSN: <ssn> Address: <city> <state> <country>"` if the person has an
# address or, `"Name: <name> SSN: <ssn>"` if its an empty string.
#
# Use Address' string representation to get address the data.
#
# Use the set method in Person to add the newly create Address object to your
# **per** object.
#
# Answer with per's string representation.
#
# Write your code below and put the answer into the variable ANSWER.
#

per_adress = classes.Address("Imre", "Vansterland", "Tear")
per.set_adress(per_adress)


ANSWER = str(per)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (2 points)
#
# Create a new class name **Teacher** make it inherit from class "Person".
# Add the instance attribute "courses" and initiate it to and empty list.
# Create the method **add_course**, it should take one argument and add it to
# the course list attribute.
# Overload the `__str__` method from the base class. It should return the
# same as the original method and add the courses to the end of the string,
# `"Name: <name> SSN: <ssn> Address: <city> <state> <country> Courses:
# <course>, <course>, ..."`. The list of courses should be comma seperated
# without one at the end. Use `super()` to access base method.
#
#
# Create a new instance of the class Teacher. Initiate it with the name
# `Buster` and ssn `619172-0731`.
# Use the add_course method to add the following courses, `webapp`,
# `ramverk1` and `linux`.
#
#
# Answer with the Teacher object's string representation.
#
# Write your code below and put the answer into the variable ANSWER.
#

teacher = classes.Teacher("Buster", "619172-0731")
courses = ["webapp", "ramverk1", "linux"]
for course in courses:
    teacher.add_course(course)

print(teacher.adress)

ANSWER = str(teacher)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (2 points)
#
# Create a new class name **Student** make it inherit from class "Person".
# Add the instance attribute "courses_grades" and initiate it to and empty
# list.
# Create the method **add_course_grade**, it should take two arguments, one
# course and a grade. Create a tuple with the two arguments and add to the
# attribute "courses_grades".
# Create the method **average_grade**. Calculate and return the students
# average grade. Ignore grades with "-" in the calculation.
#
# Create a new instance of the class Student. Initiate it with the name
# `Kvothe` and ssn `502075-3392`.
# Use the add_course_grade method to add the following courses, `linux` with
# grade `5`, `oophp` with grade `-` and `oophp` with grade `2`.
#
#
# Answer with the Student object's "average_grade" method.
#
# Write your code below and put the answer into the variable ANSWER.
#

student = classes.Student("Kvothe", "502075-3392")
courses = [("linux", 5),("oophp", "-"),("oophp", 2)]
for course, grade in courses:
    student.add_course_grade(course, grade)


ANSWER = student.average_grade()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)


dbwebb.exit_with_summary()
