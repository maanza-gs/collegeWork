#include <iostream>
#include "Address.h"
using namespace std;
int main()
{
    Address a;
    Address a1("B2");
    a.accept();
    a1.accept();
    a.print();
    a1.print();
    a.comes_before(a1);
    return 0;
}
