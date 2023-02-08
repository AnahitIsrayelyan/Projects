#include "Spreadsheet.h"

Spreadsheet::Spreadsheet(int r, int c) {
	m_cells = new Cell*[r];
	for(int i = 0; i < r; ++i) {
		m_cells[i] = new Cell[c];
	}
	m_rows = r;                              //kept for dtor deletes' loop
	m_columns = c;
}

Spreadsheet::~Spreadsheet() {
	for(int i = 0; i < m_rows; ++i) {
		delete[] m_cells[i];
	}
	delete[] m_cells;
}

Spreadsheet::Spreadsheet(const Spreadsheet& src) : m_rows(src.m_rows), m_columns(src.m_columns) {
	m_cells = new Cell*[m_rows];
	for (int i = 0; i < m_rows; i++) {
		m_cells[i] = new Cell[m_columns];
		for (int j = 0; j < m_columns; j++) {
			m_cells[i][j] = src.m_cells[i][j];
		}
	}
}

Spreadsheet& Spreadsheet::operator=(const Spreadsheet& src) {
	if(this == &src) {
		return *this;
	}
	for(int i = 0; i < m_rows; ++i) {
		delete[] m_cells[i];
	}
	delete[] m_cells;

    m_rows = src.m_rows;
    m_columns = src.m_columns;

    m_cells = new Cell*[m_rows];
    for(int i = 0; i < m_rows; ++i) {
		m_cells[i] = new Cell[m_columns];
		for(int j = 0; j < m_columns; ++j) {
			m_cells[i][j] = src.m_cells[i][j];
		}
	}
	return *this;
}

void Spreadsheet::setCellAt(int r, int c, Cell cl) {
	if(r >= m_rows or c >= m_columns or m_rows < 0 or m_columns < 0) {
		throw std::out_of_range("Out of range indexes");
	}
	this->m_cells[r][c] = cl;
}

void Spreadsheet::setCellAt(int r, int c, const std::string& str, Color clr = Color::white) {
	if(r >= m_rows or c >= m_columns or m_rows < 0 or m_columns < 0) {
		throw std::out_of_range("Out of range indexes");
	}
	this->m_cells[r][c].setValue(str);
	this->m_cells[r][c].setColor(clr);
}

const Cell& Spreadsheet::getCellAt(int r, int c) {
	return *(&(this->m_cells[r][c]));
}

void Spreadsheet::addRow(int r) {
	if(r >= m_rows or r < 0) {
		throw std::invalid_argument("Out of range argument");
	}
	Cell** temp = new Cell*[m_rows + 1];
    for(int i = 0; i < m_rows + 1; ++i) {
    	temp[i] = new Cell[m_columns];
	}

	for(int i = 0; i < m_rows; ++i) {
		for(int j = 0; j < m_columns; ++j) {
			if(i <= r) {
				temp[i][j] = m_cells[i][j];
			} else {
				temp[i+1][j] = m_cells[i][j];
			}
		}
	}
	for (int i = 0; i < m_rows; i++) {
		delete[] m_cells[i];
	}
	delete[] m_cells;
	m_cells = temp;
	++m_rows;
}

void Spreadsheet::removeRow(int r) {
	if(r >= m_rows or r < 0) {
		throw std::invalid_argument("out of range index");
	}
	for(int i = r; i < (m_rows - 1); ++i) {
		for(int j = 0; j < m_columns; ++j) {
			m_cells[i][j] = m_cells[i+1][j];
		}
	}
	delete[] m_cells[m_rows - 1];
	m_cells[m_rows - 1] = nullptr;
	--m_rows;
}

void Spreadsheet::addColumn(int c) {
	if(c >= m_columns or c < 0) {
		throw std::invalid_argument("Out of range argument");
	}
	Cell** temp = new Cell*[m_rows];
	for(int i = 0; i < m_rows; ++i) {
		temp[i] = new Cell[m_columns+1];
    }

	for(int i = 0; i < m_rows; ++i) {
        for(int j = 0; j <= c; ++j) {
            temp[i][j] = m_cells[i][j];
        }
        for(int j = c+1; j < m_columns; ++j) {
            temp[i][j + 1] = m_cells[i][j];
        }
    }
    for(int i = 0; i < m_rows; ++i) {
        delete[] m_cells[i];
    }
    delete[] m_cells;
    m_cells = temp;
    ++m_columns;
}

void Spreadsheet::removeColumn(int c) {
	if(c >= m_columns or c < 0) {
		throw std::invalid_argument("out of range index");
	}
	Cell** temp = new Cell*[m_rows];
    for(int i = 0; i < m_rows; ++i) {
    	temp[i] = new Cell[m_columns - 1];
    }

	for(int i = 0; i < m_rows; ++i) {
        for(int j = 0; j < m_columns; ++j) {
        	if(j < c) {
            	temp[i][j] = m_cells[i][j];
            } else if(j > c) {
                temp[i][j-1] = m_cells[i][j];
            }
        }
    }
	for(int i = 0; i < m_rows; ++i) {
    delete[] m_cells[i];
    }
    delete[] m_cells;
    m_cells = temp;
    --m_columns;
}
	
void Spreadsheet::swapRows(int r1, int r2) {
	if(r1 < 0 or r2 < 0 or r1 >= m_rows or r2 >= m_rows) {
		throw std::invalid_argument("out of range argument");
	}
	for(int i = 0; i < m_columns; ++i) {
		Cell tmp = std::move(m_cells[r1][i]);
		m_cells[r1][i] = std::move(m_cells[r2][i]);
		m_cells[r2][i] = std::move(tmp);
	}
}

void Spreadsheet::swapColumns(int c1, int c2) {
	if(c1 < 0 or c2 < 0 or c1 >= m_columns or c2 >= m_columns) {
		throw std::invalid_argument("out of range argument");
	}
	for(int i = 0; i < m_rows; ++i) {
		Cell tmp = std::move(m_cells[i][c1]);
		m_cells[i][c1] = std::move(m_cells[i][c2]);
		m_cells[i][c2] = std::move(tmp);
	}
}
