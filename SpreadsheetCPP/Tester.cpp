#include <iostream>
#include "Spreadsheet.cpp"


void testCell() {
	Cell c1 = Cell("hello", Color::red);

	Cell c = Cell();
	c.setValue("23");
	c.setColor(Color::red);

	if(c.getColor() == Color::red) {
		std::cout << "ok set/get color" << std::endl;
	} else {
		std::cout << "! color" << std::endl;
	}
	if(c.getValue() == "23") {
		std::cout << "ok for string" << std::endl;
	} else {
		std::cout << "! string" << std::endl;
	}
	c.reset();
	if(c.getValue() == "") {
		std::cout << "ok. reseted" << std::endl;
	} else {
		std::cout << "not reseted" << std::endl;
	}
}

void testCellValueInt() {
	Cell c = Cell("23", Color::red);
	if(c.toInt() == 23) {
		std::cout << "ok for int 23" << std::endl;
	} else {
		std::cout << "! int 23" << std::endl;	
	}
	c.setValue("023");
	if(c.toInt() == 23) {
		std::cout << "ok for int 023" << std::endl;
	} else {
		std::cout << "! int 023" << std::endl;	
	}
	c.setValue("-23");
	if(c.toInt() == -23) {
		std::cout << "ok for int -23" << std::endl;
	} else {
		std::cout << "! int -23" << std::endl;	
	}
	c.setValue("+23");
	if(c.toInt() == 23) {
		std::cout << "ok for int +23" << std::endl;
	} else {
		std::cout << "! int +23" << std::endl;	
	}
}

void testCellValueDouble() {
	Cell c = Cell("23.4");
	if(c.toDouble() == 23.4) {
		std::cout << "ok for double 23.4" << std::endl;
	} else {
		std::cout << "! double 23.4" << std::endl;
	}
	c.setValue("023.4");
	if(c.toDouble() == 23.4) {
		std::cout << "ok for double 023.4" << std::endl;
	} else {
		std::cout << "! double 023.4" << std::endl;	
	}
	c.setValue("-23.4");
	if(c.toDouble() == -23.4) {
		std::cout << "ok for double -23.4" << std::endl;
	} else {
		std::cout << "! double -23.4" << std::endl;	
	}
	c.setValue("+23.4");
	if(c.toDouble() == 23.4) {
		std::cout << "ok for double +23.4" << std::endl;
	} else {
		std::cout << "! double +23" << std::endl;	
	}
}

void testCellValueDate() {
	Cell c = Cell("08/02/2023");
	if(c.toDate() == Date(8, 02, 2023)) {
		std::cout << "ok for date 1" << std::endl;
	} else {
		std::cout << "! date 1" << std::endl;
	}
}

void testSpreadsheetSetGet() {
	Spreadsheet sp = Spreadsheet(3, 4);
	Cell cl = Cell("23");
	sp.setCellAt(0, 0, "hello");
	sp.setCellAt(0, 1, cl);
	if(sp.getCellAt(0, 1) == cl) {
		std::cout << "ok set/get" << std::endl;
	} else {
		std::cout << "! get/set" << std::endl;
	}
	try {
		sp.setCellAt(10, 10, "world");
	} catch(...) {
		std::cout << "ok out of range setCellAt 1" << std::endl;
	}
	try {
		sp.setCellAt(10, 10, cl);
	} catch(...) {
		std::cout << "ok out of range setCellAt 2" << std::endl;
	}
}

void testSpreadsheetAddRemove() {
	Spreadsheet sp = Spreadsheet(3, 4);  //size is 3x4
	sp.addRow(1);                        //size is 4x4, new row is sp[2][i]
	try {
		sp.setCellAt(3, 3, "hello");
	} catch(...) {
		std::cout << "! failed addRow" << std::endl;
	}
	sp.addRow(3);                        //size is 5x4, new row is sp[4][i]
	try { 
		sp.addRow(10); 
	} catch(...) {
		std::cout << "ok for out of range addRow" << std::endl;
	}
	sp.removeRow(0);                     //size is 4x4, removed row is sp[0][i]
	try { 
		sp.removeRow(10); 
	} catch(...) {
		std::cout << "ok for out of range removeRow" << std::endl;
	}
	sp.addColumn(1);                     //size is 4x3, removed column is sp[i][1]
	try { 
		sp.removeColumn(10); 
	} catch(...) {
		std::cout << "ok for out of range removeColumn" << std::endl;
	}
}

void testSpreadsheetSwap() {
	Spreadsheet sp = Spreadsheet(3, 4);   //3 and 4 are not indexes
	Cell cl = Cell("hello");
	sp.setCellAt(0, 0, cl);
	sp.swapRows(0, 2);                    //0 and 2 are indexes
	if(sp.getCellAt(2, 0) == cl) {
		std::cout << "ok swapRows" << std::endl;
	} else {
		std::cout << "! swapRows" << std::endl;
	}
	sp.swapColumns(0, 1);
	if(sp.getCellAt(2, 1) == cl) {
		std::cout << "ok swapColumns" << std::endl;
	} else {
		std::cout << "! swapColumns" << std::endl;
	}
}


int main() {
	testCell();
	testCellValueInt();
	testCellValueDouble();
	testCellValueDate();

	testSpreadsheetSetGet();
	testSpreadsheetAddRemove();
	testSpreadsheetSwap();

	return 0;
}


