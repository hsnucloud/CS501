# HW3.py
"""
This HW3.py is for the assignment of homework 3 from CS 501 class
Student's name: Chien-Hsien Lin
PUID: 0031982200
"""

# Problem 1
def q1():
    """
    q1() function implements the Newton's method with input coefficients to solve the root
    """
    # Input the coefficients
    # Type into numbers separated with ','(comma) e.g. 0.6,0.3,0.5
    # Split the input string with ','(comma), convert them to floating numbers, and add them to the new lists
    while True:
        try:
            coeffs = input("Enter the coefficients of the polynomial and separate them with ',': ")
            coeffs = [float(x) for x in coeffs.split(',')]
        except ValueError:
            print("NOTICE: Key in numbers only and separate them with ','. Please try again.")
            continue
        else:
            break
    # Input the initial guess, x0 for Newton's method
    while True:
        try:
            x = float(input("Enter the initial guess: "))
        except ValueError:
            print("NOTICE: Key in one number. Please try again.")
            continue
        else:
            break
    # To find the root
    while True:
        # Calculating f(x_n) and f'(x_n)
        f = 0 # initial function value
        f_d1 = 0 # initial value of first derivative
        for i, c in enumerate(coeffs):
            f += c*x**i
            if not i == 0:
                f_d1 += i*c*x**(i-1)
        # Check if |f(x_n)| < 0.0001, yes-> root found; no-> new x_n+1
        if abs(f) < 0.0001:
            break
        else:
            # New x with Newton's method
            x = x - f/f_d1
    print("The root is {:.5f}".format(x))
    return
#-----------------------------------------------------------------------------------------------------------------------

# Problem 2
def q2():
    """
    q2() function implements the Sentiment Analysis
    """
    # The parameters for positive and negative words
    positive = ('Good', 'Awesome', 'Excellent', 'Great', 'Efficient', 'Bug-free', 'User-friendly')
    negative = ('Bad', 'Bugs', 'Boring', 'Tiresome', 'Poor performance', 'Inefficient')
    # Input the text
    # Use while loop to add up text until inputting '\end'
    text = ""
    while True:
        t = input("Enter the text of review: ")
        if '/end' in t:
            t = t[:t.find('/end')]
            text += t
            break
        else:
            text += t
    # Check if the text is blank
    if text == "":
        print("Indeterminate")
        return
    # Count the word parameters in the text
    p_count = sum(text.count(word) + text.count(word.lower()) for word in positive)
    n_count = sum(text.count(word) + text.count(word.lower()) for word in negative)
    # Print out the count numbers of positive and negative words
    print("No. of positive parameters: {}".format(p_count))
    print("No. of negative parameters: {}".format(n_count))
    # Check if the review is positive, negative, or indeterminate
    if p_count == n_count: # The numbers are equal, including that both counts are zero.
        print("Indeterminate")
    elif p_count > n_count:
        print("Positive")
    else:
        print("Negative")
    return

def main():
    q1()
    q2()

if __name__ == '__main__':
    main()