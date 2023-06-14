from supermarket import *


if __name__ == "__main__":
    pr1 = UnitPricingScheme()
    pr2 = WeightPricingScheme()

    disc1 = PercentageDiscount(20)
    disc2 = BuyXForOnePrice(2)

    p1 = Product("copybook", 500, pr1, disc2)
    p2 = Product("copybook1", 600, pr2, disc2)
    p3 = Product("copybook2", 700, pr1, disc1)
    p4 = Product("copybook3", 800, pr2, disc1)

    s = Supermarket()
    s.addProduct(p1, 4)
    s.addProduct(p2, 4)
    s.addProduct(p3, 4)
    s.addProduct(p4, 4)

    for i in s._inventory:
        print(i, s._inventory[i])

    s.removeProduct(p1)
    s.sellProduct(p2)

    for i in s._inventory:
        print(i, s._inventory[i])

    print(s.calculateTotalInventoryValue())
