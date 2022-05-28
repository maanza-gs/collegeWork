#include "Address.h"
#include <iostream>
#include <string.h>
#include "Address.h"
using namespace std;
Address::Address()
{
    houseNo = postalCode = 0;
}
Address::Address (char a[10])
{
    houseNo = postalCode = 0;
    strcpy (aptNo, a);
}
void Address::accept()
{
    cout<<"Enter the following details: \n";
    cout<<"House No: ";
    cin>>houseNo;
    cout<<"Apt. no: ";
    cin>>aptNo;
    cout<<"Street: ";
    cin>>street;
    cout<<"City: ";
    cin>>city;
    cout<<"State: ";
    cin>>state;
    cout<<"Postal Code: ";
    cin>>postalCode;
}
void Address::print()
{
    cout<<"Street: "<<street<<"\nCity: "<<city<<"\tState: "<<state<<"\tPostal Code: "<<postalCode<<endl;
}
void Address::comes_before(Address a)
{
    if(a.pcode()==postalCode)
    {
        cout<<"Both the address belongs to the same place.\n";
    }
    else if(a.pcode()<postalCode)
    {
        cout<<"The given address comes before.\n";
    }
    else
        cout<<"The given address comes after.\n";
}
int Address::pcode()
{
    return postalCode;
}
