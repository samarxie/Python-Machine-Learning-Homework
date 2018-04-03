/*
Q2:
   ��ֻ��������2��3��5��������������Ugly Number��������6��8���ǳ�������14���ǣ���Ϊ����������7��
ϰ�������ǰ�1�����ǵ�һ���������󰴴�С�����˳��ĵ�N��������
*/
#include<iostream>
#include<vector>
#include<cassert>
using namespace std;
inline int min(int x,int y){return x>y ? y:x;}
// �������
void input();
// ���N������
int solve_ugly(int N);
// ���Ժ���
void solve_ugly_test();

int main(void)
{
	solve_ugly_test();
	input();
	return 0;
}

// ���N������
int solve_ugly(int N)
{
	// p1,p2,p3 ����ķֱ��ǵ�һ������2������3������5���ڵ�ǰ���һ������
	// ���ֵ�����
	int index2,index3,index5,next;
	index2 = 3;
	index3 = 2;
	index5 = 2;
	// v ���ڱ������
	vector<int> v = {1,2,3,4,5};
	if(N > 5)
	{
		int index = 5;
		while(index < N)
		{
			// ��һ������
			next = min(min(2*v[index2-1],3*v[index3-1]),5*v[index5-1]);
			v.push_back(next);
			++index;
			while(2*v[index2-1]<=next)
				++index2;
			while(3*v[index3-1]<=next)
				++index3;
			while(5*v[index5-1]<=next)
				++index5;
		}
	}
	return v[N-1];
}

void solve_ugly_test()
{
	vector<int> ugly = {1,2,3,4,5,6,8,9,10,12,15,16,18,20};
	assert(solve_ugly(1)==ugly[0]);
	assert(solve_ugly(5)==ugly[4]);
	assert(solve_ugly(9)==ugly[8]);
	assert(solve_ugly(13)==ugly[12]);
}

void input()
{
	cout<<"Please input the ugly number index:";
	int N;
	cin>>N;
	cout<<"The "<<N<<" ugly number is "<<solve_ugly(N)<<endl;
}
