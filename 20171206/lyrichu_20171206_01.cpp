/*
Q1:统计一个数字在排序数组中出现的次数。
思路:由于数组是排序的,某一个数字如果出现多次,那么一定是相邻的。
常规做法是顺序搜索，找到该数字第一次出现的位置，和最后一次出现的位置
然后统计出现次数。
高效的做法是利用二分法，随机找到该数字出现的位置，然后分别向前后搜索，找到该数字第一次以及
最后一次出现的位置，然后统计出现次数。
*/
#include<iostream>
#include<cassert>
#include<cstdlib>
using namespace std;
// 统计数字出现次数
int find_counts(int *arr,int N,int target);
// 测试函数
void find_counts_test();
// 输入输出
void output();

int main(void)
{
	find_counts_test();
	output();
	return 0;
}

int find_counts(int *arr,int N,int target)
{
	int begin = 0;
	int end = N-1;
	int mid;
	while(begin <= end)
	{
		mid = (begin+end)/2;
		if(arr[mid] < target)
			begin = mid+1;
		else if(arr[mid] > target)
			end = mid-1;
		else
			break;
	}
	// 没有找到
	if(begin>end)
		return 0;
	begin = end = mid;
	while(begin >= 0 && arr[begin] == target)
		begin--;
	begin++;
	while(end < N && arr[end] == target)
		end++;
	end--;
	return end - begin + 1;
}

void find_counts_test()
{
	int arr1[5] = {1,2,3,4,4};
	int arr2[1] = {10};
	int arr3[6] = {1,1,1,1,1,1};
	int arr4[6] = {5,5,7,8,8,8};
	assert(find_counts(arr1,5,4)==2);
	assert(find_counts(arr2,1,10)==1);
	assert(find_counts(arr3,6,4)==0);
	assert(find_counts(arr4,6,5)==2);
}

void output()
{
	cout<<"Please input the array size:";
	int size;
	cin>>size;
	int *arr;
	while((arr=new int[size])==NULL)
	{
		cerr<<"New a memory failed!"<<endl;
		exit(-1);
	}
	cout<<"Please input "<<size<<" numbers:"<<endl;
	for(int i=0;i<size;++i)
		cin>>arr[i];
	cout<<"Please input the target:";
	int target;
	cin>>target;
	int count = find_counts(arr,size,target);
	cout<<"There are "<<count<<" number "<<target<<" in arr."<<endl;
	delete [] arr;
}


