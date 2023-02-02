#include <iostream> 
#include <vector> 
 
typedef unsigned int uint; 
const uint SIZE_UINT = sizeof(uint) * 8; 
 
class Bitset { 
private: 
    std::vector<uint> m_bitset; 
    uint m_length; 
public: 
    Bitset(uint, uint); 
    void set(uint); 
    void reset(uint);
    Bitset& flip();
    Bitset& flip(uint);
    friend std::ostream& operator<<(std::ostream& os, const Bitset& obj);
    bool operator[](uint) const;
    bool test(uint) const;
    uint count() const;
}; 
 
//doesn't work properly for len > 32, e.g. Bitset(34, 1) 
Bitset::Bitset(uint len, uint value) { 
    if(len < 0) {
        throw std::invalid_argument("Length must be greater than 0");
    }
    else if(len == 0) {
        m_length = len; 
        m_bitset.resize(0, value);
    }
    else {
    m_length = len;
    m_bitset.resize((len - 1) / SIZE_UINT + 1, value);
    }
} 
 
void Bitset::set(uint index) { 
    if(index >= m_length) { 
        throw std::out_of_range("Index out of range"); 
    } else { 
        m_bitset[m_bitset.size() - 1 - index / SIZE_UINT] |= (1 << (index % SIZE_UINT)); 
    } 
} 
 
void Bitset::reset(uint index) { 
    if(index >= m_length) { 
        throw std::out_of_range("Index out of range"); 
    } else { 
        m_bitset[m_bitset.size() - 1 - index / SIZE_UINT] &= ~(1 << (index % SIZE_UINT)); 
    } 
} 

Bitset& Bitset::flip() {
    for(uint i = 0; i < m_bitset.size(); ++i) {
        m_bitset[i] = ~m_bitset[i];
    }
    return *this;
}

Bitset& Bitset::flip(uint index) {
    if (index < m_length) {
        uint vec_index = m_bitset.size() - 1 - index / SIZE_UINT;
        uint bit_index = index % SIZE_UINT;
        m_bitset[vec_index] ^= 1 << bit_index;
    }
    return *this;
}
 
std::ostream& operator<<(std::ostream& os, const Bitset& obj) { 
    if(obj.m_length > 0) {
        uint tmp = (1 << (SIZE_UINT - 1)); 
        for(int j = (SIZE_UINT - 1) - ((obj.m_length - 1) % SIZE_UINT); j < SIZE_UINT; ++j) { 
            os << bool(obj.m_bitset[0] & (tmp >> j)); 
        } 
        for(int i = 1; i < obj.m_bitset.size(); ++i) {  
            for(int j = 0; j < SIZE_UINT; ++j) { 
                os << bool(obj.m_bitset[i] & (tmp >> j)); 
            } 
        } 
    }
    return os; 
} 

bool Bitset::operator[](uint index) const {
    uint vec_index = m_bitset.size() - 1 - index / SIZE_UINT;
    uint bit_index = index % SIZE_UINT;
    return (m_bitset[vec_index] >> bit_index) & 1;
}

bool Bitset::test(uint index) const {
    if(index >= m_length) { 
        throw std::out_of_range("Index out of range"); 
    }
    uint vec_index = m_bitset.size() - 1 - index / SIZE_UINT;
    uint bit_index = index % SIZE_UINT;
    return (m_bitset[vec_index] >> bit_index) & 1;
}

uint Bitset::count() const {
    uint count = 0;
    uint vec_index = m_bitset.size() - 1;
    uint bit_index = m_length % SIZE_UINT;
    for(uint i = 0; i <= bit_index; ++i) {
        if((m_bitset[0] >> i) & 1) {
            ++count;
        }
    }
    for(uint i = 1; i <= vec_index; ++i) {
        for(uint j = 0; j < SIZE_UINT; ++j) {
            if((m_bitset[i] >> j) & 1) {
                ++count;
            }
        }
    }
    return count;
}
 
int main() { 
    Bitset bs = Bitset(5, 2); 
    std::cout << bs << std::endl; 
    std::cout << bs.count() << std::endl;
    // std::cout << bs.flip() << std::endl; 
    // bs.set(0); 
    // bs.set(1); 
    // std::cout << bs << std::endl;
    // bs.reset(0);  
    // std::cout << bs << std::endl;
    return 0; 
}