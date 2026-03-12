# 3. Star Pyramid
# Ask the user for the number of rows. Use a loop to print a right-angled triangle of stars (*). For example, if the input is 3, it should print:
# *
# **
# ***

r = int(input("Enter number for R: "))
for i in range(1,r+1):
    print('*'*i)


# *
# **
# ***
# ****
# *****