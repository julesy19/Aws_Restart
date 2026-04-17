print("Bonjour  Mamadou ")
print("*" * 50)
print("Lab 114")
print("*" * 50)


print("*" * 50)
print("Exercice 1 : Utiliser la déclaration if")
print("*" * 50)

userReply = input("Do you need to ship a package? (Enter yes or no) ")
if userReply == "yes":
    print("We can help you ship that package!")
    
else:
    print("Please come back when you need to ship a package. Thank you.")


print("*" * 50)
print("Exercice 3 : Utiliser la déclaration elif")
print("*" * 50)


userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")



