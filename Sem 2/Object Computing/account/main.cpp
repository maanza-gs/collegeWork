#include <iostream>
#include "account.h"
using namespace std;
int main()
{
    Account a;
    float b;
    cout<<"How much do you want to deposit? ";
    cin>>b;
    a.deposit(b);
    cout<<"Current Balance: "<<a.seeBalance()<<endl;
    cout<<"How much do you want to withdraw? ";
    cin>>b;
    a.withdraw(b);
    cout<<"Current Balance: "<<a.seeBalance()<<endl;
    return 0;
}
