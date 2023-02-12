class Date {
public:
    Date() = default;
	Date(int, int, int);
public:
	void setYear(int);
	void setMonth(int);
	void setDay(int);
	int getYear() const;
	int getMonth() const;
	int getDay() const;
    void displayDate();
private:
	int m_year {};
	int m_month {};
	int m_day {};
};