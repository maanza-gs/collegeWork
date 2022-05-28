#ifndef SETS_H_INCLUDED
#define SETS_H_INCLUDED



#endif // SETS_H_INCLUDED
class Set
{
        int *a, n;
    public:
        Set(int);
        void display();
        void input();
        void add_elt(int, int);
        void remove_elt(int,int);
        Set operator | (Set);
        Set operator & (Set);
};
