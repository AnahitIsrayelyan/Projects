#include "Cell.cpp"
#include <map>
#include <memory>


class Spreadsheet {
public:
	Spreadsheet() = default;
	void setIntCell(int row, int col, int value);
	void setDoubleCell(int row, int col, double value);
	void setStringCell(int row, int col, const std::string& value);
	void setDateCell(int row, int col, const Date& value);
	Cell& getCell(int row, int col);
	void removeRow(int row);
	void removeColumn(int col);
	void swapRows(int row1, int row2);
	void swapColumns(int col1, int col2);
private:
	std::map<std::pair<int, int>, std::unique_ptr<Cell>> m_cells;
};

