//2
#include <iostream>
#include "sets.h"

using namespace std;

Set::Set(int l)
{
    n = l;
    a = new int[n];
}
void Set::input()
{
    int i;
    cout<<"Creating a set:\n";
    for(i=0;i<n;i++)
    {
        cout<<"Enter element: ";
        cin>>a[i];
        cout<<endl;
    }
}
void Set::add_elt(int x, int i)
{
    a[i] = x;
}
void Set::display()
{
    int i;
    for(i=0;i<n;i++)
    {
        cout<<a[i]<<" ";
    }
    cout<<endl;
}
void Set::remove_elt(int x, int p)
{
    for (int i=0;i<n;i++)
    {
        if(i == p)
        {
            int temp = a[i];
            for(int j = i; j<n;j++)
            {
                a[j] = a[j+1];
            }
            n--;
            cout<<"Element "<<temp<<" was deleted.\n";
            break;
        }
    }
}
Set Set::operator |(Set s)
{
    Set s3(this->n+s.n);
    int i=0, j=0, c;
    while(i<this->n)
    {
        s3.add_elt(a[i], i);
        i++;
    }
    while(j<s.n)
    {
        c=0;
        for(i=0;i<this->n;i++)
        {
            if(s.a[j]==a[i])
            c++;
            break;
        }
        if(c==0)
        {
            s3.add_elt(s.a[j], j);
            j++;
        }
    }
    return s3;
}
Set Set::operator &(Set s)
{
    Set s3(n);
    int i=0, j=0, temp;
    while (i<n)
    {
        if(a[i]>a[i+1])
        {
            temp=a[i];
            a[i]=a[i+1];
            a[i+1]=temp;
        }
        i++;
    }
    while (j<n)
    {
        if(a[j]>a[j+1])
        {
            temp=a[j];
            a[j]=a[j+1];
            a[j+1]=temp;
        }
        j++;
    }
    i=0;
    j=0;
    while(i<n && j<s.n)
    {
        if(a[i]==s.a[j])
        {
            s3.add_elt(a[i], i);
            i++;
            j++;
        }
        i++;
        j++;
    }
    s3.display();
    return s3;
}
