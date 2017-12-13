/*
Q2:
   把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
*/
#include<iostream>
#include<vector>
#include<cassert>
using namespace std;
inline int min(int x,int y){return x>y ? y:x;}
// 输入输出
void input();
// 求第N个丑数
int solve_ugly(int N);
// 测试函数
void solve_ugly_test();

int main(void)
{
	solve_ugly_test();
	input();
	return 0;
}

// 求第N个丑数
int solve_ugly(int N)
{
	// p1,p2,p3 保存的分别是第一个乘以2，乘以3，乘以5大于当前最后一个丑数
	// 数字的索引
	int index2,index3,index5,next;
	index2 = 3;
	index3 = 2;
	index5 = 2;
	// v 用于保存丑数
	vector<int> v = {1,2,3,4,5};
	if(N > 5)
	{
		int index = 5;
		while(index < N)
		{
			// 下一个丑数
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
