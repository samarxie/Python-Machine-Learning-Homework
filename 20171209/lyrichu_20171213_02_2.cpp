/*
Q2:求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
---------
解法二:可以利用C++构造函数累加求解
*/
#include<iostream>
#include<cassert>
using namespace std;
void output();
class Solve
{
	private:
		// sum 用于记录和
		static unsigned int sum;
		// n 用于累加
		static unsigned int n;
	public:
		// 构造函数累加和
		Solve(){++n;sum +=n;}
		// 重置成员变量
		void reset(){n=0;sum=0;}
		// 返回求和sum的值
		unsigned int get_sum(){return sum;}
};
unsigned int Solve::n = 0;
unsigned int Solve::sum = 0;
// 测试函数
void Solve_test();

int main(void)
{
	Solve_test();
	output();
	return 0;
}

// 测试函数
void Solve_test()
{
	Solve *p = new Solve;
	p->reset();
	delete [] p;
	p = new Solve[3]; // 1+2+3
	assert(p->get_sum()==(1+2+3));
	delete [] p;
	p = new Solve;
	p->reset();
	delete [] p;
	p = new Solve[5]; // 1+2+3+4+5
	assert(p->get_sum()==(1+2+3+4+5));
	delete [] p;
	p = new Solve;
	p->reset();
	delete [] p;
	p = new Solve[10]; // 1+2+3+4+5+..+10
	assert(p->get_sum()==55);
	delete [] p;
}

void output()
{
	cout<<"Please input a positive number:";
	int number;
	cin>>number;
	Solve *p = new Solve;
	p->reset();
	delete []p;
	p = new Solve[number];
	cout<<"Accumulate from 0 to "<<number<<" is "<<p->get_sum()<<endl;
	delete []p;
}
