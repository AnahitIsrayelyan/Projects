#include "Date.h"
#include <stdexcept>

Date::Date(int d, int m, int y) {
    if((d <= 0) or (d > 31)) {          
        throw std::invalid_argument("Invalid argument for day");
    }
    if((m <= 0) or (m > 12)) {
        throw std::invalid_argument("Invalid argument for month");
    }
	m_day = d;
    m_month = m;
    m_year = y;
}

void Date::setYear(int y) {
	this->m_year = y;
}

void Date::setMonth(int m) {
    if((m <= 0) or (m > 12)) {
        throw std::invalid_argument("Invalid argument for month");
    }
	this->m_month = m;
}

void Date::setDay(int d) {
    if((d <= 0) or (d > 31)) {                  // condition could be better
        throw std::invalid_argument("Invalid argument for day");
    }
	this->m_day = d;
}

int Date::getYear() const {
	return this->m_year;
}

int Date::getMonth() const {
	return this->m_month;
}

int Date::getDay() const {
	return this->m_day;
}

bool operator==(const Date& src, const Date& ptr) {
	return (src.getYear() == ptr.getYear() and 
	src.getMonth() == ptr.getMonth() and
	src.getDay() == ptr.getDay());
}

void Date::displayDate() {
    std::cout << "DD/MM/YYYY: " << m_day << '/' << m_month << '/' << m_year;
}
