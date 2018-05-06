/*
*date    : 2018-05-05 13:43:51
*author  : lyrichu
*email   :919987476@qq.com
*link    : https://www.github.com/Lyrichu
*version : 0.1
*description:
*求数组的最长公共递增子序列
输入:一个无序数组
输出:最长公共递增子序列长度
思路:将问题转化为原数组和其递增数组的最长公共子序列的问题
*/
#include <stdio.h>
#include <stdlib.h>
# define MAXN 100 //数组最大长度
int arr1[MAXN]; //原数组
int arr2[MAXN]; // 排序数组
int N; //数组长度
int dp[MAXN+1][MAXN+1]; // dp[i][j]表示arr1前i子数组和arr2前j子数组的最长公共子序列长度

int cmp(const void *a,const void *b)
{
	return *(int*)a - *(int*)b;  // 递增排序
}

void lcs()
{
	for(int i=0;i<=N;i++)
	{
		for(int j=0;j<=N;j++)
		{
			if(i==0 || j==0)
				dp[i][j] = 0;
			else if(arr1[i-1] == arr2[j-1])
				dp[i][j] = dp[i-1][j-1] + 1;
			else
				dp[i][j] = (dp[i-1][j] > dp[i][j-1] ? dp[i-1][j]:dp[i][j-1]);
		}
	}
}

int main(int argc, char const *argv[])
{
	scanf("%d",&N);
	for(int i=0;i<N;i++)
	{
		scanf("%d",&arr1[i]);
		arr2[i] = arr1[i];
	}
	// 对arr2进行排序
	qsort(arr2,N,sizeof(arr2[0]),cmp);
	//初始化dp为0
	for(int i=0;i<=N;++i)
		for(int j=0;j<=N;++j)
			dp[i][j] = 0;
	lcs();
	printf("%d\n",dp[N][N]);
	return 0;
}

