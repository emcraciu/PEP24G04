Cappuccino = 4
Espresso = 3.5
while True:
    print("1. Cappuccino ... 4 lei")
    print("2. Espresso ... 3.5 lei")
    user_input = input("Selectati optiunea: ")
    bancnota = input("Introduceti bancnota: ")
    if user_input == "1" and bancnota == "5":
        price = f" {Cappuccino} lei"
        rest = int(bancnota) - 4

    elif user_input == "2":
        price = f" {Espresso} lei"
    else:
        break
    print(f"Vei primi restul de {rest} leu")
    print("Produsul se livreaza")
