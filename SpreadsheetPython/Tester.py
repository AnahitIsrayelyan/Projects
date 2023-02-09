import datetime
import Spreadsheet
import Cell


def tester_valid(cond, func_name, class_name):
    if cond:
        print(f"passed {func_name} for {class_name}")
    else:
        print(f"failed {func_name} for {class_name}")


""" tests for cell """


def test_cell_get_set_value():
    c = Cell.Cell()
    c.set_value("hel")
    tester_valid(c.get_value() == "hel", "get_value", "Cell")


def test_cell_get_set_color():
    c = Cell.Cell()
    c.set_color("white")
    tester_valid(c.get_color() == Cell.colors["white"], "get_color", "Cell")


def test_cell_value():
    c = Cell.Cell()
    c.set_value("-1")
    try:
        c.to_int()
    except:
        print("failed to_int for Cell, exception")
    else:
        if c.to_int() == -1:
            print("passed to_int for Cell")
        else:
            print("failed to_int for Cell")


    c.set_value("5.4")
    try:
        c.to_float()
    except:
        print("failed to_float for Cell, exception")
    else:
        if c.to_float() == 5.4:
            print("passed to_float for Cell")
        else:
            print("failed to_float for Cell")

    c.set_value("09/02/2023")
    try:
        c.to_date()
    except:
        print("failed to_date for Cell, exception")
    else:
        if str(c.to_date()) == "2023-02-09":
            print("passed to_date for Cell")
        else:
            print("failed to_date for Cell")


def test_cell_reset():
    c = Cell.Cell()
    c.set_value("hello")
    c.reset()
    tester_valid(c.get_value() == "", "reset", "Cell")


""" tests for spreadsheet """


def test_spreadsheet_set_get():
    c = Cell.Cell("hello")
    sp = Spreadsheet.Spreadsheet(2, 2)
    sp.set_cell_at(0, 0, c)
    sp.set_cell_at(1, 1, "hi")
    tester_valid(sp.get_cell_at(0, 0).get_value() == "hello", "get_cell_at(cell)", "Spreadsheet")
    tester_valid(sp.get_cell_at(1, 1).get_value() == "hi", "get_cell_at(str)", "Spreadsheet")


def test_spreadsheet_add_row():
    sp = Spreadsheet.Spreadsheet(2, 2)
    sp.set_cell_at(1, 1, "hi")
    sp.add_row(1)
    tester_valid(sp.get_cell_at(2, 1).get_value() == "hi", "add_row", "Spreadsheet")


def test_spreadsheet_remove_row():
    sp = Spreadsheet.Spreadsheet(3, 2)
    sp.set_cell_at(1, 0, "hi")
    sp.remove_row(1)
    tester_valid(sp.get_cell_at(1, 0).get_value() == "hi", "remove_row", "Spreadsheet")


def test_spreadsheet_add_column():
    sp = Spreadsheet.Spreadsheet(2, 2)
    sp.set_cell_at(1, 1, "hi")
    sp.add_column(1)
    tester_valid(sp.get_cell_at(1, 2).get_value() == "hi", "add_column", "Spreadsheet")


def test_spreadsheet_remove_column():
    sp = Spreadsheet.Spreadsheet(2, 3)
    sp.set_cell_at(1, 2, "hi")
    sp.remove_column(1)
    tester_valid(sp.get_cell_at(1, 1).get_value() == "hi", "remove_column", "Spreadsheet")


def test_spreadsheet_swap_rows():
    sp = Spreadsheet.Spreadsheet(2, 3)
    sp.set_cell_at(1, 2, "hi")
    sp.swap_rows(0, 1)
    tester_valid(sp.get_cell_at(0, 2).get_value() == "hi", "swap_rows", "Spreadsheet")


def test_spreadsheet_swap_columns():
    sp = Spreadsheet.Spreadsheet(2, 3)
    sp.set_cell_at(1, 2, "hi")
    sp.swap_columns(0, 2)
    tester_valid(sp.get_cell_at(1, 0).get_value() == "hi", "swap_columns", "Spreadsheet")


test_cell_get_set_value()
test_cell_get_set_color()
test_cell_value()
test_cell_reset()

test_spreadsheet_set_get()
test_spreadsheet_add_row()
test_spreadsheet_remove_row()
test_spreadsheet_add_column()
test_spreadsheet_remove_column()
test_spreadsheet_swap_rows()
test_spreadsheet_swap_columns()
