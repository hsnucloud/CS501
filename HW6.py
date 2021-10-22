# HW6.py
"""
This HW5.py is for the assignment of homework 6 from CS 501 class
Student's name: Chien-Hsien Lin
PUID: 0031982200
"""

import numpy as np
import matplotlib.pyplot as plt

class multiPolyFit():
    """
    class for loading x-y data and poly. fit the data with passing a list of degrees
    """
    def __init__(self, x=[], y=[]):
        self.x = []
        self.y = []
        self.p_coeff = []

    # Load the x-y data from the file
    def loadXY(self, file_name):
        with open(file_name, 'r') as f:
            text = f.readlines()
            self.x.clear()
            self.y.clear()
            for pt in text:
                pt = pt.rstrip('\n')
                coords = pt.split(',')
                self.x.append(float(coords[0]))
                self.y.append(float(coords[1]))

    # poly. fit the data with passing a list of degrees
    def polyFit(self, degs: list):
        l = len(degs)
        self.p_coeff.clear()
        for i in range(l):
            self.p_coeff.append(np.polyfit(self.x, self.y, degs[i]))

    # return x
    def getX(self):
        return self.x

    # return y
    def getY(self):
        return self.y

    # return the coefficients of the fitted polynomials
    def getFitCoeffs(self):
        return self.p_coeff

def main():
    # Create instance
    fit_data = multiPolyFit()
    fit_data.loadXY("data.txt")
    # Input the degrees
    while True:
        try:
            deg = input("Please enter the degree(s) for the polynomial fitting: ").split(',')
            deg = [int(i) for i in deg]
        except:
            print("NOTICE: Enter integers and separate them by ','")
        else:
            break
    # Poly. fitting with the list of degrees
    fit_data.polyFit(deg)
    px = fit_data.getFitCoeffs() # The coefficients
    # Plot the data
    data_x = fit_data.getX()
    data_y = fit_data.getY()
    fig, ax = plt.subplots()
    ax.plot(data_x, data_y, 'r.', markersize=12, label='data')
    # Plot the interpolations
    fit_x = np.linspace(min(data_x), max(data_x), 100) # 100 x points
    for i in range(len(px)):
        ax.plot(fit_x, np.polyval(px[i], fit_x), label='order = ' + str(deg[i]))
    ax.set(xlabel='x', ylabel='y', title='Polynomial Interpolation') # Set axial labels
    ax.legend() # Enable legends
    plt.grid(True) # Enable grids
    plt.show()

if __name__ == '__main__':
    main()
