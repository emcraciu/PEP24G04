#1
lista=['abc', 123, '1', 1]

#a
for i in lista:
    print(type(i))

#b
nr_intreg= 0
nr_float=0
nr_str=0
for i in lista:
    if type(i) == int:
        nr_intreg = nr_intreg + 1

    if type(i) == float:
            nr_float += 1

    if type(i) == str:
            nr_str+=1

print(f"Sunt {nr_intreg} numere intregi, {nr_float} numere float si {nr_str} string-uri")

#2
nr_vocale=0
cuvant=input("Introduceti un cuvant: ")
lista=list(cuvant)

print(lista)
for i in lista:
    if i=='a' or i== 'e' or i=='i' or i=='o' or i=='u' or i=='A' or i== 'E' or i=='I' or i=='O' or i=='U':
        nr_vocale=nr_vocale+1
print(f"Numarul vocalelor din cuvant este {nr_vocale}")










