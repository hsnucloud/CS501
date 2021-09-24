# HW2.py
"""
This HW2.py is for the assignment of homework 2 from CS 501 class
Student's name: Chien-Hsien Lin
PUID: 0031982200
"""

# Problem 1
def q1():
    """
    q1() function implements the sum of products with two input lists for problem 1
    """
    # Input the two lists of number
    # Type into numbers separated with ','(comma) e.g. 0.6,0.3,0.5
    # Split the input string with ','(comma), convert them to floating numbers, and add them to the new lists
    while True:
        try:
            l1_s = input()
            l1 = [eval(x) for x in l1_s.split(',')]
        except SyntaxError:
            print("Input numbers only and separate them with comma.\nInput again:")
            continue
        else:
            break
    while True:
        try:
            l2_s = input()
            l2 = [eval(x) for x in l2_s.split(',')]
        except SyntaxError:
            print("Input numbers only and separate them with comma.\nInput again:")
            continue
        else:
            break
    # The lengths of the two lists
    m, n = len(l1), len(l2)
    # Initialize the sum
    sum = 0
    # Calculate the sum of products between the elements from the two lists
    for i in range(m):
        for j in range(n):
            sum += l1[i]*l2[j]
    # Output the result with two digits after the decimal
    print("Sum of products:{:.2f} ".format(sum))
#-----------------------------------------------------------------------------------------------------------------------

# Problem 2
def q2():
    """
    q2() function implements the text replacement for the problem 2
    """
    # (a)
    # Input the word list
    # Use while loop to append the words until inputting '\end'
    word_list = []
    while True:
        s = input()
        if s == '\end':
            break
        else:
            word_list.append(s)
    # (b)
    # Input the text
    # Use while loop to add up text until inputting '\end'
    text = ""
    while True:
        t = input()
        if t == '\end':
            break
        else:
            text += t
    # (c)
    # Replace the punctuation marks (, ? . !) in the text with spaces
    p_marks = ('.', ',', '?', '!')
    for x in p_marks:
        text = text.replace(x, ' ')
    # (d)
    # Check if the word is contained within the text
    # Then replace the word with its palindrome
    for x in word_list:
        if x in text:
            text = text.replace(x, x[::-1])
    # (e)
    # Print out the result
    print(text)


# Execute the functions
def main():
    q1()
    q2()
    return

if __name__ == '__main__':
    main()