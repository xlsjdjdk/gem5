using namespace std;
#include <iostream>

#define M 64
#define N 128

#include <stdio.h>
#include <stdlib.h>


//Data Type
#define TYPE double

//Algorithm Parameters
#define row_size 128
#define col_size 128
#define L row_size*col_size
#define block_size 128
#define NUMOFBLOCKS L/block_size/block_size

void bbgemm(TYPE m1[L], TYPE m2[L], TYPE prod[L]){
    int i, k, j, jj, kk;
    int i_row, k_row;
    TYPE temp_x, mul;

    loopjj:for (jj = 0; jj < row_size; jj += block_size){
        loopkk:for (kk = 0; kk < row_size; kk += block_size){
            loopi:for ( i = 0; i < row_size; ++i){
                loopk:for (k = 0; k < block_size; ++k){
                    i_row = i * row_size;
                    k_row = (k  + kk) * row_size;
                    temp_x = m1[i_row + k + kk];
                    loopj:for (j = 0; j < block_size; ++j){
                        mul = temp_x * m2[k_row + j + jj];
                        prod[i_row + j + jj] += mul;
                    }
                }
            }
        }
    }
}


void matrix_multply_T(double *a, double *b, double *c,  int n)
{
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            double sum = c[i*N + j] ;
            for(int k = 0; k < n; k++)
            {
                sum += a[i*N + k] * b[j*N + k];
            }
            c[i*N + j] = sum; 
        }
    }        
}


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

void dgemm_block_T (double* a, double* b, double* c, int n)
{
    for ( int sj = 0; sj < n; sj += M )

        for ( int si = 0; si < n; si += M )

            for ( int sk = 0; sk < n; sk += M )

                matrix_multply(a+si*n+sk, b+sj*n+sk,  c+si*n+sj, M);

}

int main(){
    double a[16384],b[16384],c[16384];
    for (int i =0 ; i<16384;i++){
        a[i] = i;
        b[i] = i;
    }
    dgemm_block(a,b,c,128);
    cout <<"block_gemm end " << endl;
    return 0;
}