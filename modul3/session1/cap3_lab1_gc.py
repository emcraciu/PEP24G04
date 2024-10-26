# ex4

parola_corecta = "7788"

while True:
    parola_introdusa = input("Introduceti parola: ")

    if parola_introdusa == parola_corecta:
        print("Acces permis.")
        break
    else:
        print("Parola gresita. Mai incercați.")


# ex5

obiecte = ["Masa", 5, "Scaun", 4.5, [5,6,7], 8]

for obiect in obiecte:
    print(f"Tipul obiectului {obiect} este {type(obiect).__name__}")


# ex6

cuvant = input("Introducet i un cuvânt (fara majuscule): ")

prima_litera = cuvant[0]
numar_aparitii = cuvant.count(prima_litera)

print(f"{prima_litera} apare de {numar_aparitii} ori.")


# ex7

lista = input("Introduceti lista de taskuri, separate prin virgula: ")
lista_taskuri = lista.split(",")

lista_taskuri = [task.strip() for task in lista_taskuri]

lista_fara_dubluri = []
for task in lista_taskuri:
    if task not in lista_fara_dubluri:
        lista_fara_dubluri.append(task)

print("Lista fara dubluri:", lista_fara_dubluri)





