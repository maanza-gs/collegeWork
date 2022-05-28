#ifndef COUNTRY_H_INCLUDED
#define COUNTRY_H_INCLUDED
#include <string>
using namespace std;

#endif // COUNTRY_H_INCLUDED
class Country
{
        string countryName, area;
        double population;
    public:
        Country();
        friend void largestArea();
        friend void largestPop();
        friend void largePopden();
};
