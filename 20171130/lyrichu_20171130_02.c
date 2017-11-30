/*
�鲢����,�ο��ԡ��㷨���ۡ�
*/
#include<stdio.h>
#include<stdlib.h>
#include<time.h>
const int inf = 1e+8; // ����������
// �鲢���� 
void merge_sort(int *,int,int);
// ��������������ϲ�
void combine_merge(int *,int,int,int);
void print(int *,int);

int main(void)
{
	// ��ʼ�����������
	srand(time(0));
	printf("Please input the numbers count: ");
	// ������ָ���
	int count;
	scanf("%d",&count);
	int *arr = (int*)malloc(count*sizeof(int));
	if(arr == NULL)
	{
		printf("Malloc memory failed!\n");
		exit(-1);
	}
	// ���������
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
	// p Ϊ������ʼλ��,q ���м�λ��,r��ĩβλ��
	// ��Ҫ���븨������,ÿ������ĩβ����һ��λ����Ϊ��־λ
	int arr1[n1+1];
	int arr2[n2+1];
	for(i=0;i<n1;++i)
		arr1[i] = arr[p+i];
	arr1[n1] = inf;
	for(i=0;i<n2;++i)
		arr2[i] = arr[q+1+i];
	arr2[n2] = inf;
	// i,j �ֱ�������¼ arr1��arr2��λ��
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
	// �ݹ齫����������ֱ�����
	merge_sort(arr,begin,mid);
	merge_sort(arr,mid+1,end);
	// �ٺϲ�����������������
	combine_merge(arr,begin,mid,end);
}

void print(int *arr,int n)
{
	for(int i=0;i<n;++i)
		printf("%d ",*(arr+i));
	putchar('\n');
}
