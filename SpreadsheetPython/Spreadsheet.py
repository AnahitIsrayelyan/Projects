import Cell


def check_for_setter(val):
    c = Cell.Cell()
    if type(val) == type(c):
        return "Cell"
    if type(val) == type("str"):
        return "String"


class Spreadsheet:
    def __init__(self, row: int, column: int):
        cell = Cell.Cell()
        if row <= 0 and column <= 0:
            raise ValueError("Number of rows and columns must be positive values")
        self.__cells = [[cell for _ in range(column)] for _ in range(row)]

    def set_cell_at(self, row: int, col: int, val):
        if row >= len(self.__cells) or col >= len(self.__cells[0]):
            raise ValueError("invalid argument")
        if check_for_setter(val) == "Cell":
            self.__cells[row][col] = val
        if check_for_setter(val) == "String":
            self.__cells[row][col].set_value(val)

    def get_cell_at(self, row: int, col: int):
        return self.__cells[row][col]

    def add_row(self, index: int):   # add below
        cell = Cell.Cell()
        new_row = [cell for _ in range(len(self.__cells[0]))]
        self.__cells.insert(index, new_row)

    def remove_row(self, row: int):      # row is index
        del self.__cells[row]

    def add_column(self, col: int):
        cell = Cell.Cell()
        for i in range(len(self.__cells[0])):
            self.__cells[i].insert(col, cell)

    def remove_column(self, col: int):
        for i in range(len(self.__cells)):
            del self.__cells[i][col]

    def swap_rows(self, r1: int, r2: int):
        self.__cells[r1], self.__cells[r2] = self.__cells[r2], self.__cells[r1]

    def swap_columns(self, c1: int, c2: int):
        for i in range(len(self.__cells)):
            self.__cells[i][c1], self.__cells[i][c2] = self.__cells[i][c2], self.__cells[i][c1]


# rotate, export
