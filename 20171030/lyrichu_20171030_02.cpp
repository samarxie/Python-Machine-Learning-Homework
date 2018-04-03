/*
Q2:
给定一个有n个正整数的数组A和一个整数sum,求选择数组A中部分数字和为sum的方案数。
当两种选取方案有一个数字的下标不一样,我们就认为是不同的组成方案。 
输入为两行:
第一行为两个正整数n(1 ≤ n ≤ 1000)，sum(1 ≤ sum ≤ 1000)
第二行为n个正整数A[i](32位整数)，以空格隔开。
输出所求的方案数 
*/
#include<iostream>
#include<cstdlib>
#include<cassert>
using namespace std;

// 求解方案,采用动态规划的思想
int solve(int arr[],int n,int sum);
// 测试函数
void solve_test();
// 输入输出函数
void input();

int main(void)
{
	//solve_test();
	input();
	return 0;
}

int solve(int arr[],int n,int sum)
{
	int (*solve_arr)[sum+1] = new int[n+1][sum+1];
	if(solve_arr == NULL)
	{
		cout<<"new memory failed!"<<endl;
		exit(EXIT_FAILURE);
	}
	for(int i=0;i<=n;++i)
		for(int j=0;j<=sum;++j)
			solve_arr[i][j] = 0;
	// 和为0
	for(int i=0;i<=n;++i)
		solve_arr[i][0] = 1;
	for(int i=1;i<=n;++i)
	{
		for(int j=0;j<=sum;++j)
		{
			if(arr[i-1] <=j)
				solve_arr[i][j] = solve_arr[i-1][j] + solve_arr[i-1][j-arr[i-1]];
			else
				solve_arr[i][j] = solve_arr[i-1][j];
		}
	}
	int res = solve_arr[n][sum];
	delete [] solve_arr;
	return res;
}

void solve_test()
{
	int arr1[5] = {1,2,3,3,2};
	int arr2[4] = {2,4,3,5};
	assert(solve(arr1,5,4) == 3);
	assert(solve(arr2,4,5) == 2);
}

void input()
{
	cout<<"Please input the numbers count and the sum:";
	int count,sum;
	cin>>count>>sum;
	cout<<"Please input "<<count<<" numbers:"<<endl;
	int *arr = new int[count];
	if(arr == NULL)
	{
		cout<<"new memory failed!"<<endl;
		exit(EXIT_FAILURE);
	}
	for(int i=0;i<count;++i)
		cin>>arr[i];
	int total = solve(arr,count,sum);
	cout<<"The total solution counts is:"<<total<<endl;
	delete [] arr;
}