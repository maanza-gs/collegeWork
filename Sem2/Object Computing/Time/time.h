//1
#ifndef TIME_H_INCLUDED
#define TIME_H_INCLUDED



#endif // TIME_H_INCLUDED
class Time
{
        int hour, minute, second;
    public:
        Time();
        Time(int, int, int);
        void printTime();
        Time operator +(Time);
        bool operator >(Time);
};
