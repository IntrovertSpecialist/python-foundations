import random
def game(a,b,guess):
    while True:
        if a > b:
            print("Lower!")
            a = int(input("Enter your new guess: "))
            guess += 1
        elif a < b:
            print("Higher!")
            a = int(input("Enter your new guess: "))
            guess += 1
        elif a == b:
            print(f"Good job! The number was {a}")
            print(f"You took {guess} guesses to figure it out.")
            break
print("Welcome to guessing game!\nThe system will randomly generate a number and you will have to guess it based on the provided hints.\nPlease enter 1 for easy mode, 2 for medium and 3 for hard mode.")
guess = 1
while True:
    start = int(input(""))
    if start < 1 or start > 3:
        print("Invalid entry, try again")
    else:
        break
if start == 1:
    print("Easy Mode(From 0 to 100):")
    comp = random.randint(0,100)
    num = int(input("Enter your guess: "))
    game(num,comp,guess)
elif start == 2:
    print("Medium Mode(From 0 to 1000)")
    comp = random.randint(0,1000)
    num = int(input("Enter your guess: "))
    game(num,comp,guess)
elif start == 3:
    print("Hard Mode(From 0 to 10000)")
    comp = random.randint(0,10000)
    num = int(input("Enter your guess: "))
    game(num,comp,guess)




