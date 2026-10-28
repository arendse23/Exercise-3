# basic function definition and calling
def greet ():
    print ('Hello, World!')

#call the function
greet ()

# function with parameters
def personalized_greeting (name):
    print('Hello, Zena')

# call the function
personalized_greeting('Hello,Zena')

# function with return value
def square(number):
    return number * number 
result = square(5)
print(result)

# funtion with multiple parameters and return 
def rectangle_area(length, width):
    return length * width
result = rectangle_area(4,5)
print(result)

# using a function as an argument

def apply_operation (func, number):
    return func(number)

print(apply_operation(square, 5))

def double(number):
    return number * 2
print(double(5))
print(double(4))
def appy_operation(func, number):
 print(apply_operation(double,7))
print(apply_operation(square,3))