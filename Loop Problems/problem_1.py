# 1. The Divisibility Filter
# Write a program that iterates through numbers from 1 to 50. For each number, if it is divisible by 3, print "Fizz"; if it is divisible by 5, print "Buzz"; and if it is divisible by both, print "FizzBuzz."

for i in range(1,51):
    if (i % 3 == 0) and (i % 5 == 0):
        print(f"FizzBuzz and the number is {i}.")
    elif (i % 3 == 0):
        print(f"Fizz and the number is {i}.")
    elif (i % 5 == 0):
        print(f"Buzz and the number is {i}.")
    else:
        print(i)