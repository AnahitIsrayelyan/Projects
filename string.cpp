#include <iostream>
#include <utility>

class String {
private:
	size_t m_size;
	size_t m_capacity;
	char* m_buffer;
private:
	int my_length(const char*);
	void realoc(size_t);
public:
	String();
	String(const char*);
	String(const String&);
	String(String&&);
	String& operator=(String&&);
	~String();
	const char* c_str() const;
	char& at(size_t);
	const char& front();
	const char& back();
	void push_back(char);
	void pop_back();
	String& erase(size_t, size_t);
	void clear();
	String& insert(size_t, const char*);
	String& append(size_t, char);
	String& append(size_t, const char*);
	bool empty();
	bool compare(const String&);
	bool starts_with(char);
	bool starts_with(const char*);
	bool ends_with(char);
	bool ends_with(const char*);
	bool contains(char);
	bool contains(const char*);
	int find(char);
	int find(const char*);
	String& substr(size_t, size_t);
	int copy(char*, int, int);
	void resize(int, char);
	size_t size() const;
	size_t capacity() const;
	void shrink_to_fit();
	void swap(String&);
	String& operator=(const String&);
	String& operator+=(char);
	String& operator+=(const char*);
	String& operator+=(const String&);
	char& operator[](size_t);
	friend bool operator==(String&, String&);
	friend bool operator!=(String&, String&);
	friend bool operator>(String&, String&);
	friend bool operator<(String&, String&);
	friend bool operator>=(String&, String&);
	friend bool operator<=(String&, String&);
	friend std::ostream& operator<<(std::ostream&, const String&);     //why friend
};


String::String() :
	m_size {0},
	m_capacity {0},
	m_buffer {nullptr}
{
}

String::String(const char* src) : m_size {0}, m_capacity {0}, m_buffer {nullptr}
{
	if(src) {
		m_size = my_length(src);
		m_capacity = m_size + 1;
		m_buffer = new char[m_capacity];
		for(int i = 0; i < m_size; ++i) {
			m_buffer[i] = src[i];
		}
		m_buffer[m_size] = '\0';
	}
}

String::String(const String& src) {
	m_size = src.m_size;
	m_capacity = src.m_capacity;
	m_buffer = new char[m_capacity];       //new in ctor
	for(int i = 0; i < m_size; ++i) {
		m_buffer[i] = src.m_buffer[i];
	}	
}

String::String(String&& src) {
	m_size = std::exchange(src.m_size, 0);
	m_capacity = std::exchange(src.m_capacity, 0);
	m_buffer = std::exchange(src.m_buffer, nullptr);
}

String& String::operator=(String&& src) {
	if(this == &src) {
		return *this;
	}
	delete[] m_buffer;
	m_size = std::exchange(src.m_size, 0);
	m_capacity = std::exchange(src.m_capacity, 0);
	m_buffer = std::exchange(src.m_buffer, nullptr);
	return *this;
}

String::~String() {
	if(m_buffer) {
		delete[] m_buffer;
		m_buffer = nullptr;
		m_size = 0;
		m_capacity = 0;
	}
}

int String::my_length(const char* src) {
	if(!src) {
		return -1;
	}
	int num = 0;
	while(src[num]) {
		++num;
	}
	return num;
}

void String::realoc(size_t size) {
	m_capacity += size;
	char* tmp = new char[m_capacity];
	int i = 0;
	while(m_buffer[i]) {
		tmp[i] = m_buffer[i];
		++i;
	}
	tmp[i] = '\0';
	m_size = i;
	delete m_buffer;
	m_buffer = tmp;
}

const char* String::c_str() const {
	return m_buffer;
}

char& String::at(size_t pos) {
	if (pos > m_size - 1 || pos < 0 || m_size == 0) {
		throw std::out_of_range("");
	} else {
		return *(&m_buffer[pos]);
	}
}

const char& String::front() {
	return *(&m_buffer[0]);
}

const char& String::back() {
	return *(&m_buffer[m_size - 1]);
}

void String::push_back(char ch) {
	if(m_capacity <= m_size + 1) {
		(*this).realoc(10);
	}
	m_buffer[m_size++] = ch;
	m_buffer[m_size] = '\0';
}

void String::pop_back() {
	if(!m_buffer) {
		return;
	}
	m_buffer[--m_size] = '\0';
}

String& String::erase(size_t index, size_t count) {
	if(index < 0 || index >= m_size) {
		throw std::out_of_range("");
	}
	if(count > (m_size - index)) {
		m_buffer[index] = '\0';
		m_size = index;
	} else {
		for(int i = (index + count); i <= m_size; ++i) {
			m_buffer[i - count] = m_buffer[i];
		}
	}
	return *this;
}

void String::clear() {
	if(!m_buffer) return;
	m_size = 0;
	m_buffer[m_size] = '\0';
}

String& String::insert(size_t index, const char* str) {
	int size1 = my_length(str);
	if((m_size + size1 + 1) > m_capacity) {
		(*this).realoc(size1 + 1);
	}
	if(index > m_size || index < 0) {
		throw std::out_of_range("");
	}
	else if(index == 0 && (*this).empty()) {
		int i = 0;
		for(; i < size1; ++i) {
			m_buffer[i] = str[i];
		}
		m_buffer[i] = '\0';
		m_size = i;
	}
	else if(!(*this).empty() && index == m_size) {
		for(int i = 0; i < size1; ++i) {
			m_buffer[m_size] = str[i];
			++m_size;
		}
		m_buffer[m_size] = '\0';
	}
	else if(index > 0 && (index < m_size)) {
		int j = m_size + size1; 
		for(int i = m_size; i >= index; --i) {
			m_buffer[j] = m_buffer[i];
			--j;
		}
		for(int i = 0; i < size1; ++i) {
			m_buffer[index + i] = str[i];	
		}
	}
	return *this;
}

String& String::append(size_t count, char ch) {
	for(int i = 0; i < count; ++i) {
	(*this).push_back(ch);	
	}
	return *this;
}
	
String& String::append(size_t count, const char* src) {
	int size1 = my_length(src);
	if(m_capacity < (m_size + count + 1)) {
		(*this).realoc(count + 1);
	}	
	for(int j = 0; j < count; ++j) {
		m_buffer[m_size++] = src[j];
	}
	m_buffer[m_size] = '\0';
	return *this;
}

bool String::empty() {
	return !m_size;
}

bool String::compare(const String& src) {
	if (m_size != src.m_size) {
		return false;
	}
		for(int i = 0; i < m_size; ++i) {
			if (m_buffer[i] != src.m_buffer[i]) {
				return false;
			}
		}
		return true;
}

bool String::starts_with(char ch) {
	return m_buffer[0] == ch;
}

bool String::starts_with(const char* src) {
	int size = my_length(src);
	for(int i = 0; i < size; ++i) {
		if(m_buffer[i] != src[i]) {
			return false;
		}
	}
	return true;
}

bool String::ends_with(char ch) {
	return m_buffer[m_size - 1] == ch;
}

bool String::ends_with(const char* src) {
	int size1 = my_length(src);
	int size = size1 - 1;
	bool tmp = true;
	for(int i = 0; i < size1; ++i) {
		if(m_buffer[m_size - 1 - i] != src[size--]) {
			tmp = false;
		}
	}
	return tmp;
}

bool String::contains(char ch) {
	return ((*this).find(ch) != -1);
}

bool String::contains(const char* src) {
	return ((*this).find(src) != -1);
}

int String::find(char ch) {
	int i = 0;
	if (!m_buffer) {
		return -1;
	}
	while (m_buffer[i]) {
		if (m_buffer[i] == ch) {
			return i;
		}
		++i;
	}
	return -1;
}

int String::find(const char* src) {
	int size1 = my_length(src);
	bool tmp = true;
	int i = 0;
	for (; i < m_size; ++i) {
		for (int j = 0; j < size1; ++j) {
			if (m_buffer[i + j] != src[j]) {
				tmp = false;
				break;
			} else { 
				tmp = true;
			}
		}
   	if (tmp == true) {
        return i;
     	}
	}
	return -1;
}

String& String::substr(size_t index, size_t count) {
	if(index < 0 || index > m_size) {
		throw std::out_of_range("");
	}
	char tmp[count + 1];
	for(int i = 0; i < count; ++i) {
		tmp[i] = m_buffer[index + i];
	}
	tmp[count] = '\0';
	for(int i = 0; i < count; ++i) {
		m_buffer[i] = tmp[i];
	}
	m_buffer[count] = '\0';
	return *this;                                  //can't return another String
}

int String::copy(char* dest, int count, int index = 0) {
	int size1 = my_length(dest);
	if(index >= m_size) {
		throw std::out_of_range("");
	}
	int len = m_size - index;
	if(len < count) {
		count = len;
	}
	for(int i = 0; i < count; ++i) {
		dest[i] = m_buffer[index + i];
	}
	return count;
}

void String::resize(int count, char ch = '\0') {
	if(m_size >= count) {
		m_size = count;
		m_buffer[m_size] = '\0';
	} else {
		if((count + 1) > m_capacity) {
			(*this).realoc(count + 1);
		}
		for(int i = 0; i < (count - m_size); ++i) {
			(*this).push_back(ch);
		}
	}
}

size_t String::size() const {
	return m_size;
}

size_t String::capacity() const {
	return m_capacity;
}

void String::shrink_to_fit() {
	m_capacity = m_size;
}

void String::swap(String& other) {
	String tmp;
	tmp = *this;
	*this = other;
	other = tmp;
}

String& String::operator=(const String& src) {
	if(this == &src) {
		return *this;
	}
	delete m_buffer;
	m_buffer = nullptr;
	m_size = src.m_size;
	m_capacity = src.m_capacity;
	m_buffer = new char[m_capacity];
	for(int i = 0; i < m_size; ++i) {
		m_buffer[i] = src.m_buffer[i];
	}
	return *this;
}

String& String::operator+=(char ch) {
	if(!ch) {
		return *this;
	}
	if(m_capacity <= (m_size + 1)) {
		(*this).realoc(10);
	}
	(*this).append(1, ch);
	return *this;
}

String& String::operator+=(const char* src) {
	if(!src) {
		return *this;
	}
	int size1 = my_length(src);
	if(m_capacity <= (m_size + size1)) {
		(*this).realoc(size1 + 1);
	}
	(*this).append(size1, src);
	return *this;
  }

String& String::operator+=(const String& src) {
	if(m_capacity <= (m_size + src.m_size)) {
		(*this).realoc(src.m_size + 1);
	}
	(*this).append(src.m_size, src.m_buffer);
	m_size += src.m_size;
	return *this;
} 

char& String::operator[](size_t pos) {
	if (pos > m_size - 1 || pos < 0 || m_size == 0) {
		throw std::out_of_range("");
	} else {
		return *(&m_buffer[pos]);
	}
}

bool operator==(String& ptr, String& str) {
	if (ptr.m_size != str.m_size) {
		return false;
	}
	for (int i = 0; i < ptr.m_size; ++i) {
		if (ptr.m_buffer[i] != str.m_buffer[i]) {
			return false;
		}
	}
	return true;
}

bool operator!=(String& ptr, String& str) {
	return !(ptr == str);
}

bool operator>(String& ptr, String& str) {
	if(ptr.m_size <= str.m_size) {
		return false;
	}
	bool tmp = true;
	for(int i = 0; i < (ptr.m_size - str.m_size); ++i) {
		for(int j = 0; j < str.m_size; ++j) {
			if(ptr.m_buffer[i + j] != str.m_buffer[j]) {
				tmp = false;
				break;
			} else {
				tmp = true;
			}
		}
		if(tmp == true) {
			return true;
		}
	}
	return false;
}	

bool operator<(String& ptr, String& str) {
	return operator>(str, ptr);
}

bool operator>=(String& ptr, String& str) {
	return (operator>(ptr, str) or operator==(ptr, str));
}

bool operator<=(String& ptr, String& str) {
	return (operator<(ptr, str) or operator==(ptr, str));
}

std::ostream& operator<<(std::ostream& os, const String& src) {
	int i = 0;
	if (!src.m_size) {
		os << "";
    	return os;
	}
	while (src.m_buffer[i]) {
		os << src.m_buffer[i++];
	} 
	return os;
};

int main() {
	//
}
