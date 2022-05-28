#ifndef POINTS_H
#define POINTS_H

class Point
{
        int x, y;
    public:
        Point();
        Point(int, int);
        void operator+();
        void operator-();
        Point operator+(Point);
        Point operator-(Point);
        Point operator*(Point);
        bool operator!();
        void display();
};


#endif // POINTS_H
