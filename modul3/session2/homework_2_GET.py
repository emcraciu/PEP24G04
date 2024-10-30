shop1 = {"apples": 10, "plums": 13, "peach": 14, "banana": 10}
shop2 = {"apples": 11, "plums": 14, "peach": 12}
shop3 = {"apples": 12, "plums": 11, "peach": 15}
cart = {"apples": 3, "plums": 4, "peach": 5}
shops = {"magazin1": shop1, "magazin2": shop2, "magazin3": shop3}
price_per_shop = {}
for product, quantity in cart.items():
    # print(product, quantity)
    for shop_name, shop_data in shops.items():
        # print(shop_name, shop_data)
        cost_per_product = shop_data[product] * quantity
        # print(shop_data[product] * quantity)
        price_per_shop.update({shop_name: price_per_shop.get(shop_name, 0) + cost_per_product})
        print(price_per_shop)

# modificarea la .get permite un cod simplicaficat, prin renuntarea la if/else statements. Alt motiv?????
# cred ca permite sa fie mai vizibil textul, prin faptul ca va cauta direct dupa (shop_name), ca si value.
# Acel 0 nu sunt sigur dar cred ca vrea sa fie ceva gen "daca nu am value la shop_name, folosesc 0 ?????

# nu inteleg de ce a trebuit sa renunt la ".update" din price_per_shop.update

