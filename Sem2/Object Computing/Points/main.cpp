#include <iostream>
#include "points.h"
using namespace std;

int main()
{
    Point p3, p4, p5;
    Point p1(3,4), p2 (2,0);
    p1.display();
    p2.display();
    +p1;
    -p2;
    p1.display();
    p2.display();
    p3 = p1 + p2;
    p3.display();
    p4 = p1 - p2;
    p4.display();
    p5 = p2 * p1;
    p5.display();
    cout<<"\nP1 is";
    if (!p1)
        cout<<" Not origin\n";
    else
        cout<<" Origin\n";
}
