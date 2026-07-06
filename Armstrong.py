# Armstrong Number Program

num = int(input("Enter a number: "))

length = len(str(num))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** length)
    temp = temp // 10

if sum == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")