from collections import defaultdict
from product import Product
from pricingScheme import *
from discountScheme import *


# Disclaimer! There is no functionality for payments and related processes
class Supermarket:
    def __init__(self) -> None:
        self._inventory = defaultdict(float)


    def addProduct(self, product: Product, quantity: float = 1):
        if quantity >= 0:
            self._inventory[product] += quantity
        else:
            raise Exception("Invalid argument.")


    def removeProduct(self, product: Product, quantity: float = 1):
        if self._inventory[product] >= quantity:
            self._inventory[product] -= quantity
            if self._inventory[product] == 0:
                del self._inventory[product]
        else:
            raise Exception(f"{self._inventory[product]} items are left!")


    # this is the same as removeProducts, in case of project extension they may differ
    def sellProduct(self, product: Product, quantity: float = 1):
        if self._inventory[product] >= quantity:
            self._inventory[product] -= quantity
            if self._inventory[product] == 0:
                del self._inventory[product]
        else:
            raise Exception(f"{self._inventory[product]} items are left!")


    def checkStock(self, product: Product) -> bool:
        return product in self._inventory


    def calculateTotalInventoryValue(self) -> float:
        value = 0
        for prod in self._inventory:
            value += prod.getPrice(self._inventory[prod])
        return value
    




