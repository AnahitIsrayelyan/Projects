
// էս ֆայլը գրելիս անծանոթ շատ բան կար, շատ բաներ դեռ նայելով եմ գրել, 
// սմարթ փոյնթրներ պարունակող կոդերը նորից պետքա անցնեմ



#include "Spreadsheet.h"


void Spreadsheet::setIntCell(int row, int col, int value) {
	m_cells[std::make_pair(row, col)] = std::make_unique<IntCell>(value);
}

void Spreadsheet::setDoubleCell(int row, int col, double value) {
	m_cells[std::make_pair(row, col)] = std::make_unique<DoubleCell>(value);
}

void Spreadsheet::setStringCell(int row, int col, const std::string& value) {
	m_cells[std::make_pair(row, col)] = std::make_unique<StringCell>(value);
}

void Spreadsheet::setDateCell(int row, int col, const Date& value) {
	m_cells[std::make_pair(row, col)] = std::make_unique<DateCell>(value);
}

Cell& Spreadsheet::getCell(int row, int col) {
	return *m_cells.at(std::make_pair(row, col));
}

void Spreadsheet::removeRow(int row) {
	auto it = m_cells.begin();
	while (it != m_cells.end()) {
		if (it->first.first == row) {
			it = m_cells.erase(it);
		} else {
			++it;
		}
	}
}

void Spreadsheet::removeColumn(int col) {
	auto it = m_cells.begin();
	while (it != m_cells.end()) {
		if (it->first.second == col) {
			it = m_cells.erase(it);
		} else {
			++it;
		}
	}
}

void Spreadsheet::swapRows(int row1, int row2){
	for(auto& [key, cell]: m_cells) {
		if(key.first == row1) {
			auto it = m_cells.find(std::make_pair(row2, key.second));
			if(it != m_cells.end()) {
				std::swap(cell, it->second);
			} else {
				m_cells[std::make_pair(row2, key.second)] = std::move(cell);
				m_cells.erase(key);
			}
		}
	}
}

void Spreadsheet::swapColumns(int col1, int col2) {
	for(auto& [key, cell]: m_cells) {
		if(key.second == col1) {
			auto it = m_cells.find(std::make_pair(key.first, col2));
			if(it != m_cells.end()) {
				std::swap(cell, it->second);
			} else {
				m_cells[std::make_pair(key.first, col2)] = std::move(cell);
				m_cells.erase(key);
			}
		}
	}
}
