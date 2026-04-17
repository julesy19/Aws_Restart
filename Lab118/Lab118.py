print("Bonjour  Mamadou ")
print("*" * 50)
print("Lab 118")
print("*" * 50)



print("*" * 50)
print("Exercice 1 : Préparation de l'analyse de l'insuline avec Python")
print("Python pour automatiser")
print("*" * 50)


import re

with open("preproinsulin_seq_clean.txt") as f:
    data = f.read()

# Nettoyage
clean = re.sub(r'[^a-zA-Z]', '', data).lower()

print("Séquence nettoyée :", clean)
print("Longueur :", len(clean))

# Découpage
lsinsulin = clean[0:24]
binsulin = clean[24:54]
cinsulin = clean[54:89]
ainsulin = clean[89:110]

print("\nLS:", lsinsulin, len(lsinsulin))
print("B :", binsulin, len(binsulin))
print("C :", cinsulin, len(cinsulin))
print("A :", ainsulin, len(ainsulin))