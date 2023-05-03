import math
import random


lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
x = random.randint(lower, upper)

print("\n\tYou've only ", round(math.log(upper-lower+1,2)), "chances to guess!\n")

count = 0

while count<math.log(upper-lower+1,2):
    count+=1
    guess = int(input("Enter your guess: "))
    if x==guess:
        print("\n\tCongratulations! You guessed it in ", count, " guesses!")

        break
    elif guess<x:
        print("\n\tYour guess is too low!")
    elif guess>x:
        print("\n\tYour guess is too high!")


    
if count>=math.log(upper-lower+1,2):
    print("\n\tSorry, you ran out of guesses!")
    print("\n\tThe number was", x)