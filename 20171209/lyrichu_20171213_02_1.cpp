/*
Q2:求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
---------
解法一:可以利用函数指针求解
*/
#include<iostream>
#include<cassert>
using namespace std;
// 定义一个函数指针
typedef unsigned int (*f)(unsigned int);
void output();
// 控制递归结束的函数一
unsigned int f1(unsigned int);
// 主递归函数二
unsigned int solve(unsigned int n);
// 测试函数
void solve_test();

int main(void)
{
	solve_test();
	output();
	return 0;
}

// 控制递归结束的函数一
unsigned int f1(unsigned int n)
{
	return 0;
}

// 主递归函数二
unsigned int solve(unsigned int n)
{
	// 定义一个函数指针数组
	f arr[2] = {f1,solve};
	// 注意 !!0=0,!!n = 1,n不等于0
	return n + arr[!!n](n-1);
}

void solve_test()
{
	assert(solve(0)==0);
	assert(solve(3)==6);
	assert(solve(5)==15);
	assert(solve(10)==55);
}

void output()
{
	int number;
	cout<<"Please input a positive number:";
	cin>>number;
	if(number < 0)
		return;
	cout<<"Accumulate from 0 to "<<number<<" is "<<solve(number)<<endl;
}
