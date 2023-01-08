#include <iostream>
#include <malloc.h>
#include <math.h>
#include <cstdio>
using namespace std;
#define M 128
#define N 128 
#define MaxSize M*N

//三元组定义
typedef struct{
	int r;
	int c;
	double d;//元素值
} TupNode;

//三元组顺序表定义
//总共有多少行，多少列
//里面含有多少个元素
typedef struct{
	int rows;//标准矩阵行数
	int cols;//标准矩阵列数
	int nums;//矩阵的非零值数量
	TupNode data[MaxSize];
} TSMatrix;

//将一个矩阵转为稀疏矩阵t
void CreatMat(TSMatrix& t, double A[M][N]){
	t.rows = M;
	t.cols = N;
	t.nums = 0;
	for (int i = 0; i < M; i++)
		for (int j = 0; j < N; j++)
			if (A[i][j] != 0)  
			{
                //如果这个元素不是0，就把它读入系数矩阵
				t.data[t.nums].r = i;
				t.data[t.nums].c = j;
				t.data[t.nums].d = A[i][j];
				t.nums++;//每读入一个元素，nums+1
			}
}

//稀疏矩阵相乘
//由矩阵乘法规则可知
//C(i,j) = A(i,1)*B(1,j)+A(i,2)*B(2,j)+....+A(i,n)*B(n,j)
//即C(i,j)为A的第i行与B的第j列非零元素乘积之和。
bool MatMul(TSMatrix a, TSMatrix b, double c[M][N]){
	int i, j = 0;
	//a乘b，如果a的行数与b的列数不相等，则两个矩阵无法相乘
	if (a.cols != b.rows)
		return false;//返回执行错误
	
	for (i = 0; i < a.nums; i++){
		for (j = 0; j < b.nums; j++){
			if (a.data[i].c == b.data[j].r){
				c[a.data[i].r][b.data[j].c] = a.data[i].d * b.data[j].d + c[a.data[i].r][b.data[j].c];
			}
		}
	}
		
	return true;//返回执行正确
}

int main(int argc ,char* argv[]){
    if (argc != 4){
		printf("Input argv Error!\n");
		return -1;
	}
    
    FILE * fp1, * fp2, *fp3;
    
    fp1 = fopen(argv[1], "r");
	fp2 = fopen(argv[2], "r");
    fp3 = fopen(argv[3], "w");

    if (fp1 && fp2 == NULL){
		printf("Input file Error!\n");
		return -1;
	}

    double a1[M][N], b1[M][N];

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

	TSMatrix a, b;

	double c[M][N] = {0};

    CreatMat(a, a1);
	CreatMat(b, b1);

    MatMul(a, b, c);

    //输出矩阵C
	for (int i = 0; i < M; i++){
		for (int j = 0; j < N; j++){
			fprintf(fp3, "%lf ", c[i][j]);
		}
        fprintf(fp3, "\n");
	}

    return 0;

}