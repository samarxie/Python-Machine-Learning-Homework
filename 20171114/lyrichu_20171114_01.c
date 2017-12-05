/*
Q1：实现几种不同版本的基于划分的快速排序(基本快速排序,随机化的快速排序等)
*/
#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>
// 快排的划分函数
int partition(int *,int,int);
// 快排的原始划分函数
int old_partition(int *,int,int);
// 随机的划分函数
int random_partition(int *,int,int);
// 基本快速排序 
void quick_sort(int *,int,int);
// 尾递归版本的快速排序
void quick_sort_by_tail_recursion(int *,int,int);
// 随机化的快速排序 
void random_quick_sort(int *,int,int);
// 交换 
void swap(int *,int,int);
// 打印
void print(int *,int);
// 输入测试
void input_test(void);
//运行时间测试
void time_test(void);

int main(void)
{
	srand(time(0));
	time_test();
	//input_test();
	return 0;
}
// 交换数组两个元素
void swap(int *arr,int m,int n)
{
	int temp = *(arr+m);
	*(arr+m) = *(arr+n);
	*(arr+n) = temp;
}
// 打印 
void print(int *arr,int n)
{
	for(int i=0;i<n;++i)
		printf("%d ",*(arr+i));
	printf("\n");
}
// 快排的划分函数
int partition(int *arr,int begin,int end)
{
	int key = arr[end];
	int i,j,temp;
	i = begin-1;
	for(j=begin;j<end;++j)
	{
		if(arr[j]<=key)
		{
			++i;
			// 交换 arr[i] 和 arr[j]
			swap(arr,i,j);
		}
	}
	swap(arr,i+1,end);
	return i+1;
}
// 快排的原始划分函数
int old_partition(int *arr,int begin,int end)
{
	int i,j,key;
	i = begin;
	j = end;
	key = arr[begin];
	while(1)
	{
		while(arr[j]> key)
			j--;
		while(arr[i] < key)
			i++;
		if(i < j)
			swap(arr,i,j);
		else
			return j;
	}
}
// 随机划分函数
int random_partition(int *arr,int begin,int end)
{
	// 产生 begin 到 end 之间的随机数
	int r = begin + (rand() % (end-begin+1));
	swap(arr,r,end);
	return partition(arr,begin,end);
}

// 快速排序 
void quick_sort(int *arr,int begin,int end)
{
	if(begin >= end)
		return;
	int mid = old_partition(arr,begin,end);
	quick_sort(arr,begin,mid-1);
	quick_sort(arr,mid+1,end);
}
// 尾递归版本的快速排序
void quick_sort_by_tail_recursion(int *arr,int begin,int end)
{
	int mid;
	while(begin < end)
	{
		mid = partition(arr,begin,end);
		quick_sort_by_tail_recursion(arr,begin,mid-1);
		begin = mid +1;
	}
}
// 随机快速排序 
void random_quick_sort(int *arr,int begin,int end)
{
	if(begin >= end)
		return;
	int mid = random_partition(arr,begin,end);
	random_quick_sort(arr,begin,mid-1);
	random_quick_sort(arr,mid+1,end);
}

// 输入测试
void input_test(void)
{
	printf("Please input the numbers count: ");
	int count;
	scanf("%d",&count);
	int *arr = (int*)malloc(count*sizeof(int));
	if(arr == NULL)
	{
		printf("Malloc memory failed!\n");
		exit(-1);
	}
	for(int i=0;i<count;++i)
		*(arr+i) = rand() % 100;
	printf("Before quick sort,the arr is:\n");
	print(arr,count);
	quick_sort(arr,0,count-1);
	printf("After quick sort,the arr is:\n");
	print(arr,count);
	for(int i=0;i<count;++i)
		*(arr+i) = rand() % 100;
	printf("Before random quick sort,the arr is:\n");
	print(arr,count);
	random_quick_sort(arr,0,count-1);
	printf("After random quick sort,the arr is:\n");
	print(arr,count);
	for(int i=0;i<count;++i)
		*(arr+i) = rand() % 100;
	printf("Before tail recursion quick sort,the arr is:\n");
	print(arr,count);
	quick_sort_by_tail_recursion(arr,0,count-1);
	printf("After tail recursion quick sort,the arr is:\n");
	print(arr,count);
	free(arr);
}

// 对比基本快速排序与随机版本快速排序的性能
void time_test(void)
{
	int num;
	printf("Please input the random numbers count: ");
	scanf("%d",&num);
	int *arr1 = (int*)malloc(num*sizeof(int));
	int *arr2 = (int*)malloc(num*sizeof(int));
	if(arr1 == NULL || arr2 == NULL)
	{
		printf("Malloc memory failed!\n");
		if(arr1)
			free(arr1);
		if(arr2)
			free(arr2);
		exit(-1);
	}
	for(int i=0;i<num;++i)
		*(arr1+i) = rand() % 1000;
	// 从 arr1 复制到 arr2
	memcpy(arr2,arr1,sizeof(int)*num);
	clock_t t1,t2;
	t1 = clock();
	quick_sort_by_tail_recursion(arr1,0,num-1);
	t2 = clock();
	printf("sort %d random numbers by quick sort costs %.3f seconds.\n",num,(double)(t2-t1)/CLOCKS_PER_SEC);
	t1 = clock();
	random_quick_sort(arr2,0,num-1);
	t2 = clock();
	printf("sort %d random numbers by random quick sort costs %.3f seconds.\n",num,(double)(t2-t1)/CLOCKS_PER_SEC);
}
