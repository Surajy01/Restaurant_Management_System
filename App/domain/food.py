class Food:
    def __init__(self, id, category, name, unit, stock, price):
        self.id=id
        self.category=category
        self.name=name
        self.unit=unit
        self.stock=stock
        self.price=price

    def dict(self):
        return {
            "id": self.id,
            "category": self.category,
            "name": self.name,
            "unit": self.unit,
            "stock": self.stock,
            "price": self.price
        }