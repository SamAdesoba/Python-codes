class ShoppingCart:

    def __init__(self, basket: list, amount: int):
        self.basket_length = 3
        self.basket = basket
        self.amount = amount

    def get_length(self):
        self.basket_length = len(self.basket)
        if self.basket_length <= 3:
            return self.basket_length
        raise ValueError("Items should not be more than three")

    def add(self, item: str):
        if self.basket_length > 3:
            index = 0
            while index < self.basket_length-3:
                self.basket.remove(self.basket[index])
                self.basket.append(item)
        self.basket.append(item)

    def get_item(self, item_index: int):
        return self.basket[item_index]

