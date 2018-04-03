/*
Q2:(数字拆解)
3 = 2+1 = 1+1+1，所以3一共有三种拆解的方式
4 = 3+1 = 2+2 = 2+1+1 = 1+1+1+1 共有5种拆法
输入一个正整数N，输出拆解的总数
例:
输入:3
输出:
3
------------
分析:
设 f(n,m) 为数字n分解方式中所有数字都不超过m的分解总数
则 (1) n=1 或 m=1 时 f(n,m) = 1
   (2) 当 m >n时,f(n,m) = f(n,n)
   (3) m = n 时,f(n,n) = 1 + f(n,n-1)
   (4) m < n 时,f(n,m) = f(n,m-1) + f(n-m,m)
*/
#include<iostream>
#include<cassert>
using namespace std;

void output();
// 数字n拆解个数,最大不超过m(递归解法)
int number_slice_recursion(int n,int m);
// 拆解的动态规划解法
int number_slice_dp(int n);
// 测试函数
void number_slice_recursion_test();
void number_slice_dp_test();

int main(void)
{
	number_slice_recursion_test();
	number_slice_dp_test();
	output();
	return 0;
}

void output()
{
	cout<<"Please input a positive number:";
	int number;
	cin>>number;
	cout<<"By dp method,there are "<<number_slice_dp(number)<<" ways to slice "<<number<<endl;
	cout<<"By recursion method,there are "<<number_slice_recursion(number,number)<<" ways to slice "<<number<<endl;
}

// 递归解法
int number_slice_recursion(int n,int m)
{
	if(n==1 || m==1)
		return 1;
	if(m > n)
		return number_slice_recursion(n,n);
	if(m==n)
		return 1 + number_slice_recursion(n,n-1);
	if(m < n)
		return number_slice_recursion(n,m-1) + number_slice_recursion(n-m,m);
}

// 动态规划解法
int number_slice_dp(int n)
{
	int arr[n+1][n+1];
	for(int i=1;i<=n;++i)
	{
		for(int j=1;j<=n;++j)
		{
			if(i==1 || j==1)
				arr[i][j] = 1;
			else if(j < i)
				arr[i][j] = arr[i][j-1] + arr[i-j][j];
			else if(i == j)
				arr[i][j] = 1 + arr[i][i-1];
			else if(i < j)
				arr[i][j] = arr[i][i];
		}
	}
	return arr[n][n];
}

// 测试函数
void number_slice_recursion_test()
{
	assert(number_slice_recursion(3,3)==3);
	assert(number_slice_recursion(4,4)==5);
}

void number_slice_dp_test()
{
	assert(number_slice_dp(3)==3);
	assert(number_slice_dp(4)==5);
}


