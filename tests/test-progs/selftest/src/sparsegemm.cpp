#include <iostream>
#include <malloc.h>
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

//函数功能：赋值。令t[i,j]处的值等于x
bool Value(TSMatrix& t, double x, int i, int j){
	int k = 0, k1;
	if (i >= t.rows || j >= t.cols)
		return false;
	while (k<t.nums && i>t.data[k].r)k++;
	while (k<t.nums && i == t.data[k].r && j>t.data[k].c)k++;
	if (t.data[k].r == i && t.data[k].c == j)
		t.data[k].d = x;
	else
	{
		for (k1 = t.nums - 1; k1 >= k; k1--)
		{
			t.data[k1 + 1].r = t.data[k].r;
			t.data[k1 + 1].c = t.data[k].c;
			t.data[k1 + 1].d = t.data[k].d;
		}
		t.data[k].r = i;
		t.data[k].c = j;
		t.data[k].d = x;
		t.nums++;
	}
	return true;
}

//函数功能：令x=矩阵t[i,j]处的值
//相当于取出矩阵t[i,j]处的值
bool Assign(TSMatrix t, double& x, int i, int j){
	int k = 0;
	if (i >= t.rows || j >= t.cols)
		return false;
	while (k<t.nums && i>t.data[k].r)k++;
	while (k<t.nums && i == t.data[k].r && j>t.data[k].c)k++;
	if (t.data[k].r == i && t.data[k].c == j)
		x = t.data[k].d;
	else
		x = 0;
	return true;
}

//将稀疏矩阵t转置为稀疏矩阵tb
void TranMat(TSMatrix t, TSMatrix& tb){
	int i, j, k = 0;
	tb.rows = t.cols; //t的行数变为tb的列数
	tb.cols = t.rows; //t的列数变为tb的行数
	tb.nums = t.nums; //t的非零值和tb的非零值相同
	if (t.nums != 0)  //如果该矩阵有非0值
	{
		//这是很慢的算法了
		//按列来扫是因为转置矩阵相当于按行来添加的元素
		for (i = 0; i < t.cols; i++) //按列来扫
			for (j = 0; j < t.nums; j++)
				if (t.data[j].c == i) //如果该元素的行数等于现在的行数
				{
					tb.data[k].r = t.data[j].c;
					tb.data[k].c = t.data[j].r;
					tb.data[k].d = t.data[j].d;
					k++;
				}
	}
}

//返回矩阵c低i行第j列的值
double getvalue(TSMatrix c, int i, int j){
	int k = 0;
	//遍历稀疏矩阵里的值
	while (k < c.nums && (c.data[k].r != i || c.data[k].c != j))
		k++;
	if (k < c.nums)
		return (c.data[k].d);
	else//稀疏矩阵，如果没有找到当然就返回0
		return 0;
}

//稀疏矩阵相乘
//由矩阵乘法规则可知
//C(i,j) = A(i,1)*B(1,j)+A(i,2)*B(2,j)+....+A(i,n)*B(n,j)
//即C(i,j)为A的第i行与B的第j列非零元素乘积之和。
bool MatMul(TSMatrix a, TSMatrix b, TSMatrix& c){
	int i, j, k, p = 0;
	double s;//s用来累加相乘的值
	//a乘b，如果a的行数与b的列数不相等，则两个矩阵无法相乘
	if (a.cols != b.rows)
		return false;//返回执行错误
	
	for (i = 0; i < a.rows; i++)
		for (j = 0; j < b.cols; j++)
		{
			s = 0;
			//这一步用getvalue函数很聪明，因为getvalue对没有值的数据会返回0
			for (k = 0; k < a.cols; k++)
				s += getvalue(a, i, k) * getvalue(b, k, j);
			//如果算出来的结果不为0，就添加到稀疏矩阵c中
			if (s != 0)  
			{
				c.data[p].r = i;
				c.data[p].c = j;
				c.data[p].d = s;
				p++;
			}
		}
	//乘完后，c的行数等于a的行数，c的列数等于a的列数
	c.rows = a.rows;
	c.cols = b.cols;
	//c里面总共有p个有值的数
	c.nums = p;
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

    TSMatrix a, b, c;

	CreatMat(a, a1);
	CreatMat(b, b1);
    MatMul(a, b, c);

    //输出矩阵C
	for (int i = 0; i < M; i++){
		for (int j = 0; j < N; j++){
			fprintf(fp3, "%lf ", getvalue(c, i, j));
		}
        fprintf(fp3, "\n");
	}

    return 0;

}