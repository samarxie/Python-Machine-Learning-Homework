/*
Q1:
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，
他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： 
{[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}，
 {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
 -----------------思路----------------------
 本题可以采用两端开口的队列(C++里的deque)实现
*/
#include<iostream>
#include<vector>
#include<deque>
#include<cassert>
#include<cstddef>
using namespace std;
// 求滑动窗口的最大值
vector<int> max_int_windows(const vector<int> &v,size_t size);
// 测试函数
void test();
int main(void)
{
	test();
	return 0;
}

// 求滑动窗口的最大值
vector<int> max_int_windows(const vector<int> &v,size_t size)
{
	vector<int> maxIntWindows;
	if(size <= v.size() && size >=1)
	{
		deque<int> index;
		for(size_t i=0;i<size;++i)
		{
			while(!index.empty() && v[i] > v[index.back()])
				index.pop_back();
			index.push_back(i);
		}
		for(size_t i= size;i<v.size();++i)
		{
			maxIntWindows.push_back(v[index.front()]);
			while(!index.empty() && v[i] > v[index.back()])
				index.pop_back();
			while(!index.empty() && index.front() <=i-size)
				index.pop_front();
			index.push_back(i);
		}
		maxIntWindows.push_back(v[index.front()]);
	}
	return maxIntWindows;
}

void test()
{
	vector<int> v = {2,3,4,2,6,2,5,1};
	size_t size = 3;
	vector<int> maxIntWindows = max_int_windows(v,size);
	vector<int> tmp = {4,4,6,6,6,5};
	assert(maxIntWindows == tmp);
	cout<<"Test 1 succeed!"<<endl;
	size = 2;
	maxIntWindows = max_int_windows(v,size);
	tmp = {3,4,4,6,6,5,5};
	assert(maxIntWindows == tmp);
	cout<<"Test 2 succeed!"<<endl;
}
