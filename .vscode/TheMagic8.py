import random 

secret_number=random.randint(1,10)

guess = 0

while guess != secret_number:
    guess = int(input("Guess the number (1,10)"))

    if guess == secret_number:
        print("You are a Wizard!")

    else:
        print("Oops, not today, sorcerer!")
 