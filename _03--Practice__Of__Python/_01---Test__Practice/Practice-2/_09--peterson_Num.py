# . Write a program to check given number is Peterson number or not.

import math

num = int(input("Enter a number: "))
temp = num
sum_fact = 0

while temp > 0:
    digit = temp % 10
    sum_fact += math.factorial(digit)
    temp = temp // 10

if sum_fact == num:
    print(f"{num} is a Peterson number.")
else:
    print(f"{num} is not a Peterson number.")
      