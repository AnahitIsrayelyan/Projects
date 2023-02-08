#include <string>

enum class Color {white, red, green, blue};

class Date {
public:
	Date(int, int, int);
	void setYear(int);
	void setMonth(int);
	void setDay(int);
	int getYear() const;
	int getMonth() const;
	int getDay() const;
private:
	int m_year;
	int m_month;
	int m_day;
};

class Cell {
public:
	Cell(const std::string&, Color);     
public:
	void setValue(const std::string&);
	std::string getValue() const;
	int toInt();
	double toDouble();
	Date toDate();
	void reset();
	void setColor(Color);
	Color getColor() const;
private:
	bool isInt();
	bool isDouble();
	bool isDate();
private: 
	std::string m_value;
	Color m_color;
};
