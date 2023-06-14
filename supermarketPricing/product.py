from pricingScheme import *
from discountScheme import *

class Product:
    def __init__(self, name: str, unitPrice: float, pricingScheme: PricingScheme, discountScheme: DiscountScheme = None) -> None:
        self._name = name
        self._unitPrice = unitPrice 
        self._pricingScheme = pricingScheme
        self._discountScheme = discountScheme


    def __repr__(self) -> str:
        return f"name: {self._name}, price: {self._unitPrice}"


    def getPrice(self, quantity):
        price = self._pricingScheme.calculatePrice(self._unitPrice)
        return self._discountScheme.applyDiscount(price, quantity) if self._discountScheme else (price * quantity)


    def changePricingScheme(self, pricingScheme: PricingScheme):
        self._pricingScheme = pricingScheme


    def changeDiscountScheme(self, discountScheme: DiscountScheme):
        self._discountScheme = discountScheme


    def deleteDiscount(self):
        self._discountScheme = None

