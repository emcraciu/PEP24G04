# ex.1
lista = ['abc', 123, '1', 1]

for element in lista:
    print(f"Elementul {element} este de tipul {type(element)}")

numere_intregi = 0
numere_float = 0
siruri = 0

for element in lista:
    if isinstance(element, int):
        numere_intregi += 1
    elif isinstance(element, float):
        numere_float += 1
    elif isinstance(element, str):
        siruri += 1

print(f"Numarul de numere întregi: {numere_intregi}")
print(f"Numarul de numere float: {numere_float}")
print(f"Numarul de siruri de caractere: {siruri}")

# ex.2

sir = input("Introduceti un cuvant: ")
lista_caractere = list(sir.lower())
vocale = ['a', 'e', 'i', 'o', 'u']
numar_vocale = sum(1 for caracter in lista_caractere if caracter in vocale)

print(f"Vocale in cuvantul dvs: {numar_vocale}")


