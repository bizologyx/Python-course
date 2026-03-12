# 5. Vowel Counter
# Take a string input from the user. Use a for loop to iterate through the string and count how many vowels (a, e, i, o, u) are in the text.

sen = input("Enter a sentence: ")
v = "aeiouAEIOU"
count = 0
for i in sen:
    if i in v:
        count= count + 1
print(f'Total Vowels is: {count}')