import random

print("Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start the Game!")

low = int(input("Enter the Lower Bound: ")) #lowest number
high = int(input("Enter the Upper Bound: ")) #highest number 

print(f"\nYou have 7 chances to guess the number between {low} and {high}.")

num = random.randint(low, high) 
tc = 7                        # total chances allowed
gc = 0                        # guesses counting

while gc < tc:
    gc += 1
    guess = int(input('Enter your Guessing Number: '))

    if guess == num:
        print(f'Correct! The number is {num}. You guessed it in {gc} attempts.')
        break

    elif gc >= tc and guess != num:
        print(f'Sorry! The number was {num}. Better luck next time.')

    elif guess > num:
        print('Too high! Try a lower number.') #if the gussing number is higher

    elif guess < num:
        print('Too low! Try a higher number.') # if the gudding number is lower
print("Thank you")