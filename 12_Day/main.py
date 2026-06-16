# A module could be a file containing a single variable, a function or a big code base.
# So module is like a package in java that you import.
# You can import Built-in modules or create your own module.
# You can import multiple modules at the top of the file.
# Syntax to call a function in a module- module.funtion(arguments).
# main.py file
import mymodule
print(mymodule.generate_full_name('Satoru', 'Gojo')) # Satoru Gojo

#Import functions from a module
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Satoru','Gojo'))
print(sum_two_nums(1,9))
mass = 100
weight = mass * gravity
print(weight)
print(person['firstname'])

#Import Functions from a Module and Renaming
# main.py file
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Satoru','Gojo'))
print(total(1, 9))
mass = 100 
weight = mass * g
print(weight)
print(p)
print(p['firstname'])

# Built-in modules
# common built-in modules: math, datetime, os,sys, random, statistics, collections, json,re

