/*
Q3:
题目描述
输入一个递增排序的数组(数字都是正数)和一个数字S，在数组中查找两个数，是的他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
输出描述:
对应每个测试案例，输出两个数，小的先输出。
-----------------
分析:两个数字的和一定，则仅当它们相等的时候乘积最大，且两个数字越相近越大。
由于输入是排序数组，则从第一个元素a[0]开始搜索,利用二分法在[a1]~a[n-1]之间搜索S-a[0]，
如果找到了则直接返回；否则下一个变为a[1],一直到a[n-2]为止。
*/
#include<iostream>
#include<cassert>
#include<cstdlib>
#include<algorithm>
using namespace std;
// 在 arr 中搜索和为s的两个数字,first 和 second 为 指向两个数字的指针
// 如果没有找到，则返回 false,找到返回true
bool find_sums(int *arr,int n,int s,int *first,int *second);
// 测试函数
void find_sums_test();
// 输出 
void output();

int main(void)
{
	find_sums_test();
	output();
	return 0;
}

// 在 arr 中搜索和为s的两个数字,first 和 second 为 指向两个数字的指针
// 如果没有找到，则返回 false,找到返回true
bool find_sums(int *arr,int n,int s,int *first,int *second)
{
	if(s <= 0 || s < 2*arr[0] || s > 2*arr[n-1])
		return false;
	// 当前搜索位置
	int current = 0;
	while(current < n-1)
	{
		if(arr[current] >= s)
			return false;
		if(binary_search(arr+current+1,arr+n,s-arr[current]))
		{
			*first = arr[current];
			*second = s-arr[current];
			return true;
		}
		current++;
	}
	return false;
}

// 测试函数
void find_sums_test()
{
	int arr1[5] = {1,2,3,4,5};
	int arr2[10] = {1,2,3,4,5,6,7,9,11,12};
	int first,second;
	first = second = 0;
	bool is_find;
	is_find = find_sums(arr1,5,5,&first,&second);
	assert(is_find && first==1 && second==4);
	is_find = find_sums(arr1,5,10,&first,&second);
	assert(!is_find);
	is_find = find_sums(arr2,10,13,&first,&second);
	assert(is_find && first==1 && second==12);
}

// 输出 
void output()
{
	cout<<"How many numbers do you want to input:";
	int count;
	cin>>count;
	int *arr;
	if((arr = new int[count]) == NULL)
	{
		cerr<<"New int array memory failed!"<<endl;
		exit(-1);
	}
	cout<<"Please input "<<count<<" positive numbers:"<<endl;
	for(int i=0;i<count;++i)
		cin>>arr[i];
	cout<<"Please input the target sum number:";
	int s;
	cin>>s;
	int *first = new int;
	int *second = new int;
	if(first == NULL || second == NULL)
	{
		cerr<<"New int memory failed!"<<endl;
		exit(-1);
	}
	bool is_find = find_sums(arr,count,s,first,second);
	if(is_find)
		cout<<s<<"="<<*first<<"+"<<*second<<endl;
	else
		cout<<"Can't find two numbers whose sum is "<<s<<endl;
	delete arr;
	delete first;
	delete second;
}
