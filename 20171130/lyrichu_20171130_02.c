/*
归并排序,参考自《算法导论》
*/
#include<stdio.h>
#include<stdlib.h>
#include<time.h>
const int inf = 1e+8; // 近似正无穷
// 归并排序 
void merge_sort(int *,int,int);
// 将两个有序数组合并
void combine_merge(int *,int,int,int);
void print(int *,int);

int main(void)
{
	// 初始化随机数种子
	srand(time(0));
	printf("Please input the numbers count: ");
	// 随机数字个数
	int count;
	scanf("%d",&count);
	int *arr = (int*)malloc(count*sizeof(int));
	if(arr == NULL)
	{
		printf("Malloc memory failed!\n");
		exit(-1);
	}
	// 产生随机数
	for(int i=0;i<count;++i)
		*(arr+i) = rand() % 100;
	printf("Before merge sort,the arr is:\n");
	print(arr,count);
	merge_sort(arr,0,count-1);
	printf("After merge sort,the arr is:\n");
	print(arr,count);
	free(arr);
	return 0;
}

void combine_merge(int *arr,int p,int q,int r)
{
	if(p>=r)
		return;
	int n1 = q-p+1;
	int n2 = r-q;
	int i,j,k;
	// p 为数组起始位置,q 是中间位置,r是末尾位置
	// 需要引入辅助数组,每个数组末尾多留一个位置作为标志位
	int arr1[n1+1];
	int arr2[n2+1];
	for(i=0;i<n1;++i)
		arr1[i] = arr[p+i];
	arr1[n1] = inf;
	for(i=0;i<n2;++i)
		arr2[i] = arr[q+1+i];
	arr2[n2] = inf;
	// i,j 分别用来记录 arr1和arr2的位置
	i = j = 0;
	for(k=p;k<=r;++k)
	{
		if(arr1[i] < arr2[j])
		{
			arr[k] = arr1[i++];
		}
		else
		{
			arr[k] = arr2[j++];
		}
	}
}

void merge_sort(int *arr,int begin,int end)
{
	if(begin >= end)
		return;
	int mid = (begin+end)/2;
	// 递归将两个子数组分别排序
	merge_sort(arr,begin,mid);
	merge_sort(arr,mid+1,end);
	// 再合并排序后的两个子数组
	combine_merge(arr,begin,mid,end);
}

void print(int *arr,int n)
{
	for(int i=0;i<n;++i)
		printf("%d ",*(arr+i));
	putchar('\n');
}
