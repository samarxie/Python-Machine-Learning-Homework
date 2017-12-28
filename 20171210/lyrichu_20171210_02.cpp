/*
Q2:
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，
但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。
 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
---------------------
开一个辅助数组作为hash表。
*/
#include<stdio.h>
#include<stdlib.h>
#include<assert.h>
#include<string.h>
int find_first_reapeat_once(int *arr,int n);
void find_first_reapeat_once_test();
void output();

int main(void)
{
	find_first_reapeat_once_test();
	output();
	return 0;
}

int find_first_reapeat_once(int *arr,int n)
{
	if(arr==NULL || n<=1)
		return -1;
	int *hash;
	if((hash = (int*)malloc(sizeof(int)*n))==NULL)
	{
		fprintf(stderr,"Malloc memory failed!\n");
		exit(-1);
	}
	// 将 hash 元素初始化为0
	for(int i=0;i<n;++i)
		hash[i] = 0;
	for(int i=0;i<n;++i)
	{
		if(arr[i]>=n || arr[i] < 0)
		{
			fprintf(stderr,"The array's number must be none negative less than %d and \n",n);
			exit(-1);
		}
		++hash[arr[i]];
		if(hash[arr[i]]==2)
			return arr[i];
	}
	free(hash);
	return -1;
}

// 测试 
void find_first_reapeat_once_test()
{
	int arr1[6] = {1,2,2,4,4,3};
	int arr2[5] = {1,2,3,4,1};
	int arr3[] = {1};
	assert(find_first_reapeat_once(NULL,0)==-1);
	assert(find_first_reapeat_once(arr1,6)==2);
	assert(find_first_reapeat_once(arr2,5)==1);
	assert(find_first_reapeat_once(arr3,1)==-1);
}

void output()
{
	puts("How many numbers do you want to input:");
	int num;
	scanf("%d",&num);
	int *arr;
	if(num <= 0 || (arr = (int*)calloc(num,sizeof(int)))==NULL)
		exit(-1);
	printf("Please input %d numbers between 0 and %d:\n",num,num-1);
	for(int i=0;i<num;++i)
		scanf("%d",arr+i);
	int n = find_first_reapeat_once(arr,num);
	if(n>=0)
		printf("The first repeat number is %d\n",n);
	else
		puts("There is no repeat numbers!");
	free(arr);
}

