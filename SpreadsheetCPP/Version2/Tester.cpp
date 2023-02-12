#include <iostream>
#include "Spreadsheet.cpp"

void testIntCell() {
	IntCell obj = IntCell(5);

	if(obj.getStringValue() == "5") {
		std::cout << "passed IntCell.getStringValue" << std::endl;
	} else {
		std::cout << "failed IntCell.getStringValue" << std::endl;
	}

	obj.setValue(6);
	if(obj.getStringValue() == "6") {
		std::cout << "passed IntCell.setValue" << std::endl;
	} else {
		std::cout << "failed IntCell.setValue" << std::endl;
	}

	obj.setColor(Color::blue);
	if(obj.getColor() == Color::blue) {
		std::cout << "passed IntCell.set/get color" << std::endl;
	} else {
		std::cout << "failed IntCell.set.get color" << std::endl;
	}

	obj.reset();
	if(obj.getStringValue() == "0") {
		std::cout << "passed IntCell.reset" << std::endl;
	} else {
		std::cout << "failed IntCell.reset" << std::endl;
	}
}


void testDoubleCell() {
	DoubleCell obj = DoubleCell(5.4);

	if(obj.getStringValue() == "5.4") {
		std::cout << "passed DoubleCell.getStringValue" << std::endl;
	} else {
		std::cout << "failed DoubleCell.getStringValue" << std::endl;
	}

	obj.setValue(6.5);
	if(obj.getStringValue() == "6.5") {
		std::cout << "passed DoubleCell.setValue" << std::endl;
	} else {
		std::cout << "failed DoubleCell.setValue" << std::endl;
	}

	obj.setColor(Color::blue);
	if(obj.getColor() == Color::blue) {
		std::cout << "passed DoubleCell.set/get color" << std::endl;
	} else {
		std::cout << "failed DoubleCell.set.get color" << std::endl;
	}

	obj.reset();
	if(obj.getValue() == 0.0) {
		std::cout << "passed DoubleCell.reset" << std::endl;
	} else {
		std::cout << "failed DoubleCell.reset" << std::endl;
	}
}

void testStringCell() {
	StringCell obj = StringCell("hello");

	if(obj.getStringValue() == "hello") {
		std::cout << "passed StringCell.getStringValue" << std::endl;
	} else {
		std::cout << "failed StringCell.getStringValue" << std::endl;
	}

	obj.setValue("world");
	if(obj.getStringValue() == "world") {
		std::cout << "passed StringCell.setValue" << std::endl;
	} else {
		std::cout << "failed StringCell.setValue" << std::endl;
	}

	obj.setColor(Color::blue);
	if(obj.getColor() == Color::blue) {
		std::cout << "passed StringCell.set/get color" << std::endl;
	} else {
		std::cout << "failed Stringell.set.get color" << std::endl;
	}

	obj.reset();
	if(obj.getStringValue() == "") {
		std::cout << "passed StringCell.reset" << std::endl;
	} else {
		std::cout << "failed StringCell.reset" << std::endl;
	}
}

void testDateCell() {
	DateCell obj = DateCell(22, 12, 1999);

	if(obj.getStringValue() == "22/12/1999") {
		std::cout << "passed DateCell.getStringValue" << std::endl;
	} else {
		std::cout << "failed DateCell.getStringValue" << std::endl;
	}

	Date obj2 = Date(12, 2, 2023);
	obj.setValue(obj2);
	if(obj.getStringValue() == "12/2/2023") {
		std::cout << "passed DateCell.setValue" << std::endl;
	} else {
		std::cout << "failed DateCell.setValue" << std::endl;
	}

	obj.setColor(Color::blue);
	if(obj.getColor() == Color::blue) {
		std::cout << "passed DateCell.set/get color" << std::endl;
	} else {
		std::cout << "failed DateCell.set.get color" << std::endl;
	}

	DateCell obj3 = Date(0, 0, 0);
	obj.reset();
	if(obj.getStringValue() == obj3.getStringValue()) {
		std::cout << "passed DateCell.reset" << std::endl;
	} else {
		std::cout << "failed DateCell.reset" << std::endl;
	}
}


void testSpreadsheetSetGet() {
	Spreadsheet sp = Spreadsheet();
	sp.setIntCell(0, 0, 5);
	if(sp.getCell(0, 0).getStringValue() == "5") {
		std::cout << "passed setIntCell" << std::endl;
	} else {
		std::cout << "failed setIntCell" << std::endl;
	}

	sp.setDoubleCell(0, 0, 5.5);
	if(sp.getCell(0, 0).getStringValue() == "5.5") {
		std::cout << "passed setDoubleCell" << std::endl;
	} else {
		std::cout << "failed setDoubleCell" << std::endl;
	}

	sp.setStringCell(0, 0, "hello");
	if(sp.getCell(0, 0).getStringValue() == "hello") {
		std::cout << "passed setStringCell" << std::endl;
	} else {
		std::cout << "failed setStringCell" << std::endl;
	}

	Date dt = Date(12, 2, 2023);
	sp.setDateCell(0, 0, dt);
	if(sp.getCell(0, 0).getStringValue() == "12/2/2023") {
		std::cout << "passed setDateCell" << std::endl;
	} else {
		std::cout << "failed setDateCell" << std::endl;
	}

	sp.setIntCell(0, 1, 5);
	sp.setIntCell(1, 2, 10);
	sp.setIntCell(3, 4, 22);
	sp.removeRow(1);
	try {
		sp.getCell(1, 2).getStringValue();
	} catch (...) {
		std::cout << "passed removeRow" << std::endl;
	}

	sp.removeColumn(4);
	try {
		sp.getCell(3, 4).getStringValue();
	} catch (...) {
		std::cout << "passed removeColumn" << std::endl;
	}

	// implement and test swaps
}


int main() {
	testIntCell();
	testDoubleCell();
	testStringCell();
	testDateCell();
	testSpreadsheetSetGet();
}
