#include <iostream>
#include <malloc.h>
#include <cstdio>
using namespace std;
#define M 128
#define N 128
#define MaxSize M*N

int main(int argc ,char* argv[]){
    if (argc != 4){
		printf("Input argv Error!\n");
		return -1;
	}
    
    FILE * fp1, * fp2, * fp3;
    
    fp1 = fopen(argv[1], "r");
	fp2 = fopen(argv[2], "r");
    fp3 = fopen(argv[3], "w");

    if (fp1 && fp2 == NULL){
		printf("Input file Error!\n");
		return -1;
	}

    double a1[M][N], b1[M][N], c1[M][N];

    //输入矩阵A
	for (int i = 0; i < M; i++){
		for (int j = 0; j < N; j++){
			fscanf(fp1, "%lf", &a1[i][j]);
		}
	}
	fclose(fp1);

    //输入矩阵B
	for (int i = 0; i < M; i++){
		for (int j = 0; j < N; j++){
			fscanf(fp2, "%lf", &b1[i][j]);
		}
	}
	fclose(fp2);

	//乘法
	for (int i = 0; i < M; i++){
		for (int j = 0; j < N; j++){
			double sum = 0;
			for (int k = 0; k < N; k++){
				sum = sum + a1[i][k] * b1[k][j];
			}
			c1[i][j] = sum;
		}
	}

    //输出矩阵C
	for (int i = 0; i < M; i++){
		for (int j = 0; j < N; j++){
			fprintf(fp3, "%lf ", c1[i][j]);
		}
        fprintf(fp3, "\n");
	}

    return 0;
}