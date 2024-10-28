word = input("Introduceti un cuvant fara majuscule: ")
first_letter = word[0]
repeat = 1
for letter in word[1:]:
    if letter == first_letter:
        repeat += 1
print(f'{first_letter} apare de {repeat} ori')

# folosind dictionare

word = input("Introduceti un cuvant fara majuscule: ")
repeat = {}
for letter in word:
    if letter in repeat:
        existing_repeat_count = repeat.get(letter)
        existing_repeat_count += 1
        repeat[letter] = existing_repeat_count
    else:
        repeat[letter] = 1
for letter, repeat in repeat.items():
    print(f"letter {letter} is repeated {repeat} times")
