#include <iostream>
#include "account.h"
using namespace std;
Account::Account()
{
    balance = 10000;
}
int Account::checkBalance(float b)
{
    if(b>balance)
        return 5;
    else
        return 0;
}
float Account::seeBalance()
{
    return balance;
}
void Account::withdraw(float b)
{
    balance -= b + checkBalance(b);
}
void Account::deposit(float b)
{
    balance+=b;
}
