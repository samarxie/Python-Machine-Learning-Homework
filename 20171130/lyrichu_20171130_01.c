/*
插入排序
*/
#include<stdio.h>
#include<time.h>
#include<stdlib.h>
// 插入排序 
void insert_sort(int *,int);
void print(int *,int);
int main(void)
{
	srand(time(0));
	printf("Please input the numbers count: ");
	// 随机产生整数个数
	int count;
	scanf("%d",&count); 
	int *arr = (int*)calloc(count,sizeof(int));
	if(arr == NULL)
	{
		printf("Alloc memory failed!");
		exit(EXIT_FAILURE);
	}
	// 利用随机数填充数组
	for(int i=0;i<count;++i)
		*(arr+i) = rand() % 100;
	printf("Before insert sort,the arr is:\n");
	print(arr,count);
	insert_sort(arr,count);
	printf("After insert sort,the arr is:\n");
	print(arr,count);
	// 释放内存
	free(arr);
	return 0;
}

void insert_sort(int *arr,int n)
{
	int i,j,target;
	if(n <= 1)
		return;
	else
	{
		for(j=1;j<n;++j)
		{
			// 待插入目标值
			target = arr[j];
			i = j-1;
			while(i >=0 && arr[i] > target)
			{
				arr[i+1] = arr[i];
				--i;
			}
			arr[i+1] = target;	
		}
	}	
}

void print(int *arr,int n)
{
	for(int i=0;i<n;++i)
		printf("%d ",*(arr+i));
	printf("\n");
}
