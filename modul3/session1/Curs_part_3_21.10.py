# while loop

# while True:
#     number = input("give number: ")
#     print(f"Number is {number}")

# while int(input("Give number: ")) < 100:
#     print("Nr is too small: ")

"""str1 = "Hello"
# H E L L O
# 0 1 2 3 4
value = True
index = 0
while value:
    letter = str1[index]
    index += 1
    print(letter)
    if letter == 'e':
        break
    if index <= len(str1):
        value = False

print("Done")"""

# --------------------------------------
Cappuccino = 4
Espresso = 3.5
while True:
    print("1. Cappuccino ... 4 lei")
    print("2. Espresso ... 3.5 lei")
    user_input = input("Selectati optiunea 1 sau 2: ")
    bancnota = input("Introduceti bancnota: ")
    if user_input == "1" and bancnota == "5":
        price = f" {Cappuccino} lei"
        rest = int(bancnota) - Cappuccino
    elif user_input == "1" and bancnota == "10":
        price = f" {Cappuccino} lei"
        rest = int(bancnota) - Cappuccino
    elif user_input == "2" and bancnota =="5":
        price = f" {Espresso} lei"
        rest = int(bancnota) - Espresso
    elif user_input == "2" and bancnota =="10":
        price = f" {Espresso} lei"
        rest = int(bancnota) - Espresso

    else:
        print("Invalid")
        print(f"Ti se returneaza bancnota {bancnota}")
        continue

    print(f"Vei primi restul de {rest} lei")
    print("Produsul se livreaza")

# ------------------------------------------------------------------------------------

"""str1 = "Hello"
index = 0
while True:
    letter = str1[index]
    index += 1

    if letter == "l":
        continue
    print(letter)
    if index >= len(str1):
        break"""