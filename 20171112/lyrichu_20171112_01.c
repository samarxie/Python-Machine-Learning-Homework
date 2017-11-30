/*
Q1:数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
*/
#include<stdio.h>
// 快速排序
void quick_sort(int *,int,int);
// 打印数组元素
void print(int *,int);
// 通过快排找
int find_half_num_by_quicksort(int *,int);
// 通过增减索引找
int find_half_num_by_index(int *,int);

int main(void)
{
	int arr[7] = {1,3,3,2,4,2,2};
	printf("%d\n",find_half_num_by_quicksort(arr,7));
	printf("%d\n",find_half_num_by_index(arr,7));
	return 0;
}

void print(int *arr,int n)
{
	for(int i=0;i<n;++i)
		printf("%d ",arr[i]);
	printf("\n");
}
// 快速排序
void quick_sort(int *arr,int begin,int end)
{
	int i = begin;
	int j = end;
	if(i>=j)
		return;
	int key = arr[i]; // 目标值
	while(i < j)
	{
		while(i<j && arr[j]>=key)
			--j;
		arr[i] = arr[j];
		while(i<j && arr[i]<=key)
			++i;
		arr[j] = arr[i];
	}
	// 设置 key 
	arr[i] = key;
	quick_sort(arr,begin,i-1);
	quick_sort(arr,i+1,end);
}

int find_half_num_by_quicksort(int *arr,int n)
{
	// 快排
	quick_sort(arr,0,n-1);
	// 取出中间数字
	int mid = arr[n/2];
	int count = 0;
	for(int i=0;i<n;++i)
	{
		if(arr[i] == mid)
			++count;
	}
	return count > n/2 ? mid:0;
}

int find_half_num_by_index(int *arr,int n)
{
	int value = *arr;
	int count = 1;
	int index = 0;
	while(++index < n)
	{
		if(arr[index] == value)
			++count;
		else
		{
			--count;
			if(count == 0)
				value = arr[index];
		}
	}
	//验证value值是否满足条件
	count = 0;
	for(int i=0;i<n;++i)
	{
		if(arr[i] == value)
			++count;
	}
	return count > n/2 ? value:0;
}


