# This is the exceptions lecture on modern python bootcamp from udemy

# Usage of a tuple and type() to raise multiple error types.  Feels clunky
def colorize(text, color):
    colors = ("cyan","yellow","red","blue","green","magenta")
    if type(text) is not str:
        raise TypeError('text must be a string')
    if type(color) is not str:
        raise TypeError('color must be a string')
    if color not in colors:
        raise ValueError('color must be cyan, yellow, red, blue, green or magenta')
    print(f"Printed {text} in {color}")


# colorize("hello", "red")
# colorize(34, "red")
# colorize("hello", 10)
# colorize("hello", "redd")


# try and except block to catch KeyError
d = {"name": "Ricky"}

def get(d, key):
    try:
        return d[key]
    except KeyError:
        return
#
# print(get(d, "name"))
# print(get(d, "city"))


# Really basic guessing game framework using While True to loop and except to catch valueerror
# while True:
#     try:
#         num = int(input("Please enter a number: "))
#     except ValueError:
#         print("That is not a number")
#     else:
#         print("Good job, you entered a number")
#         break
#     finally:
#         print("This will always run at the end")

# Catch individual errors
# def divide(a,b):
#     try:
#         result =  a/b
#     except ZeroDivisionError:
#         print("Division by zero is not possible")
#     except TypeError as err:
#         print("A or B must be int or float")
#         print(err)
#     else:
#         print(f"{a} divided by {b} is {result}")

# Catch multiple errors in one statement
def divide(a,b):
    try:
        result =  a/b
    except (ZeroDivisionError, TypeError) as err:
        print(f"Something went wrong: {err}")
    else:
        print(f"{a} divided by {b} is {result}")


print(divide(1,2))
print(divide(1,0))
print(divide(1,"a"))