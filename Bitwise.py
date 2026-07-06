# Bitwise Operators in Python

a = 10      # 1010
b = 10      # 1010 (same value)

print("a =", a)
print("b =", b)

# 1. Bitwise AND (&)
print("a & b =", a & b)

# 2. Bitwise OR (|)
print("a | b =", a | b)

# 3. Bitwise XOR (^)
print("a ^ b =", a ^ b)   # Same values -> Output = 0

# 4. Bitwise NOT (~)
print("~a =", ~a)

# 5. Left Shift (<<)
print("a << 2 =", a << 2)

# 6. Right Shift (>>)
print("a >> 2 =", a >> 2)

# Check Even or Odd using Bitwise AND
num = int(input("\nEnter a number: "))

if num & 1:
    print(num, "is Odd")
else:
    print(num, "is Even")

# Examples
print("\nExamples:")
print("10 ^ 10 =", 10 ^ 10)   # 0
print("10 & 10 =", 10 & 10)   # 10
print("10 | 10 =", 10 | 10)   # 10
print("1 & 1 =", 1 & 1)       # 1 (Odd)
print("2 & 1 =", 2 & 1)       # 0 (Even)