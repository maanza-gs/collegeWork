//2
#include <iostream>
#include "sets.h"

using namespace std;

int main()
{
    Set s1(6), s2(8);
    Set s3(14), s4(6);
    s1.input();
    s2.input();
    s1.display();
    s2.display();
    s3 = s1|s2;
    s4 = s1&s2;
    s3.display();
    s4.display();
}
