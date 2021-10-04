# HW4.py
"""
This HW4.py is for the assignment of homework 4 from CS 501 class
Student's name: Chien-Hsien Lin
PUID: 0031982200
"""
from math import sqrt, floor

# Problem 1
def q1():
    """
    q1() function implements to find out prime numbers in an interval from 1 to an input number
    """
    # Input the first number for the upper boundary of an interval
    while True:
        try:
            num1 = int(input("Enter the first integer: "))
        except ValueError:
            print("NOTICE: Only integers are acceptable. Input again.")
        else:
            if num1 <= 1:
                print("NOTICE: Enter a number larger than 1.")
                continue
            else:
                break
    # Generate the list of prime numbers with the upper range of num1
    prime_list = prime_list_upper(num1)
    #print(prime_list)
    while True:
        try:
            num2 = int(input("Enter the second integer: "))
        except ValueError:
            print("NOTICE: Only integers are acceptable. Input again.")
        else:
            if num1 <= 1:
                print("NOTICE: Enter a number larger than 1.")
                continue
            else:
                break
    # Find the closest number in the prime list with the input num2
    closest = closest_number(prime_list, num2)
    print("Closest prime number: {}".format(closest))

# Find prime numbers
def prime_list_upper(upper_number):
    """
    Find prime numbers within the range from 1 to the input number
    :param upper_number: the upper bound of the range
    :return: prime_list
    """
    prime_list = [] # Because we know num1 > 1
    for n in range(2, upper_number+1):
        if n == 2: # 2 is the initial prime number
            prime_list.append(n)
        elif n == 3: # 3 is the second prime number
            prime_list.append(n)
        else:
            n_r = floor(sqrt(n)) # Use square root of the current number to reduce the searching range
            # Check the current number with the factors of current prime number list
            for i, p in enumerate(prime_list):
                if (n % p) == 0: # Not a prime number
                    break
                elif p > n_r: # stop estimating when prime number from the list > square root of the current number
                    prime_list.append(n)
                    break
                else: # Continue to check with next prime factor
                    pass
    return prime_list

# Find the closest number in a sorted list
def closest_number(sorted_list, target):
    """
    Find an element of a sorted list which is the closest to the target number
    :param sorted_list: a sorted list with values
    :param target: target number
    :return: the closest number of element
    """
    if target > sorted_list[-1]:
        closest = sorted_list[-1]
    elif target in sorted_list:
        closest = target
    else:
        # Short script with built-in function min()
        # closest = min(prime_list, key=lambda x: abs(x-num2))
        # Long script with written bisect algorithm
        interval = [0, len(sorted_list)-1] # Initial interval of bisection
        for i in range(floor(len(sorted_list)/2)):
            m = floor(sum(interval) / 2)
            if target < sorted_list[m]:
                interval[1] = m
            elif target == sorted_list[m]:
                closest = sorted_list[m]
                break
            else:
                interval[0] = m
            # Leave the loop if the interval is the smallest
            if interval[1] - interval[0] == 1:
                break
        #print(sorted_list[interval[0]], sorted_list[interval[1]])
        # Check which prime number is closer to target
        if abs(target - sorted_list[interval[0]]) < abs(target - sorted_list[interval[1]]):
            closest = sorted_list[interval[0]]
        elif abs(target - sorted_list[interval[0]]) == abs(target - sorted_list[interval[1]]):
            closest = sorted_list[interval[0]] # the smaller one if equidistant
        else:
            closest = sorted_list[interval[1]]
    return closest

# -----------------------------------------------------------------------------------------------------------------------
# Problem 2
def q2():
    """
    q2() function implements to find the indexes of two number with an equal sum of the target number
    """
    # Input the list of integers
    while True:
        try:
            integers = input("Enter the integers and separate them with ',': ")
            integers = [int(x) for x in integers.split(',')]
        except ValueError:
            print("NOTICE: Enter integer numbers only and separate them with ','. Please try again.")
            continue
        else:
            break
    # Input the target number of sum
    while True:
        try:
            target_sum = int(input("Enter the target sum: "))
        except ValueError:
            print("NOTICE: Enter one integer. Please try again.")
            continue
        else:
            break
    # Find the indexes of the two numbers summing up equal to the target
    indexes = findSum(integers, target_sum)
    print("The indexes are {}".format(indexes))

# Find the two numbers summing up equal to the target
def findSum(input_list, target_sum):
    """
    Find the indexes of two numbers summing up equal to the target with hash mapping
    :param input_list: the input list of number elements
    :param target_sum: the input target sum
    :return: the list of indexes
    """
    # Initial hash map
    record_hash = dict() # num: index
    # Check the subtraction within the hash map of recorded elements
    for i, n in enumerate(input_list):
        diff = target_sum - n # The difference between the sum and the current element
        if diff in record_hash:
            return [record_hash[diff], i]
        else:
            # If not in the hash map, add it into the map
            record_hash.update({n: i})

# -----------------------------------------------------------------------------------------------------------------------
# Problem 3
def q3():
    """
    q3() function implements to find the longest common prefix within the list of strings
    """
    # Input the list of strings
    words = input("Enter the words and separate them with ',': ")
    words = [x.strip() for x in words.split(',')]
    print("The longest common prefix is ", maxPrefix(words))

def maxPrefix(words):
    """
    Find the longest common prefix within the list of strings
    :param words: list of strings
    :return: the longest common prefix
    """
    # If no strings
    if len(words) == 0:
        return ""
    # If only one string
    if len(words) == 1:
        return words[0]
    # initialize the common prefix
    common_prefix = words[0]
    # Check each pair of strings
    for i in range(1, len(words)):
        common_prefix = commonPrefixTwoStrings(common_prefix, words[i])
    if common_prefix == "":
        return "NULL"
    else:
        return common_prefix

# Function to get common prefix of two strings
def commonPrefixTwoStrings(str1, str2):
    """
    Find the common prefix between two strings
    :param str1: 1st string
    :param str2: 2nd string
    :return: the common prefix
    """
    # Initial prefix
    common_prefix = ""
    # The minimum length of the strings
    n = min(len(str1), len(str2))
    # Check the characters if they are the same by indexes
    for i in range(n):
        if str1[i] == str2[i]:
            common_prefix += str1[i]
        else:
            break
    return common_prefix
# -----------------------------------------------------------------------------------------------------------------------

def main():
    q1()
    q2()
    q3()

if __name__ == '__main__':
    main()