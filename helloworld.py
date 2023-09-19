print("Hello, World!")

integer_var = 10
float_var = 3.14
string_var = "Hello, World!"
boolean_var = True
list_var = [1, 2, 3]
tuple_var = (4, 5, 6)
dictionary_var = {'key': 'value'}
set_var = {7, 8, 9}

print(f"Type of integer_var: {type(integer_var)}, value: {integer_var}")
print(f"Type of float_var: {type(float_var)}, value: {float_var}")
print(f"Type of string_var: {type(string_var)}, value: {string_var}")
print(f"Type of boolean_var: {type(boolean_var)}, value: {boolean_var}")
print(f"Type of list_var: {type(list_var)}, value: {list_var}")
print(f"Type of tuple_var: {type(tuple_var)}, value: {tuple_var}")
print(f"Type of dictionary_var: {type(dictionary_var)}, value: {dictionary_var}")
print(f"Type of set_var: {type(set_var)}, value: {set_var}")

numbers = list(range(1, 11))
numbers.append(20)
numbers.remove(3)
numbers.sort()

print(numbers)

numbers = [10, 20, 30, 40]
sum_numbers = sum(numbers)
average = sum_numbers / len(numbers)

print(f"Sum: {sum_numbers}, Average: {average}")

def reverse_string(input_string):
    return input_string[::-1]

input_string = "Python"
reversed_string = reverse_string(input_string)
print(reversed_string)


def count_vowels(input_string):
    vowels = "AEIOUaeiou"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

input_string = "Hello"
num_vowels = count_vowels(input_string)
print(f"Number of vowels: {num_vowels}")


def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

input_number = 13
if is_prime(input_number):
    print(f"{input_number} is a prime number.")
else:
    print(f"{input_number} is not a prime number.")


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

input_number = 5
result = factorial(input_number)
print(f"Factorial of {input_number} is {result}.")

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

input_n = 5
fib_sequence = fibonacci(input_n)
print(fib_sequence)

squares = [x**2 for x in range(1, 11)]
print(squares)


