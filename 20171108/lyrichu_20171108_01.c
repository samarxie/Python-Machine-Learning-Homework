/*
Q1：
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
*/
#include<stdio.h>
#include<stdlib.h>
// 调整数组数字顺序
void exchange(int *arr1,int *arr2,int n);

int main(void)
{
	printf("Please input the array length:");
	int len;
	scanf("%d",&len);
	printf("Please input the array numbers:");
	// 为数组分配内存
	int *arr1 = (int*)malloc(len*sizeof(int));
	// arr2 存储调整之后的整数
	int *arr2 = (int*)malloc(len*sizeof(int));
	if(arr1==NULL || arr2 == NULL)
	{
		printf("Malloc memory failed!\n");
		exit(-1);
	}
	// 数组填充
	for(int i=0;i<len;++i)
		scanf("%d",arr1+i);
	exchange(arr1,arr2,len);
	printf("After exchange,the array is:\n");
	for(int i=0;i<len;++i)
		printf("%d ",*(arr2+i));
	puts("");
	free(arr1);
	free(arr2);
	return 0;
}

// 调整数组数字顺序
void exchange(int *arr1,int *arr2,int n)
{
	// 首先求奇数个数
	int odd = 0;
	for(int i=0;i<n;++i)
	{
		if(arr1[i] % 2 == 1)
			odd++;
	}
	// 将arr1的数字填充到arr2,奇数从0开始填充，偶数从odd位置开始填充
	// 奇数起始位置
	int index_odd = 0;
	// 偶数起始位置
	int index_even = odd;
	for(int i=0;i<n;++i)
	{
		// 如果是奇数
		if(arr1[i] % 2)
			arr2[index_odd++] = arr1[i];
		else
			arr2[index_even++] = arr1[i];
	}
}
