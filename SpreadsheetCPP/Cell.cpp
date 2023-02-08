#include "Cell.h"
#include <cctype>


Cell::Cell(const std::string& str = "", Color clr = Color::white) : m_value{str}, m_color{clr} {}

void Cell::setValue(const std::string& str) {
	this->m_value = str;
}

std::string Cell::getValue() const {
	return this->m_value;
}

void Cell::setColor(Color clr) {
	this->m_color = clr;
}

Color Cell::getColor() const { 
	return this->m_color;      
}

int Cell::toInt() {
	if(!this->isInt()) {
		throw std::invalid_argument("Invalid convertion from string to int");
	} 
	int num = 0;
	int start = 0;
	int end = m_value.length() - 1;
	if(m_value[0] == '-' || m_value[0] == '+') {
		start = 1;
	}
	for(int i = start; i <= end; ++i) {
		num = num * 10 + (m_value[i] - '0');
	}
	if(m_value[0] == '-') {
		num *= -1;
	}
	return num;
}

double Cell::toDouble() {
	if(!this->isDouble()) {
		throw std::invalid_argument("Invalid convertion from string to double");
	} 
	int afterDot = 0;                             //count digits after dot
	double num = 0;
	int start = 0;
	int end = m_value.length() - 1;
	if(m_value[0] == '-' || m_value[0] == '+') {
		start = 1;
	}
	for(int i = start; i <= end; ++i) {
		if(m_value[i] != '.') {
			num = num * 10 + (m_value[i] - '0');
		}
		if(m_value[i] == '.' or afterDot) {
			++afterDot;                           //digits after dot + 1
		}
	}
	for(int i = 1; i < afterDot; ++i) {           //to decimal
		num /= 10; 
	}
	if(m_value[0] == '-') {
		num *= -1;
	}
	return num;
}

Date Cell::toDate() {
	if(!this->isDate()) {
		throw std::invalid_argument("Invalid convertion from string to Date");
	}
	Date dt = Date(0, 0, 0);
	dt.setDay((m_value[0] - '0') * 10 + (m_value[1] - '0'));       // hard to read, hardcoded
	dt.setMonth((m_value[3] - '0') * 10 + (m_value[4] - '0')); 
	dt.setYear((m_value[6] - '0') * 1000 + 
				(m_value[7] - '0') * 100 + 
				(m_value[8] - '0') * 10 + 
				(m_value[9] - '0'));
	return dt;
}

bool Cell::isDate() {                                         // bad implementation
	return (isdigit(m_value[0]) and isdigit(m_value[1]) and
	m_value[2] == '/' and 
	isdigit(m_value[3]) and isdigit(m_value[4]) and
	m_value[5] == '/' and 
	isdigit(m_value[6]) and isdigit(m_value[7]) and isdigit(m_value[8]) and isdigit(m_value[9]));
}

void Cell::reset() {
	this->m_color = Color::white;
	this->m_value = "";
}

bool Cell::isInt() {
	if(m_value.empty()) {
		return false;
	}
	int start = 0;
	int end = m_value.length() - 1;
	if(m_value[0] == '-' || m_value[0] == '+') {
		start = 1;
	}
	for(int i = start; i <= end; ++i) {
		if(!isdigit(m_value[i])) {
			return false;
		}
	}
	return true;
}

bool Cell::isDouble() {
	if(m_value.empty()) {
		return false;
	}
	int dotCount = 0;
	int start = 0;
	int end = m_value.length() - 1;
	if(m_value[0] == '-' || m_value[0] == '+') {
		start = 1;
	}
	for(int i = start; i <= end; ++i) {
		if(!isdigit(m_value[i]) and m_value[i] != '.') {
			return false;
		}
		if(m_value[i] == '.') {
			++dotCount;
		}
	}
	if(dotCount > 1) {
		return false;
	}
	return true;
}

bool operator==(const Cell& src, const Cell& ptr) {
	return (src.getValue() == ptr.getValue() and
			src.getColor() == ptr.getColor());
}
