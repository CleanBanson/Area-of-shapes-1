



"""
Author: Matthew Harris
Date: April 27, 2022
File: Area_Of_Shapes.py
"""




from cmath import pi
import math
from curses.textpad import rectangle

print('This is a numbers magic trick. I will calculate the area as well as volumes\nof shapes based off of the numbers that you give me.\nAnd I will do so in the blink of an eye.')
ready_to_play = input('Are you ready? Y/N ')
if ready_to_play.upper() == 'Y':
    print()
else:
    quit()

square_length = float(input('What is the length of one of the sides of the square in centimeters? '))
square_area = square_length ** 2
square_area_meter = square_area / 10000
print(f'The area of the square in centimeters is {square_area}.')
print(f'The area of the square in meters is {square_area_meter}.')

print()
print()

rectangle_length = float(input('What is the length of the rectangle in centimeters? '))
rectangle_Width = float(input('What is the width of the rectangle in centimeters? '))
rectangle_area = rectangle_length * rectangle_Width
rectangle_area_meter = rectangle_area / 10000
print(f'The area of the rectangle in centimeters is {rectangle_area}.')
print(f'The area of the rectangle in meters is {rectangle_area_meter}.')

print()
print()

circle_radius = float(input('What is the radius of the circle in centimeters? '))
#pi = 3.14
circle_area = pi * (circle_radius * circle_radius)
circle_area_meter = circle_area / 10000
print(f'The area of the circle in centimeters is {circle_area}.')
print(f'The area of the circle in meters is {circle_area_meter}.')

print()
print()

print('Now for my next trick I will calculate the area of a square and a circle, aswell as the volume of a cube and a sphere...\nall with the single number you shall provide me....')
number = float(input('What number do you choose? '))

print()


area_square = number ** 2
area_circle = pi * (number ** 2)
volume_square = number ** 3
volume_sphere = (4 / 3) * pi * (number ** 3)


print(f'The area of the square is {area_square}.')
print(f'The area of the circle is {area_circle}.')
print(f'The volume of the cube is {volume_square}.')
print(f'The volume of the sphere is {volume_sphere}.')









