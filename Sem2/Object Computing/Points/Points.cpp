#include "Points.h"
#include <iostream>
using namespace std;

Point:: Point()
{
    x = y = 0;
}
Point:: Point(int a, int b)
{
    x = a;
    y = b;
}
void Point:: operator+()
{
    x = ++x;
    y = ++y;
}
void Point:: operator-()
{
    x = --x;
    y = --y;
}
Point Point:: operator+(Point p2)
{
    Point p3;
    p3.x = x + p2.x;
    p3.y = y + p2.y;
    return p3;
}
Point Point:: operator-(Point p2)
{
    Point p3;
    p3.x = x - p2.x;
    p3.y = y - p2.y;
    return p3;
}
Point Point:: operator*(Point p2)
{
    Point p3;
    p3.x = x * p2.x;
    p3.y = y * p2.y;
    return p3;
}
void Point:: display()
{
    cout<<"X = "<<x<<"\tY = "<<y<<endl;
}
bool Point:: operator!()
{
    if (x!=0 && y!=0)
        return true;
    else
        return false;
}
