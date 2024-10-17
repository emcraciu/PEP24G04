# Exercitiu 1
# Se cere calcularea ariei unui triunghi folosind forma de mai jos,
# cerand parametrii de la utilizator

# a. Cereți input de la utilizator cu baza triunghiului și înălțimea acestuia. Asigurati-va
# ca utilizatorul știe ce trebuie sa introduca, și stocati valorile cerute într-o variabila.
# b. Creați o variabila care sa reprezinte rezultatul calculului.
# c. Afișați tipul de data a variabilei rezultate
# d. Afișați rezultatul funcției pe ecran.
"""
b = input("Introduceti valoarea bazei: ")
h = input("Introduceti valoarea inaltimii: ")

result = 0.5 * int(b) * int(h)

print(result)
print()"""

# ----------------------------------------------------------------------------------------------------------------
# Parola unui calculator este 7710. Se cere input de la utilizator cu un număr.
# Afișați comparatia intre aceste doua numere.
# Daca este True, înseamnă ca utilizatorul a ghicit parola.

"""parola = 7710
user_input = int(input("Introduceti o valoare: "))
result = user_input == parola
print("Corect", result)"""

# ----------------------------------------------------------------------------------------------------------------
# Se va cere input de la utilizator cu 2 numere. Se calculeaza:
# a. Media numerelor
# b. Impartirea numerelor in ordinea introdusa de catre utilizator (rezultatul trebuie sa fie număr întreg)
# c. Primul număr la puterea celui de-al doilea număr.

nr1 = input("Introduceti valoarea primului numar: ")
nr2 = input("Introduceti valoarea pentru al doilea numar: ")

# a
average = (int(nr1) + int(nr2)) / 2
print(average)

# b
divide = int(nr1) / int(nr2)
print(divide)

# c
nr3 = int(input("Introduceti valoarea numarului 3: "))
nr4 = int(input("Introduceti valoarea numarului 4: "))

punct_c = nr3 ** nr4
print(f"{nr1} la puterea {nr2} este: {punct_c}")

# ----------------------------------------------------------------------------------------------------------------

# Se cere input de la utilizator cu venit net pe luna. Din acesta, calculati regula 50/30/20:
# - 50% din venit acordat necesităților (cumparaturi, intretinere, chirie, etc)
# - 30% din venit acordat scopurilor recreative
# - 20% din venit acordat datoriilor și economiilor

venit_net = float(input("Venitul lunar este de: "))
# venit_net = int(input("Venitul lunar este de: "))

ron = "RON"
necesitati = venit_net * 0.5
recreative = venit_net * 0.3
economii =  venit_net * 0.2

print(f"Din venit lunar de {venit_net} {ron} aveti nevoie de urmatoarele sume: ")
print(f"{necesitati} {ron} pentru necesitati uzuale")
print(f"{recreative} {ron} pentru scopuri recreative")
print(f"{economii} {ron} pentru economii")