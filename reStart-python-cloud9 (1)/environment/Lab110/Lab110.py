print("Bonjour  Mamadou ")
print("*" * 50)
print("Lab 110")
print("*" * 50)


myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))



print("*" * 50)
print("Exercice 2 : Utiliser la concaténation des chaînes")
print("*" * 50)

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

print("*" * 50)
print("Exercice 3 : Utiliser des chaînes d'entrée")
print("*" * 50)

name = input("What is your name? ")
print(name)


print("*" * 50)
print("Exercice 4 : Formater des chaînes de sortie")
print("*" * 50)


color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

print("{}, you like a {} {}!".format(name,color,animal))