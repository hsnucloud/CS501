# HW5.py
"""
This HW5.py is for the assignment of homework 5 from CS 501 class
Student's name: Chien-Hsien Lin
PUID: 0031982200
"""


# Problem 1
def q1():
    """
    q1() function implements counting the occurrence of letters in the strings
    """
    # Use while loop to add up texts until inputting '\end'
    # Initialize the string list
    string_list = []
    while True:
        t = input("Enter the one-line text: ")
        if '\end' in t:
            t = t[:t.find('\end')]
            if t != '':
                string_list.append(t)
            break
        else:
            string_list.append(t)
    # Output the sorted dictionary of letter occurrence
    if len(string_list) > 0:
        for text in string_list:
            print(frequency(text))
    else:  # If no item in the string list
        print("Error")


def frequency(text: str):
    """
    Count the occurrence of the existing letters in the input string
    :param text: one-line string
    :return: dictionary of occurrence
    """
    # Make the set of exception characters
    exception = {' ', ',', '.', ';', '!', '/', '\\'}
    # Initialize the dictionary
    d = dict()
    for c in text.lower():  # Lower case for the string
        if c in exception:  # Check if having exception char.
            continue
        elif c in d.keys():  # Check if already in the keys of dict.
            d[c] += 1
        else:
            d.update({c: 1})
    # Return the sorted dict. by keys
    return dict(sorted(d.items()))


# ----------------------------------------------------------------------------------------------------------------------


# Problem 2
def q2():
    """
    q2() function implements finding the lower left corner of all points
    """
    # Input the locations
    pts_list = []
    # Initial minimum of x and y
    min_x = 0
    min_y = 0
    while True:
        pt = input("Enter the coordinates of x and y separated by ',': ")
        if pt == '\end':
            break
        else:
            try:
                pt = [float(c) for c in pt.split(',')]
            except:
                print("NOTICE: Enter the numbers and separated the pair by ','. ")
                continue
            else:
                if len(pt) != 2:
                    print("NOTICE: Please enter exactly two coordinates (x, y).")
                    continue
                else:
                    if pt[0] < min_x:
                        min_x = pt[0]
                    if pt[1] < min_y:
                        min_y = pt[1]
                    pts_list.append(pt)
    if pts_list == []:
        print("No input locations")
        return
    # Find the lower left point (minimum distance square to the lower left corner of location boundary)
    distance_pts = dict() # Initial dictionary of {distance_square: points}
    for pt in pts_list:
        d = (pt[0] - min_x)**2 + (pt[1] - min_y)**2 # square distance
        distance_pts.update({d: pt})
    # Find the point with the minimum distance
    llc = tuple(distance_pts[min(distance_pts.keys())])
    print("The lower left corner is {}".format(llc))


def main():
    q1()
    q2()


if __name__ == '__main__':
    main()
