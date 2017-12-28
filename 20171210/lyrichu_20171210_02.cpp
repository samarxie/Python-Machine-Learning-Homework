/*
Q2:
��һ������Ϊn����������������ֶ���0��n-1�ķ�Χ�ڡ� ������ĳЩ�������ظ��ģ�
����֪���м����������ظ��ġ�Ҳ��֪��ÿ�������ظ����Ρ����ҳ�����������һ���ظ������֡�
 ���磬������볤��Ϊ7������{2,3,1,0,2,5,3}����ô��Ӧ������ǵ�һ���ظ�������2��
---------------------
��һ������������Ϊhash��
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
	// �� hash Ԫ�س�ʼ��Ϊ0
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

// ���� 
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

