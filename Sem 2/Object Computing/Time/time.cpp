//1
#include "time.h"
#include <iostream>
using namespace std;

Time:: Time()
{
    hour = minute = second = 0;
}
Time:: Time (int h, int m, int s)
{
    hour = h;
    minute = m;
    second = s;
}
Time Time::operator +(Time t)
{
    Time t2;
    t2.hour = hour + t.hour;
    t2.minute = minute + t.minute;
    t2.second = second + t.second;
    return t2;
}
bool Time::operator >(Time t)
{
    if(hour>t.hour)
        return true;
    else if(hour<t.hour)
        return false;
    else
    {
        if(minute>t.minute)
            return true;
        else if(minute<t.minute)
            return false;
        else
        {
            if(second>t.second)
                return true;
            else if(second<t.second)
                return false;
            else
                return true;
        }
    }
}
void Time::printTime()
{
    cout<< hour <<" Hour(s) "<< minute <<" Minute(s) "<< second << " Second(s)"<< endl;
}
