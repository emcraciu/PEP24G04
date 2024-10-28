word = input("Introduceti un cuvant fara majuscule: ")
first_letter = word[0]
repeat = 1
for letter in word[1:]:
    if letter == first_letter:
        repeat += 1
print(f'{first_letter} apare de {repeat} ori')
