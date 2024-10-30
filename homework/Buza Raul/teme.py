lista = ['abc', 123, '1', 1]
for obj in lista:
    print(type(obj))

obj_int = 0
obj_float = 0
obj_str= 0

for x in lista:
    if type(x) == int:
        obj_int  += 1
    elif type(x) == float:
        obj_float += 1
    elif type(x) == str:
        obj_str += 1
print('Numărul de întregi:',obj_int)
print('Numărul de float-uri:',obj_float)
print('Numărul de șiruri:', obj_str)






sir = input("Introduceti un cuvant: ")
lista = list(sir)

vocale = 'aeiouAEIOU'
numar_vocale = 0

for caracter in lista:
    if caracter in vocale:
        numar_vocale += 1

print('Vocale in cuvantul dvs:', numar_vocale)