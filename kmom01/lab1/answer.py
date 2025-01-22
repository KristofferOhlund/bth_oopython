#!/usr/bin/env python3

"""
64a8cff7f8dfa4c96880d1be5093f744
oopython
lab1
v2
kroh24
2025-01-20 11:02:42
v4.0.0 (2019-03-05)

Generated 2025-01-20 12:02:42 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb
from classes import Cat, Duration

# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 1 - oopython
#
# If you need to peek at examples or just want to know more, take a look at
# the [Python documentation](https://docs.python.org/3/library/index.html).
# Here you will find everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Objects and classes
#
# Basic object oriented python.
#
# Create a new file, call it **classes.py**. Write all the classes code in
# this file.
#
# Dont forget to import the file!
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# In classes.py create the class Cat. Add the following instance attributes
# in the Cat class constructor:
# - `eye_color`
# - `name`
# Add a paramater for each attribute in the method definition.
#
# In the code below create a new variable called `cat1` and initiate it with
# a new *Cat object*.
# Give the object the eye color "black" and the name "Gordon".
#
# Use the attributes `eye_color` and `name` from the object to create and
# answer with the string "My cat's name is `name` and has `eye_color` eyes.".
#
# Write your code below and put the answer into the variable ANSWER.
#

cat1 = Cat("black", "Gordon")

ANSWER = f"My cat's name is {cat1.name} and has {cat1.eye_color} eyes."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Expand your Cat class with the private instance attribute `lives_left`.
# Also add a set method and get method for the attribute.
#
# In the constructor deifintion, add `lives_left` as a parameter with a
# default value of `-1`.
#
# In the code below set cat1's lives to the value `6`.
#
# Use the get method to answer with how many lives cat1 has left.
#
# Write your code below and put the answer into the variable ANSWER.
#

cat1.set_lives_left(6)


ANSWER = cat1.get_lives_left()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a new method in the Cat class, called `description`. The method
# should return the string "My cat's name is `name`, has `eye_color` eyes and
# `lives_left` lives left to live.".
#
# Answer with the result returned from `cat1.description()`.
#
# Write your code below and put the answer into the variable ANSWER.
#


ANSWER = cat1.description()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Create a static attribute in the Cat class, "nr_of_paws", that contains the
# number of paws a cat have.
# Assign its value to `4` in the declaration.
#
# Answer with the string "`cat1.name` has `cat1.nr_of_paws` paws.".
#
# Write your code below and put the answer into the variable ANSWER.
#

ANSWER = f"{cat1.name} has {cat1.nr_of_paws} paws."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# In the code below assign `0` to cat1's nr_of_paws.
#
# Answer with the string "`cat1.name` has `cat1.nr_of_paws` paws but cats
# have `Cat.nr_of_paws` paws.".
#
# Write your code below and put the answer into the variable ANSWER.
#

cat1.nr_of_paws = 0

ANSWER = f"{cat1.name} has {cat1.nr_of_paws} paws but cats have {Cat.nr_of_paws} paws."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# Create a new variable called `cat2` and initiate it with a new Cat object.
# Give cat2 the name "Kvothe" and eye color "red".
#
# Put cat1 and cat2 variables in a list. Iterate through the list and
# concatenate the result from their description methods together in a string,
# with a space seperation the two strings.
#
# Answer with the string.
#
# Write your code below and put the answer into the variable ANSWER.
#
cat2 = Cat(name="Kvothe", eye_color="red")

cat_list = [cat1, cat2]
descriptions = []
for cat in cat_list:
    descriptions.append(cat.description())
concatinated_description = " ".join(descriptions)


ANSWER = concatinated_description

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.7 (1 points)
#
# Create a new class named Duration.
# Declare the following instance attributes in the constructor:
# - `hours`
# - `minutes`
# - `seconds`
# Add a parameter for each attribute to the method heading and assign each
# parameter to respective attribute.
#
# Add the method `display` to the class, it should return the duration as a
# string with the format "hh-mm-ss".
# Numbers below 10 should have a leading zero in the string.
#
# Initialize a new *Duration object* and assign it to a variable called
# `duration1`. Give it hours `36`, minutes `1` and seconds `20`.
#
# Answer with the result from the display method.
#
# Write your code below and put the answer into the variable ANSWER.
#
duration1 = Duration(36, 1, 20)

ANSWER = duration1.display()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.7", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.8 (1 points)
#
# Create a static method in the Duration class, name it `duration_to_sec`.
# The method should take one argument, a string in the format as the one
# `display` returns, "hh-mm-ss".
# The method should return the duration it represents converted to number of
# seconds.
#
# Answer with `Duration.duration_to_sec(duration1.display())`.
#
# Write your code below and put the answer into the variable ANSWER.
#


ANSWER = Duration.duration_to_sec(duration1.display())

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.8", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Overriding methods
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Overload the `add operator(+)` in the Duration class.
# It should return the duration of two objects added together, in seconds.
#
# Initialize a new Duration object to a variable called `duration2` , give it
# hours `36`, minutes `23` and seconds `1`.
#
# Answer with `duration1+duration2`.
#
# Write your code below and put the answer into the variable ANSWER.
#

duration2 = Duration(36, 23, 1)


ANSWER = duration1 + duration2

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Overload the `iadd operator(+=)` in the Duration class to update the own
# object with the sum of its own units and the other objects units,
# hours+other.hours, minutes+other.minutes and seconds+other.seconds. If the
# seconds is 60 and higher adjust the minutes and so on. 65 seconds is 1
# minute and 5 seconds.
#
# Initialize a new Duration object to a variable called `duration3` , give it
# hours `2`, minutes `11` and seconds `34`.
# In the code use "+=" to update `duration2` with `duration3`.
#
# Answer with `duration2`s display method.
#
# Write your code below and put the answer into the variable ANSWER.
#

duration3 = Duration(2, 11, 34)
duration2 += duration3


ANSWER = duration2.display()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# Overload the `smaller than operator(<)` in the Duration class.
# It should return True if the duration is shorter than the other.
#
# Answer with `duration1<duration2`.
#
# Write your code below and put the answer into the variable ANSWER.
#


ANSWER = duration1 < duration2

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)


dbwebb.exit_with_summary()
