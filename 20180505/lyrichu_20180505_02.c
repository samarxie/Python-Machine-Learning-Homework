/*
*date    : 2018-05-05 11:45:28
*author  : lyrichu
*email   :919987476@qq.com
*link    : https://www.github.com/Lyrichu
*version : 0.1
*description:
*n 的全排列(采用dfs)
*/
#include <stdio.h>

#define MAXN 10
int N; // n的大小
int count; // 统计全排列个数
int history[MAXN]; // 记录每个位置的数字大小

void dfs(int);

void dfs(int i)
{
	if(i == N) // 已经找到最后一个位置,输出当前的解,count 递增１
	{
		count++;
		for(int j=0;j<N;j++)
			printf("%d ",history[j]);
		printf("\n");
		return;
	}
	// 为第i个位置填数(1-N之间)
	for(int k=1;k<=N;k++)
	{
		int ok = 1; // 判断填数是否合法
		// 遍历i之前的数字判断填数是否合法
		for(int j=0;j<i;j++)
		{
			if(history[j] == k) // i位置与j位置填数相同，不合法
				ok = 0;
		}
		if(ok) // 合法
		{
			history[i] = k; // ｉ位置填k
			dfs(i+1);
		}
	}
}

int main(int argc, char const *argv[])
{
	scanf("%d",&N);
	dfs(0);
	return 0;
}
