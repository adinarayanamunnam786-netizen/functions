# 1. Sum of Digits
num = int(input("Enter a number: "))
temp = num
s = 0
while temp > 0:
    s += temp % 10
    temp //= 10
print("Sum of Digits =", s)

# 2. Reverse a Number
num = int(input("\nEnter a number: "))
temp = num
rev = 0
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
print("Reverse =", rev)

# 3. Count Digits
num = int(input("\nEnter a number: "))
count = len(str(num))
print("Number of Digits =", count)

# 4. Check Even or Odd
num = int(input("\nEnter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 5. Check Prime Number
num = int(input("\nEnter a number: "))
prime = True
if num < 2:
    prime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            prime = False
            break
if prime:
    print("Prime Number")
else:
    print("Not a Prime Number")

# 6. Factorial of a Number
num = int(input("\nEnter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial =", fact)

# 7. Factors of a Number
num = int(input("\nEnter a number: "))
print("Factors are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")

# 8. Check Palindrome Number
num = int(input("\n\nEnter a number: "))
temp = num
rev = 0
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
if rev == num:
    print("Palindrome")
else:
    print("Not a Palindrome")

# 9. Check Armstrong Number
num = int(input("\nEnter a number: "))
length = len(str(num))
temp = num
total = 0
while temp > 0:
    digit = temp % 10
    total += digit ** length
    temp //= 10
if total == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

# 10. Find GCD (HCF) of Two Numbers
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
while b != 0:
    a, b = b, a % b
print("GCD (HCF) =", a)