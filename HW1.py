# HW1.py
"""
This HW1.py is for the assignment of homework 1 from CS 501 class
Student's name: Chien-Hsien Lin
PUID: 0031982200
"""
# Import some functions from math module as well as the graphics module
from math import pi, sqrt, exp
from graphics import *

# Problem 1
def q1():
    """
    q1() function implements the Gaussian Function for the problem 1
    """
    # Input and convert the strings to numbers as parameters
    m = eval(input("enter m: "))
    s = eval(input("enter s: "))
    x = eval(input("enter x: "))

    # Compute the Gaussian Function f(x) with the above parameters
    f = 1/(sqrt(2*pi)*s)*exp(-0.5*((x-m)/s)**2)

    # Print out the results
    print("value of f(x) is", f)
#-----------------------------------------------------------------------------------------------------------------------

# Problem 2
def q2():
    """
    q2() function implements the sum of 10 input numbers for the problem 2
    """
    # Initialize the sum
    sum = 0

    # A for loop to receive the 10 inputs and add them to the sum sequently
    for i in range(10):
        x = eval(input("Enter the number: ")) # Convert the string to numbers
        sum += x # Add it up to the sum

    # Print out the result
    print("Sum is", sum)
#-----------------------------------------------------------------------------------------------------------------------

# Problem 3
def q3():
    """
    q3() function implements the plotting script by graphics for the problem 3
    """
    # Open a graphic window (canvas) with size of 300x300
    window = GraphWin("Question 3", 300, 300)
    window.setBackground("black") # Set up the color of background

    # Draw a circle
    center = Point(100, 100) # location of the center
    c = Circle(center, 50) # circle with a radius of 50
    c.setFill("red") # Fill the circle with red color
    c.draw(window)

    # Draw the text inside the circle
    text_c = Text(Point(100, 100), "Area = 7854 m2") # Create the text
    text_c.setSize(9) # set font size to be 9
    text_c.draw(window)

    # Draw a rectangle
    r = Rectangle(Point(150, 200), Point(250, 250)) # a rectangle with length of 100 and width of 50
    r.setFill("yellow") # Fill the rectangle with yellow color
    r.draw(window)

    # Draw the text inside the rectangle
    text_r = Text(Point(200, 225), "Area = 5000 m2")  # Create the text
    text_r.setSize(9)  # set font size to be 9
    text_r.draw(window)

    # Pause to watch
    wait()

# Pause the program
def wait():
    _ = input("")

# Execute the functions
def main():
    #q1()
    q2()
    #q3()
    return

main()