/*
*date    : 2018-05-05 13:14:12
*author  : lyrichu
*email   :919987476@qq.com
*link    : https://www.github.com/Lyrichu
*version : 0.1
*description:
Q3:
给定一个数t，以及n个整数，在这n个数中找到加和为t的所有组合，例如t=4，n=6这6个数为[4,3,2,2,1,1]，
这样输出就有4个不同的组合它们的加和为4:4,3+1,2+2,and 2+1+1。请设计一个高效算法实现这个需求。
思路:先将数据按从大到小进行排序，然后使用回溯法遍历所有可能。注意去掉重复的结果。
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXN 100 // 数组最大长度
int N; // 数组长度
int X[MAXN]; // 标记第i个元素是否使用
int arr[MAXN]; // 记录数组元素
int target; // 目标和
int sum; // 当前和

// 比较函数
int cmp(const void *a,const void *b)
{
	return *(int*)b - *(int*)a; // 递减排序
}

void backtrace(int n)
{
	if(sum > target) // 当前和大于target
		return;
	if(sum == target) // 当前和等于target,输出结果
	{
		for(int j=0;j<n;++j)
		{
			if(X[j]) // 如果第j个位置已经使用过
				printf("%d ",arr[j]);
		}
		printf("\n");
		return;
	}
	if(n == N) // 超过N层,退出
		return;
	// 当前和小于target
	for(int i=n;i<N;++i)
	{
		if(!X[i]) // 第i个位置未使用
		{
			X[i] = 1; // 标记已经使用
			sum += arr[i]; // 更新和
			backtrace(i+1); // 继续回溯
			X[i] = 0;
			sum -= arr[i];
			while(i<N-1 && arr[i] == arr[i+1]) // 跳过相同的
				i++;
		}
	}
}

int main(int argc, char const *argv[])
{
	sum = 0;
	scanf("%d",&N);
	for(int i=0;i<N;i++)
		scanf("%d",&arr[i]);
	scanf("%d",&target);
	//将数组X置为0
	memset(X,0,sizeof(X));
	qsort(arr,N,sizeof(arr[0]),cmp);
	backtrace(0);
	return 0;
}