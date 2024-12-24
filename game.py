print ("Welcome to Nova Number Guessing Version 2.1")
githubinfo = ("Go to my Github Repo called 'Nova-Number-Guessing' to view future events and updates")
print (githubinfo)
print ("Good Luck!")
endlog = ("Thank you for playing! Check my Git Repo for more!")

input("Press enter to begin playing")

import random

low = 1
high = 40
tries = 0
number = random.randint(low,high)

while True:
    guess = int(input(f"Enter your guess... It will be between ({low} - {high}):"))
    tries += 1

    if guess < number:
        print (f"{guess} is too little. Try again!")
    elif guess > number:
        print (f"{guess} is too much. Try again!")
    else:
        print (f"{guess} is correct! Good job!")

        print(f"This round took you {tries} tries to get it right")
        break

playagainlog = input ("This time, it will be harder! Press enter to defeat the final round!")

low = 1
high = 70
tries = 0
number = random.randint(low,high)

while True:
    guess = int(input(f"Enter your guess... It will be between ({low} - {high}):"))
    tries += 1

    if guess < number:
        print (f"{guess} is too little. Try again!")
    elif guess > number:
        print (f"{guess} is too much. Try again!")
    else:
        print (f"{guess} is correct! Good job!")

        print(f"This harder round took you {tries} tries to get it right")
        break

twoplaylog = input ("But wait... That's Not all!!! This time, it will be extremely tough! Press enter to win the extreme round!")

low = 1
high = 100
tries = 0
number = random.randint(low,high)

while True:
    guess = int(input(f"Enter your guess... It will be between ({low} - {high}):"))
    tries += 1

    if guess < number:
        print (f"{guess} is too little. Try again!")
    elif guess > number:
        print (f"{guess} is too much. Try again!")
    else:
        print (f"{guess} is correct! Good job!")

        print(f"This extreme round took you {tries} tries to get it right! Amazing!")
        break

print (endlog)
