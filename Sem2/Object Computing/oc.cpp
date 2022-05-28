#include <iostream>
class Point
{
        int x, y;
    public:
        Point ();
        Point (int, int);
        void operator + ();
        void operator - ();
        Point operator + (Point);
        Point operator - (Point);
        Point operator * (Point);
}
