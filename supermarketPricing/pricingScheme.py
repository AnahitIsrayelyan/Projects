from myEnum import *


# derived classes are for further possible extension of the project
class PricingScheme(ABC):
    def __init__(self) -> None:
        super().__init__()


    def calculatePrice(self, unitPrice: float, quantity: float = 1):
        return unitPrice * quantity


class UnitPricingScheme(PricingScheme):
    def __init__(self) -> None:
        self._schemeType = SchemeType.UNIT


    def calculatePrice(self, unitPrice: float, quantity: float = 1):
        return super().calculatePrice(unitPrice, quantity)


class WeightPricingScheme(PricingScheme):
    def __init__(self) -> None:
        self._schemeType = SchemeType.WEIGHT


    def calculatePrice(self, unitPrice: float, quantity: float = 1):
        return super().calculatePrice(unitPrice, quantity)



    