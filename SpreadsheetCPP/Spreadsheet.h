#include "Cell.cpp"

class Spreadsheet {
public:
	Spreadsheet(int, int);
	Spreadsheet(const Spreadsheet&);
	~Spreadsheet();
public:
	void setCellAt(int, int, Cell);
	void setCellAt(int, int, const std::string&, Color);
	const Cell& getCellAt(int, int);
	void addRow(int);
	void removeRow(int);
	void addColumn(int);
	void removeColumn(int);
	void swapRows(int, int);
	void swapColumns(int, int);
	Spreadsheet& operator=(const Spreadsheet&);
private:
	Cell** m_cells;
	int m_rows;
	int m_columns;
};
