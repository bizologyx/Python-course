import random
comp = random.randint(1,10)
user = int(input("Enter any number B/W (1-10): "))
if (user == comp):
    print(f"You Won, Computer = {comp}")
else:
    print(f"You Lose, Computer = {comp}")