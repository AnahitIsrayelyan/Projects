import datetime


colors = {"white": 0, "red": 1, "green": 2, "blue": 3}


class Cell:
    def __init__(self, value: str = "", color=colors["white"]):
        self.__value = str(value)
        self.__color = color

    def set_value(self, value: str):
        self.__value = value

    def set_color(self, color: str):
        self.__color = colors[color]

    def get_value(self):
        return self.__value

    def get_color(self):
        return self.__color

    def to_int(self):                                                     # don't we raise an exception???
        return int(self.__value)

    def to_float(self):
        return float(self.__value)

    def to_date(self):
        return datetime.datetime.strptime(self.__value, "%d/%m/%Y").date()

    def reset(self):
        self.__value = ""
