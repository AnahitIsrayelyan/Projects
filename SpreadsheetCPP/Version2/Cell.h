#include <string>
#include "Date.cpp"        

enum class Color {white, red, green, blue};

class Cell {
public:
	void setColor(Color);
	Color getColor() const;
	virtual std::string getStringValue() = 0;
	virtual void reset() = 0;
private:
	Color m_color;
};

class IntCell: public Cell {
public:
	IntCell(int);
public:
	void setValue(int);
	int getValue() const;
	std::string getStringValue() override;
	void reset() override;
private:
	int m_value;
};

class DoubleCell: public Cell {
public:
	DoubleCell(double);
public:
	void setValue(double);
	double getValue() const;
	std::string getStringValue() override;
	void reset() override;
private:
	double m_value;
};

class StringCell: public Cell {
public:
	StringCell(const std::string&);
public:
	void setValue(const std::string&);
	std::string& getValue() const;
	std::string getStringValue() override;
	virtual void reset() override;
private:
	std::string m_value;
};

class DateCell: public Cell {
public:
	DateCell(const Date&);
	DateCell(int, int, int);
public:
	void setValue(const Date&);
	std::string getStringValue() override;
	virtual void reset() override;
private:
	Date m_value;
};
