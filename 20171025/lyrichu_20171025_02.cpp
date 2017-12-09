/*
Q2:
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity. 
*/
#include<iostream>
#include<cassert>
#include<cstdlib>
using namespace std;
// 合并两个有序数组
void merge_two(int *arr1,int n1,int *arr2,int n2,int *arr_merge,int n);
void merge_two_test();
// 输入输出函数
void input();

int main(void)
{
	merge_two_test();
	input();
	return 0;
}

// 合并两个有序数组
// arr1:第一个数组
// arr2:第二个数组
// n1: 第一个数组长度
// n2: 第二个数组长度
// arr_merge:合并以后数组
// n 合并以后数组长度
void merge_two(int *arr1,int n1,int *arr2,int n2,int *arr_merge,int n)
{
	// i,j,k分别指向arr1与arr2,arr_merge
	int i,j,k;
	i = j = k = 0;
	while(i <n1 && j < n2)
	{
		if(arr1[i] < arr2[j])
		{
			arr_merge[k] = arr1[i];
			++i;
		}
		else
		{
			arr_merge[k] = arr2[j];
			++j;
		}
		++k;	
	}
	if(i == n1)
	{
		while(j < n2)
			arr_merge[k++] = arr2[j++];
	}
	else
	{
		while(i < n1)
			arr_merge[k++] = arr1[i++];
	}
}

// 测试函数
void merge_two_test()
{
	int arr1[4] = {1,3,5,6};
	int arr2[5] = {2,3,6,7,9};
	int arr3[9];
	merge_two(arr1,4,arr2,5,arr3,9);
	assert(arr3[0]==1);
	assert(arr3[3]==3);
	assert(arr3[6]==6);
	assert(arr3[8]==9);
}

void input()
{
	int count1,count2;
	cout<<"Please input the array1,array2 count:";
	cin>>count1>>count2;
	int *arr1 = new int[count1];
	int *arr2 = new int[count2];
	int *arr_merge = new int[count1+count2];
	if(arr1==NULL || arr2 == NULL || arr_merge == NULL)
	{
		cout<<"New memory failed!"<<endl;
		exit(-1);
	}
	cout<<"Please input "<<count1<<" numbers of array1:"<<endl;
	for(int i=0;i<count1;++i)
		cin>>arr1[i];
	cout<<"Please input "<<count2<<" numbers of array2:"<<endl;
	for(int i=0;i<count2;++i)
		cin>>arr2[i];
	merge_two(arr1,count1,arr2,count2,arr_merge,count1+count2);
	cout<<"After merge,the array is:"<<endl;
	for(int i=0;i<count1+count2;++i)
		cout<<arr_merge[i]<<" ";
	cout<<endl;
	delete [] arr1;
	delete [] arr2;
	delete [] arr_merge;
}
