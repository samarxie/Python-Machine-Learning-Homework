/*
Q2:��1+2+3+...+n��Ҫ����ʹ�ó˳�����for��while��if��else��switch��case�ȹؼ��ּ������ж���䣨A?B:C����
---------
�ⷨ��:��������C++���캯���ۼ����
*/
#include<iostream>
#include<cassert>
using namespace std;
void output();
class Solve
{
	private:
		// sum ���ڼ�¼��
		static unsigned int sum;
		// n �����ۼ�
		static unsigned int n;
	public:
		// ���캯���ۼӺ�
		Solve(){++n;sum +=n;}
		// ���ó�Ա����
		void reset(){n=0;sum=0;}
		// �������sum��ֵ
		unsigned int get_sum(){return sum;}
};
unsigned int Solve::n = 0;
unsigned int Solve::sum = 0;
// ���Ժ���
void Solve_test();

int main(void)
{
	Solve_test();
	output();
	return 0;
}

// ���Ժ���
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
