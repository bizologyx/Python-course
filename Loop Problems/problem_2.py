# 2. The Factorial Calculator
# Ask the user for a positive integer. Use a while loop to calculate the factorial of that number (e.g., if the user enters 5, the output should be 120 because 5 \times 4 \times 3 \times 2 \times 1 = 120).

num = int(input("Enter a number: "))
new_num = num 
f = 1 
while(num > 0):
    f = f * num 
    num = num - 1 
print(f"F of {new_num} is {f} ")