print("Bonjour  Mamadou ")
print("*" * 50)
print("Lab 115")
print("*" * 50)



print("*" * 50)
print("Exercice 1 : Utiliser la déclaration while")
print("*" * 50)

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")


import random

number = random.randint(1,10)

isGuessRight = False

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
        
        
        
print("Count to 10!")

for x in range (0, 11):
    print(x)