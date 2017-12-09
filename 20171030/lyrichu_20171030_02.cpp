/*
Q2:
����һ����n��������������A��һ������sum,��ѡ������A�в������ֺ�Ϊsum�ķ�������
������ѡȡ������һ�����ֵ��±겻һ��,���Ǿ���Ϊ�ǲ�ͬ����ɷ����� 
����Ϊ����:
��һ��Ϊ����������n(1 �� n �� 1000)��sum(1 �� sum �� 1000)
�ڶ���Ϊn��������A[i](32λ����)���Կո������
�������ķ����� 
*/
#include<iostream>
#include<cstdlib>
#include<cassert>
using namespace std;

// ��ⷽ��,���ö�̬�滮��˼��
int solve(int arr[],int n,int sum);
// ���Ժ���
void solve_test();
// �����������
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
	// ��Ϊ0
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