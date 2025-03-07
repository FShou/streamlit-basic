class Product:
    def __init__(self, name, price, stock = 1) -> None:
        self.name = name
        self.price = price
        self.stock = stock

    def increase_stock(self, amount):
        self.stock += amount

    def decrease_stock(self, amount):
        if self.stock - amount < 0 :
            self.stock = 0
            return
        self.stock -= amount

class Catalog:
    def __init__(self, name) -> None:
        self.name = name
        self.products: list[Product] = []

    def add_product(self, product: Product):
        self.products.append(product)

    def get_available_products(self):
        return [product for product in self.products if not product.stock == 0 ]

