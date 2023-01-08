using namespace std;
#include <iostream>

#define M 32
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


void matrix_multiply_T(double *a, double *b, double *c,  int n)
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

void matrix_multiply_Tun(double *a, double *b, double *c,  int n)
{
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            double sum = c[i*N + j] ;
            for(int k = 0; k < n; k=k+32)
            {
                sum = sum + a[i*N + k] * b[j*N + k]+a[i*N + k+1] * b[j*N + k+1] +a[i*N + k+2] * b[j*N + k+2]+a[i*N + k+3] * b[j*N + k+3]
                    + a[i*N + k+4] * b[j*N + k+4]+a[i*N + k+5] * b[j*N + k+5] +a[i*N + k+6] * b[j*N + k+6]+a[i*N + k+7] * b[j*N + k+7]
                    + a[i*N + k+8] * b[j*N + k+8]+a[i*N + k+9] * b[j*N + k+9] +a[i*N + k+10] * b[j*N + k+10]+a[i*N + k+11] * b[j*N + k+11]
                    + a[i*N + k+12] * b[j*N + k+12]+a[i*N + k+13] * b[j*N + k+13] +a[i*N + k+14] * b[j*N + k+14]+a[i*N + k+15] * b[j*N + k+15]
                    + a[i*N + k+16] * b[j*N + k+16]+a[i*N + k+17] * b[j*N + k+17] +a[i*N + k+18] * b[j*N + k+18]+a[i*N + k+19] * b[j*N + k+19]
                    + a[i*N + k+20] * b[j*N + k+20]+a[i*N + k+21] * b[j*N + k+21] +a[i*N + k+22] * b[j*N + k+22]+a[i*N + k+23] * b[j*N + k+23]
                    + a[i*N + k+24] * b[j*N + k+24]+a[i*N + k+25] * b[j*N + k+25] +a[i*N + k+26] * b[j*N + k+26]+a[i*N + k+27] * b[j*N + k+27]
                    + a[i*N + k+28] * b[j*N + k+28]+a[i*N + k+29] * b[j*N + k+29] +a[i*N + k+30] * b[j*N + k+30]+a[i*N + k+31] * b[j*N + k+31];
            
            }
            c[i*N + j] = sum; 
        }
    }        
}


void matrix_multiply(double *a, double *b, double *c,  int n)
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

void matrix_multiply_un(double *a, double *b, double *c,  int n)
{
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            double sum = c[i*N + j] ;
            for(int k = 0; k < n; k=k+32)
            {
                sum = sum + a[i*N + k] * b[k*N + j]+ a[i*N + k+1] * b[(k+1)*N + j]+ a[i*N + k+2] * b[(k+2)*N + j]+ a[i*N + k+3] * b[(k+3)*N + j]
                    + a[i*N + k+4] * b[(k+4)*N + j]+ a[i*N + k+5] * b[(k+5)*N + j]+ a[i*N + k+6] * b[(k+6)*N + j]+ a[i*N + k+7] * b[(k+7)*N + j]
                    + a[i*N + k+8] * b[(k+8)*N + j]+ a[i*N + k+9] * b[(k+9)*N + j]+ a[i*N + k+10] * b[(k+10)*N + j]+ a[i*N + k+11] * b[(k+11)*N + j]
                    + a[i*N + k+12] * b[(k+12)*N + j]+ a[i*N + k+13] * b[(k+13)*N + j]+ a[i*N + k+14] * b[(k+14)*N + j]+ a[i*N + k+15] * b[(k+15)*N + j]
                    + a[i*N + k+16] * b[(k+16)*N + j]+ a[i*N + k+17] * b[(k+17)*N + j]+ a[i*N + k+18] * b[(k+18)*N + j]+ a[i*N + k+19] * b[(k+19)*N + j]
                    + a[i*N + k+20] * b[(k+20)*N + j]+ a[i*N + k+21] * b[(k+21)*N + j]+ a[i*N + k+22] * b[(k+22)*N + j]+ a[i*N + k+23] * b[(k+23)*N + j]
                    + a[i*N + k+24] * b[(k+24)*N + j]+ a[i*N + k+25] * b[(k+25)*N + j]+ a[i*N + k+26] * b[(k+26)*N + j]+ a[i*N + k+27] * b[(k+27)*N + j]
                    + a[i*N + k+28] * b[(k+28)*N + j]+ a[i*N + k+29] * b[(k+29)*N + j]+ a[i*N + k+30] * b[(k+30)*N + j]+ a[i*N + k+31] * b[(k+31)*N + j];
                

            }
            c[i*N + j] = sum; 
        }
    }        
}

void matrix_multiply_quick(double *a, double *b, double *c,  int n)
{
    for(int i = 0; i < n; i++){
        for(int k = 0; k < n; k++){
            double s = a[i*N + k];
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

                matrix_multiply(a+si*n+sk, b+sk*n+sj,  c+si*n+sj, M);

}

void dgemm_block_T (double* a, double* b, double* c, int n)
{
    for ( int sj = 0; sj < n; sj += M )

        for ( int si = 0; si < n; si += M )

            for ( int sk = 0; sk < n; sk += M )

                matrix_multiply_Tun(a+si*n+sk, b+sj*n+sk,  c+si*n+sj, M);

}

void dgemm_block_s (double* a, double* b, double* c, int n)
{

    for ( int sk = 0; sk < n; sk += M )

        for ( int si = 0; si < n; si += M )
        
            for ( int sj = 0; sj < n; sj += M )

        
                matrix_multiply_T(a+si*n+sk, b+sj*n+sk,  c+si*n+sj, M);

}

int main(){
    double a[16384],b[16384],c[16384];
    for (int i =0 ; i<16384;i++){
        a[i] = i;
        b[i] = i;
    }
    dgemm_block_T(a,b,c,128);
    cout <<"block_gemm end " << endl;
    return 0;
}