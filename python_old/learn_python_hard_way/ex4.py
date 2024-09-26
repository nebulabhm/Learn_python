# -*- coding: utf-8 -*-
# @FileName:ex4.py
# @Author: nebulabhm760
# @Date:   2017-06-08 15:31:06
# @Last Modified by:   nebulabhm760
# @Last Modified time: 2017-06-08 16:41:11
# @Descreption:

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars -  drivers
cars_driven = drivers
carpool_capacity = cars_driven *space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


