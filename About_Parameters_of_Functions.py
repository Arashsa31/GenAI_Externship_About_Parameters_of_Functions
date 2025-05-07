#Task 1 - Writing Functions
def greet_user(name):
    print(f"Hello, {name}! Welcome aboard.")
greet_user("Alice")

def add_numbers(a, b):
    return a + b
a = 5
b = 10
result = add_numbers(a,b)
print(f"The sum of {a} and {b} is {result}.")
print()

#Task 2 - Using Default Parameters
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")
describe_pet("Buddy")
describe_pet("Whiskers", "cat")
print()

#Task 3 - Functions with Variable Arguments
def make_sandwich(*args):
    print("Making a sandwich with the following ingredients:")
    for ingredients in args:
        print(f"- {ingredients}")
make_sandwich("Lettuce", "Tomato", "Cheese")
print()

#Task 4 - Understanding Recursion
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)
a = 5
b = 6
factorial_result = factorial(a)
fibonacci_result = fibonacci(b)
print(f"Factorial of {a} is {factorial_result}. The {b}th Fibonacci number is {fibonacci_result}.")
print()