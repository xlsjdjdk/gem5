using namespace std;
#include <iostream>

#define M 32
#define N 128

void matrix_multply(double *a, double *b, double *c,  int n)
{
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            double sum = c[i*N + j] ;
            for(int k = 0; k < n; k++)
            {
                sum += a[i*N + k] * b[k*N + j];
            }
            c[i*N + j] = sum; 
        }
    }        
}

void matrix_multply_quick(double *a, double *b, double *c,  int n)
{
    double s;
    for(int i = 0; i < n; i++){
        for(int k = 0; k < n; k++){
            s = a[i*N + k];
            for(int j = 0; j < n; j++){
                c[i*N + j] += s*b[k*N + j];
            }
        }
    }
}

void dgemm_block (double* a, double* b, double* c, int n)
{
    for ( int sj = 0; sj < n; sj += M )

        for ( int si = 0; si < n; si += M )

            for ( int sk = 0; sk < n; sk += M )

                matrix_multply(a+si*n+sk, b+sk*n+sj,  c+si*n+sj, M);

}

int main(){
    double a[16384],b[16384],c[16384];
    for (int i =0 ; i<16384;i++){
        a[i] = i;
        b[i] = i;
    }
    //matrix_multply(a,b,c,128);
    cout <<"gemm end " << endl;
    return 0;
}