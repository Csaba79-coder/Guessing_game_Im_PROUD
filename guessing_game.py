
# guessing game is guessing numbers by user input, if guessed number of the user and the number guessed by the computer is the same you guessed it! you are codecool :)

import math # unused import
import random
a = [] # an empty list
a.append(random.randint(1, 99)) # appending a random number to the list - number from 1 till 99 SO including the end point!
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99)) # making append 10 times --> so we have 10 random numbers (at the end) in the list between 1 to 99
print(a)
for i in range(10): # a loop that iterates throug the list (so on the 10 elements - that are numbers) - so we can guess 10 different number 
    g = int(input("Enter an integer from 1 to 99: ")) # there is a user input (for guessing a number from 1 to 99) must be an integer
    while a[i] != g: # because of the loop 10 times we make the guess, and this while loop says if the guessed number and the list element is the same or not
        if g < a[i]: # it says if guess number is smaller than the number in the list
            print("guess is low") # that the number is low what we guessed
            g = int(input("Enter an integer from 1 to 99: ")) # and asking for new number
        elif g > a[i]: # if guessed number is bigger than the element of the list
            print("guess is high") # it says the number that we guessed is high
            g = int(input("Enter an integer from 1 to 99: ")) # asking again for a new guess - input
        else: # as it is an endless while loop only we can stop the loop with break! BUT only in case if input is the same number as the element of the list we have to have guessing
            break # it stops the loop 
    print("you guessed it!") # it says it was a correct guess (the loop goes arund 10 times, so we need to guess 10 different number after eachother!)

b = [] # it is a new list! but the numbers are between 1 till 49 - the code makes the same! we have to guess for all the 10 elements in the list to finish the game 
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
print(b)
for i in range(10):
    g = int(input("Enter an integer from 1 to 49: "))
    while b[i] != g:
        if g < b[i]:
            print("guess is low")
            g = int(input("Enter an integer from 1 to 49: "))
        elif g > b[i]:
            print("guess is high")
            g = int(input("Enter an integer from 1 to 49: "))
        else:
            break
    print("you guessed it!") # so all together we guessed 20 numbers! to finish the game!
