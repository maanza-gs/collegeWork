#ifndef ADDRESS_H
#define ADDRESS_H
using namespace std;
class Address
{
    private:
        int houseNo, postalCode;
        char street[20], aptNo[10], city[20], state[20];
    public:
        Address();
        Address(char a[10]);
        void accept();
        void print();
        void comes_before(Address);
        int pcode ();
};

#endif // ADDRESS_H
