# This is the functions section from python modern boot camp
#

from random import random


def sing_happy_birthday(name):
    print("Happy bday to you!")
    print("Happy bday to you!")
    print(f"Happy bday dear {name}")
    print("Happy bday to you!")
# sing_happy_birthday('Sohail')


def square_of_7():
    return 7 ** 2
# print(square_of_7())


def flip_coin():
    if random() > 0.5:
        return 'heads'
    return 'tails'
# print(flip_coin())


def square(num):
    return num ** 2
# print(square(128))


# utilizes default value for power to return square
def square_by_power(num, power=2):
    """exponent(num, power) raises num to power.  Power defaults to 2"""
    return num ** power
# print(square_by_power(2,))
# print(square_by_power.__doc__)


def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Can not divide by zero"
# print(divide(1, 3))


def single_letter_count(s, l):
    return s.lower().count(l.lower())
# print(single_letter_count('Hello World', 'H'))


def multiple_letter_count(s):
    return {l: s.count(l) for l in s}
# print(multiple_letter_count('awesome'))


def list_manipulation(l, c, loc, value=0):
    if c == "remove" and loc == "end":
        return l.pop()
    elif c == "remove" and loc == "beginning":
        return l.pop(0)
    elif c == "add" and loc == "beginning":
        l.insert(0, value)
        return l
    elif c == "add" and loc == "end":
        l.append(value)
        return l
# print(list_manipulation([1,2,3], "remove", "end")) # 3
# print(list_manipulation([1,2,3], "remove", "beginning")) #  1
# print(list_manipulation([1,2,3], "add", "beginning", 20)) #  [20,1,2,3]
# print(list_manipulation([1,2,3], "add", "end", 30)) #  [1,2,3,30]


def is_palindrome(v):
    v = v.replace(" ", "")
    return v == v[::-1]


# print(is_palindrome('testing'))
# print(is_palindrome('tacocat'))
# print(is_palindrome('hannah'))
# print(is_palindrome('robert'))
# print(is_palindrome('amanaplanacanalpanama'))
#
def frequency(l, s):
    return l.count(s)


#
# print(frequency([1,2,3,4,4,4], 4)) # 3
# print(frequency([True, False, True, True], False)) # 1

def multiply_even_numbers(l):
    total = 1
    for x in l:
        if x % 2 == 0:
            total *= x
    return total


# print(multiply_even_numbers([2,3,4,5,6]))

# verbose method
# def compact(l):
#     r = []
#     for x in l:
#         if x:
#             r.append(x)
#     return r

# using list comprehension
def compact(l):
    return [val for val in l if val]


# print(compact([0,1,2,"",[], False, {}, None, "All done"]))

def isEven(num):
    return num % 2 == 0


# verbose method
# def partition(l, fn):
#     truthy = []
#     falsey = []
#     for val in l:
#         if fn(val):
#             truthy.append(val)
#         else:
#             falsey.append(val)
#     return [truthy, falsey]

# list comprehension method
def partition(list, fn):
    return [[val for val in list if fn(val)], [val for val in list if not fn(val)]]


# print(partition([1,2,3,4], isEven))

def fav_colors(**kwargs):
    print(kwargs)
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}")


# fav_colors(me='red',you='blue',him='red',her='blue',he='red',she='blue')

# parameters first, then *args, then default parameters, then **kwargs
def display_info(a, b, *args, instructor="Colt", **kwargs):
    return [a, b, args, instructor, kwargs]


# print(display_info(1, 2, 3, last_name="Steele", job="Instructor"))

def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
    print(total)


# Unpacking a list or tuple to a function using *list or *tuple
nums = [1,2,3,4,5,6]
# nums = (1, 2, 3, 4, 5, 6)


# sum_all_values(*nums)


# Unpacking a dictionatry to a function using **dictionary
def display_names(first, second):
    print(f"{first} says hello to {second}")


names = {"first": "Colt", "second": "Nancy"}


# display_names(**names)

# Unpacking a dict with additional kwargs
def add_and_multiply_numbers(a, b, c, **kwargs):
    print(a + b * c)
    print("OTHER STUFF...")
    print(kwargs)


data = dict(a=1, b=2, c=3, d=4, name="tony")


# add_and_multiply_numbers(**data, cat="blue")

# Dictionary unpacking exercise
def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get("first", 0) + kwargs.get("second", 0),
        'subtract': kwargs.get("first", 0) - kwargs.get("second", 0),
        'multiply': kwargs.get("first", 0) * kwargs.get("second", 0),
        'divide': kwargs.get("first", 0) / kwargs.get("second", 1)
    }

    is_float = kwargs.get("make_float", False)

    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = "{} {}".format(kwargs.get(
            'message', 'The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get(
            'message', 'The result is'), int(operation_value))
    return final


# print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))
# print(calculate(make_float=True, operation='divide', first=3.5, second=5))

# Lambda usage in a map to return a map object as a list
def decrement_list(l):
    return list(map(lambda x: x - 1, l))


# print(decrement_list([1,2,3]))

# filter() usage with lambda to remove negative numbers
def remove_negatives(l):
    return list(filter(lambda x: x >= 0, l))


# print(remove_negatives([-1,3,4,-99]))

# Return only strings when given a list
def is_all_strings(list1):
    return all(type(l) == str for l in list1)


# Return min and max of a list
def extremes(l):
    return (min(l), max(l))


# print(extremes([1,2,3,4,5]))
# print(extremes([99,25,-7,100]))
# print(extremes('alcatraz'))

# Return the largest number from 0
def max_magnitude(list1):
    return max(abs(num) for num in list1)


# print(max_magnitude([1,2,3,4,5,6,7,87,9,-99]))


# Returns the sum of only the even numbers
def sum_even_values(*args):
    num = (arg for arg in args if arg % 2 == 0)
    if num:
        return sum(num)
    else:
        return 0


# Simpler solution
def sum_even_values2(*args):
    return sum(arg for arg in args if arg % 2 == 0)


# print(sum_even_values2(1,2,3,4,5,6))
# print(sum_even_values2(4,2,1,10))
# print(sum_even_values2(1))

# Return sum of only floats in a passed in list
def sum_floats(*args):
    return sum(arg for arg in args if type(arg) == float)


# print(sum_floats(1.5, 2.4, 'awesome', [], 1))
# print(sum_floats(1,2,3,4,5))

# Usage of zip and map and lambda to join 3 lists and return an ordered list of student and highest/average grade
students = ['dan', 'don', 'jon']
midterms = [90, 80, 70]
finals = [70, 80, 90]

final_grades = dict(
    zip(
        students,
        map(
            lambda pair: max(pair),
            zip(midterms, finals)
        )
    )
)

avg_grades = dict(
    zip(
        students,
        map(
            lambda pair: ((pair[0] + pair[1]) / 2),
            zip(midterms, finals)
        )
    )
)


# print(final_grades)
# print(avg_grades)

# Use multiple joins and zip to interweave 2 strings
def interleave(s1, s2):
    return ''.join(''.join(x) for x in (zip(s1, s2)))


# print(interleave('hi', 'ha'))


# Returns the triple of numbers divisible by 4 from a list
def triple_and_filter(lst):
    return list(map(lambda y: y * 3, filter(lambda x: x % 4 == 0, lst)))


# print(triple_and_filter([1,2,3,4]))
# print(triple_and_filter([6,8,10,12]))

# Extract first and last name and return concatenated strings
def extract_full_name(dictlist):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), dictlist))


names = [{'first': 'Elie', 'last': 'Schoppik'},
         {'first': 'Colt', 'last': 'Steele'}]

# print(extract_full_name(names))  # ['Elie Schoppik', 'Colt Steele']
