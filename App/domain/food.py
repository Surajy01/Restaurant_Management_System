class Food:
    def __init__(self, id, category, name, food_type, unit, stock, price):
        self.id=id
        self.category=category
        self.name=name
        self.food_type=food_type
        self.unit=unit
        self.stock=stock
        self.price=price

    def dict(self):
        return {
            "id": self.id,
            "category": self.category,
            "name": self.name,
            "food_type": self.food_type,
            "unit": self.unit,
            "stock": self.stock,
            "price": self.price
        }