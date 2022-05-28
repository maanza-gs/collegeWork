#ifndef MATRIX_H_INCLUDED
#define MATRIX_H_INCLUDED



#endif // MATRIX_H_INCLUDED
class Matrix
{
        int **m, r, c;
    public:
        Matrix();
        Matrix(int, int);
        void display();
        Matrix addMatrix(Matrix);
        Matrix subMatrix(Matrix);
        Matrix mulMatrix(Matrix);
        int getElement(int, int);
        void addElement();
};
