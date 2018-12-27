# Given the radius of a circle, calculate the area.
import numpy
import math

def area(radius):
  area_of_circle= math.pi * pow(radius, 2)
  print(numpy.ceil(area_of_circle))


area(5)