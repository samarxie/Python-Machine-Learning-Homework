/*
*date    : 2018-05-06 10:19:34
*author  : lyrichu
*email   :919987476@qq.com
*link    : https://www.github.com/Lyrichu
*version : 0.1
*description:
*Q4:使用dfs实现八皇后问题.
*/
#include <stdio.h>
#include <stdlib.h>
#define N 10  // 皇后个数
int total = 0; //可行解总数
int C[N]; // C[i] 表示第i行皇后所在的列编号
int columns[N]; // 表示已经放置的皇后占了哪些列
// 占据了哪些主对角线
int principal[2*N];
//占据了哪些副对角线
int counter[2*N];


// 按列打印可行解
void output()
{
	int i,j;
	printf("No. %d\n",total);
	for(j=0;j<N;++j)
	{
		for(i=0;i<N;++i)
		{
			if(C[i] != j)
				printf("0 ");
			else
				printf("1 ");
		}
		printf("\n");
	}
}

/*
检查当前位置(row,col)能否放置皇后
@param row:当前行
@param col:当前列
@return:能返回1,不能返回0
*/
int check(int row,int col)
{
	// 需要检查列，主对角线以及副对角线是否已经放置
	return columns[col] == 0 && principal[row+col] == 0 && counter[row-col+N] == 0;
}
/*
八皇后，深度优先搜索,用空间换时间
@param row:搜索当前行，该在哪一列上放皇后
@return:可行解的个数
*/
int search(const int row)
{
	int j;
	if(row == N)  // 找到了一个可行解
	{
		++total;
		output(); //打印可行解
		return total;
	}
	// 一列一列的试
	for(j=0;j<N;++j)
	{
		const int ok = check(row,j); // 检查row行,j列是否合法
		// 如果合法，则继续递归
		if(ok)
		{
			// 执行扩展动作
			C[row] = j;
			columns[j] = principal[row+j] = counter[row-j+N] = 1;
			search(row+1);
			// 撤销动作
			columns[j] = principal[row+j] = counter[row-j+N] = 0;
		}
	}
	return total;
}

int main(int argc, char const *argv[])
{
	search(0);
	return 0;
}