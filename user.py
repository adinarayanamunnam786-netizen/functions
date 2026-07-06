

# 1. Function to add two numbers
def add(a, b):
    return a + b

print("1. Add:", add(10, 20))


# 2. Function to find the square of a number
def square(n):
    return n * n

print("2. Square:", square(6))


# 3. Function to check whether a number is even or odd
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"

print("3. Even/Odd:", check_even_odd(7))


# 4. Function to find the largest of three numbers
def largest(a, b, c):
    return max(a, b, c)

print("4. Largest:", largest(10, 25, 15))


# 5. Function to calculate the factorial of a number
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print("5. Factorial:", factorial(5))


# 6. Function to reverse a string
def reverse_string(text):
    return text[::-1]

print("6. Reverse String:", reverse_string("Python"))


# 7. Function to count vowels in a string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

print("7. Vowel Count:", count_vowels("Programming"))


# 8. Function to check whether a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("8. Is Prime:", is_prime(13))


# 9. Function to find the sum of elements in a list
def list_sum(numbers):
    return sum(numbers)

print("9. List Sum:", list_sum([10, 20, 30, 40]))


# 10. Function to check whether a string is a palindrome
def is_palindrome(text):
    return text == text[::-1]

print("10. Is Palindrome:", is_palindrome("madam"))