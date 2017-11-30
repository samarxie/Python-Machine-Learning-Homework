/*
Q3:输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，
则最小的4个数字是1,2,3,4,。
*/
#include<stdio.h>
#include<stdlib.h>
// 快排
void quick_sort(int *,int,int);
// 快排输出
void print_by_quicksort(int *,int,int);
// 冒泡排序输出
void print_by_bubblesort(int *,int,int);

int main(void)
{
	// 输入整数个数
	int count;
	printf("Please input the numbers count: ");
	scanf("%d",&count);
	// 开辟数组
	int *arr = (int*)malloc(sizeof(int)*count);
	if(arr == NULL)
	{
		printf("Malloc memory failed!\n");
		exit(EXIT_FAILURE);
	}
	printf("Please input %d numbers:\n",count);
	for(int i=0;i<count;++i)
		scanf("%d",arr+i);
	printf("Please input the minimize numbers count: ");
	int k;
	scanf("%d",&k);
	printf("The minimize %d numbers is(by quick sort):\n",k);
	print_by_quicksort(arr,count,k);
	printf("The minimize %d numbers is(by bubble sort):\n",k);
	print_by_bubblesort(arr,count,k);
	return 0;
}

void quick_sort(int *arr,int begin,int end)
{
	int i = begin;
	int j = end;
	if(i>=j)
		return;
	int key = arr[i];
	while(i < j)
	{
		while(i < j && arr[j]>=key)
			j--;
		arr[i] = arr[j];
		while(i < j && arr[i] <=key)
			++i;
		arr[j] = arr[i];
	}
	arr[i] = key;
	quick_sort(arr,begin,i-1);
	quick_sort(arr,i+1,end);
}

void print_by_quicksort(int *arr,int n,int k)
{
	if(n <=0 || k<=0 || k > n)
		return;
	quick_sort(arr,0,n-1);
	for(int i=0;i<k;++i)
		printf("%d ",arr[i]);
	printf("\n");
}

void print_by_bubblesort(int *arr,int n,int k)
{
	if(n <=0 || k<=0 || k > n)
		return;
	int temp;
	for(int i=0;i<k;++i)
	{
		for(int j=i+1;j<n;++j)
		{
			if(arr[j] < arr[i])
			{
				temp = arr[j];
				arr[j] = arr[i];
				arr[i] = temp;
			}
		}
		printf("%d ",arr[i]);
	}
	puts("");
}


