from myEnum import *


class DiscountScheme(ABC):
    def __init__(self) -> None:
        super().__init__()


    @abstractmethod
    def applyDiscount(self, unitPrice, quantity):
        pass


# ordinary percentage discount
class PercentageDiscount(DiscountScheme):
    def __init__(self, percentage: InterruptedError) -> None:
        super().__init__()
        self._percentage = abs(percentage)


    def applyDiscount(self, unitPrice, quantity) -> float:
        if self._percentage == 0:
            return (unitPrice * quantity)
        return ((quantity * unitPrice) * (1 - self._percentage / 100))


# buy 3 pay for 1
class BuyXForOnePrice(DiscountScheme):
    def __init__(self, xquantity: float) -> None:
        super().__init__()
        self._xquantity = xquantity


    def applyDiscount(self, unitPrice, quantity) -> float:
        return ((quantity // self._xquantity) + (quantity % self._xquantity)) * unitPrice


# buy 4 items and get 20% discount
class XUnitsYDiscount(DiscountScheme):
    def __init__(self, items, discount) -> None:
        super().__init__()
        self._items = items
        self._discount = discount


    def applyDiscount(self, unitprice, quantity):
        return ((quantity // self._items)*self._items*(unitprice*(1-self._discount/100)) + (quantity % self._items)*unitprice)
    
