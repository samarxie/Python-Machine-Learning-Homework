/*
�������������
*/
#include<iostream>
#include<vector>
#include<cassert>
using namespace std;
const int INF = 1e8;

// ������������
int find_max_sum(const vector<int> &v);
// ��������
void input(void);
// ���Ժ���
void find_max_sum_test();

int main(void)
{
	//find_max_sum_test();
	input();
	return 0;
}

void input(void)
{
	cout<<"Please input the numbers count:";
	int count;
	cin>>count;
	cout<<"Please input "<<count<<" numbers:"<<endl;
	vector<int> v(count);
	for(int i=0;i<count;++i)
		cin>>v[i];
	int max_sum;
	max_sum = find_max_sum(v);
	cout<<"The concret max sum is:"<<max_sum<<endl;
}

void find_max_sum_test()
{
	vector<int> v1 = {1,2,-4,3,-2,6,10};
	vector<int> v2 = {1,-10,3,4,-9,2,10};
	assert(find_max_sum(v1)==17);
	assert(find_max_sum(v2)==12);
}

int find_max_sum(const vector<int> &v)
{
	// ��ʼ������Ϊ������
	int max_sum = -INF;
	int sum = 0;
	for(auto x :v)
	{
		if(sum>=0)
			sum += x;
		else
			sum = x;
		if(sum > max_sum)
			max_sum = sum;
	}
	return max_sum;
}

