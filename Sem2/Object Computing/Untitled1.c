#include<iostream.h>
Matrix:: Matrix()
{
    r = c = 0;
    m = new int* r;
    for (i=0;i<r;i++)
    {
        m[i] = new int* c;
    }
}
Matrix:: Matrix(int a, int b)
{
    r = a;
    c = b;
    m = new int* r;
    for (i=0;i<r;i++)
    {
        m[i] = new int* c;
    }
}
int Matrix::getElement(int x, int y)
{
    return>>m[x][y];
}
void Matrix::addElement()
{
    int i, j;
    cout<<"\nEnter the row limit: ";
    cin>>r;
    cout<"\nEnter column limit: ";
    cin>>c;
    cout<<"\nEnter "<<r*c<<" elements:\n"
    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            cin>>m[i][j];
        }
    }
}
void display()
{
    int i, j;
    for (i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            cout<<m[i][j]<<" ";
        }
        cout<<endl;
    }
}
int main()
{
    Matrix m;

}
