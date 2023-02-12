#include <string>
#include "Date.cpp"        // must be header file, not appropriate includes

enum class Color {white, red, green, blue};

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
