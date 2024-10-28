# Parola unui PC este 7788. Creați un script care sa simuleze accesul la PC.
# Introduceti parola: 7677
# Parola gresita. Mai incercati.
# Introduceti parola: 3432
# Parola gresita. Mai incercati.
# Introduceti parola: 7788
# Acces permis.
# Process finished with exit code 0


"""parola_corect = "7788"
counter = 0
while counter > 3:
    parola_introdusa = input("Introduceti parola: ")
    if parola_introdusa == parola_corecta:
        print("Acces permis")
        break
    else:
        print("Parola gresita. Mai incercati.")
        counter +=1"""
from itertools import count

# ------------------------------------------------------------------------------------------

# 5. Creați o lista obiecte = [“Masa”
# , 5,
# “Scaun”
# , 4.5, [5,6,7],8]. Parcurgeți lista de obiecte și
# afișați tipul fiecăruia. Challenge: Afișați tipul obiectelor în felul următor:
# Tipul obiectului Masa este str
# Tipul obiectului 5 este int

"""lista_obiecte = ["Masa", 5, "Scaun", 4.5, [5,6,7], 8]
for item in lista_obiecte:
    print(f"Tipul obiectului {item} este {type(item).__name__}")
    if type(item) == list:
        for i in item:
            print(f"Tipul obiectului {i} este {type(i).__name__}")"""

# ------------------------------------------------------------------------------------------

# 6. Luați ca input de la utilizator un cuvant si afisati numarul ocurentei primei litere din
# cuvant.
# Exemplu: Introduceti un cuvant (fara majuscule): rabdare
# r apare de 2 ori.

"""cuvant = input("introduceti un cuvant: ")
litera_1 = cuvant [0]
reperate_litera_1 = cuvant.count(litera_1)
print(f"{litera_1} se repeta de {reperate_litera_1} ori")"""

"""word = input("Introduceti cuvant: ")
first_letter = word [0]
repeat = 1
for letter in word[1:]:
    if letter == first_letter:
        repeat += 1
print(f"{first_letter} se repeta de {repeat} ori")"""

"""word = input("Introduceti cuvant: ")
repeat = {} # se creeaza un dictionar gol
for letter in word:
    if letter in repeat:
        print("letter is present: ", letter)
        existing_repeat_count = repeat.get(letter)
        existing_repeat_count +=1
        repeat[letter] = existing_repeat_count
    else:
        repeat[letter] = 1
print(repeat)
for letter, repeat in repeat.items():
    print(f"letter {letter} is repetead {repeat} times")"""

# Pentru acest exercițiu aveți începutul codului care cere input de la utilizator cu un șir
# separat prin virgula și îl împarte într-o listă.

# lista = input("Introduceti lista de taskuri: ")
# lista_taskuri = lista.split(",")
# print(lista taskuri)

"""lista = input("introduceti lista de taskuri: ")
lista_taskuri = lista.split(",")
lista_fara_dubluri = set(lista_taskuri)
print(lista_fara_dubluri)"""


