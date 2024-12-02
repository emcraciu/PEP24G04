# ex1

lista = ['abc', 123, '1', 1]

tipuri_elemente = [type(element) for element in lista]

numere_intregi = sum(1 for tip in tipuri_elemente if tip == int)
numere_float = sum(1 for tip in tipuri_elemente if tip == float)
siruri = sum(1 for tip in tipuri_elemente if tip == str)

print(f"Tipuri elemente: {tipuri_elemente}\nNumere intregi: {numere_intregi}\nNumere float: {numere_float}"
      f"\nSiruri de caractere: {siruri}")

# ex2

sir = input("Introduce-ti un sir: ")

lista_caractere = list(sir.lower())

vocale = 'aeiou'

numar_vocale = sum(1 for caracter in lista_caractere if caracter in vocale)

print(f"Vocale in cuvantul dvs.: {numar_vocale}")
