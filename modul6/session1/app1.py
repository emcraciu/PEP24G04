class Product:

    def __init__(self):
        self.name, self.price, self.stock = input("Give (name, price, stock) for product:").split(',')

    def __repr__(self):
        return (f"{self.__class__.__name__}: ({self.name},{self.price},{self.stock})")

    def __str__(self):
        return (f"Nume: {self.name} \n"
                f"Pret: {self.price} \n"
                f"Stoc: {self.stock} \n"
                f"{40 * '-'}")


class Category:

    def __init__(self, name: str):
        self.category_name = name
        self.products = []

    def add_product(self):
        # product = input("give product:")
        product = Product()
        self.products.append(product)


class Shop:

    def run(self):
        while True:
            # code here

