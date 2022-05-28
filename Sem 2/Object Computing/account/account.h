#ifndef ACCOUNT_H_INCLUDED
#define ACCOUNT_H_INCLUDED

#endif // ACCOUNT_H_INCLUDED
class Account
{
        float balance;
    public:
        Account();
        void withdraw(float);
        void deposit(float);
        int checkBalance(float);
        void cInterest();
        float seeBalance();
};
