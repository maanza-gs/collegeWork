//1
#include <iostream>
#include "time.h"
using namespace std;
int main()
{
    Time t3;
    Time t1(3,0,7), t2(4,0,0);
    t1.printTime();
    t2.printTime();
    t3 = t1+t2;
    t3.printTime();
    if (t1>t2)
    {
        cout<<"Greater Time: ";
        t1.printTime();
    }
    else
    {
        cout<<"Greater Time: ";
        t2.printTime();
    }
}
