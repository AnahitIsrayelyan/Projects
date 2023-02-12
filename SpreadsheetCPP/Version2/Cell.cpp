#include "Cell.h"
#include <cctype>
#include <sstream>

void Cell::setColor(Color clr) {
	m_color = clr;
}

Color Cell::getColor() const { 
	return m_color;      
}

IntCell::IntCell(int val) : m_value(val) {}

void IntCell::setValue(int val) {
	m_value = val;
}

int IntCell::getValue() const {
	return m_value;
}

void IntCell::reset() {
	m_value = 0;
}

std::string IntCell::getStringValue() {
	return std::to_string(m_value);
}

DoubleCell::DoubleCell(double val) : m_value(val) {}

void DoubleCell::setValue(double val) {
	m_value = val;
}

double DoubleCell::getValue() const {
	return m_value;
}

void DoubleCell::reset() {
	m_value = 0.0;
}

std::string DoubleCell::getStringValue() {
	std::ostringstream os;
    os << m_value;
    std::string str = os.str();
	return str;
}

StringCell::StringCell(const std::string& val) : m_value(val) {}

void StringCell::setValue(const std::string& val) {
	m_value = val;
}

void StringCell::reset() {
	m_value = "";
}

std::string StringCell::getStringValue() {
	return m_value;
}

DateCell::DateCell(const Date& val) : m_value(val) {}

DateCell::DateCell(int d, int m, int y) {
	m_value = Date(d, m, y);
}

void DateCell::setValue(const Date& val) {
	m_value = val;
}

void DateCell::reset() {
	m_value = Date(0, 0, 0);
}

std::string DateCell::getStringValue() {
	std::ostringstream os;
    os << m_value.getDay() << "/" << m_value.getMonth() << "/" << m_value.getYear();
	return os.str();
}



