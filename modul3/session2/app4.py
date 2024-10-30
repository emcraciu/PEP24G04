parola_corecta = "7788"
counter = 0
while counter < 3:
    parola_introdusa = input("Introduceti parola: ")
    if parola_introdusa == parola_corecta:
        print("Acces permis.")
        break
    else:
        print("Parola gresita. Mai incercati.")
        counter += 1

["Masa", 5, "Scaun", 4.5, [5, 6, 7], 8]
