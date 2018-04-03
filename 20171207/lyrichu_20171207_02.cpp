/*
Q2:
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
输出描述:
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
*/
#include<iostream>
#include<vector>
#include<cassert>
#include<algorithm>
using namespace std;
void output();
// 得到和为s的所有连续序列，序列存放在 v中
void get_sums_series(int s,vector<vector<int>> &v);
// 测试函数
void get_sums_series_test();

int main()
{
	get_sums_series_test();
	output();
	return 0;
}

// 得到和为s的所有连续序列，序列存放在 v中
void get_sums_series(int s,vector<vector<int>> &v)
{
	if(s <=0)
		return;
	int current = 1;
	vector<int> v1(1,current);
	while(v1[0] <= s/2)
	{
		if(accumulate(v1.begin(),v1.end(),0) < s)
		{
			current++;
			v1.push_back(current);
		}
		else if(accumulate(v1.begin(),v1.end(),0) > s)
			v1.erase(v1.begin()); // 删除第一个元素
		else
		{
			v.push_back(v1); // 注意这里添加的是拷贝而不是引用
			v1.erase(v1.begin());
		}
	}
}

// 测试函数
void get_sums_series_test()
{
	// 10 = 1 + 2 + 3 + 4
	// 20 = 2 + 3 + 4 + 5 + 6
	// 4 没有
	vector<vector<int>> v;
	get_sums_series(10,v);
	vector<int> v1 = {1,2,3,4};
	assert(v.size()==1 && v[0] == v1);
	v.clear();
	get_sums_series(20,v);
	v1 = {2,3,4,5,6};
	assert(v.size()==1 && v[0] == v1);
	v.clear();
	get_sums_series(4,v);
	assert(v.size()==0);
}

// 输出 
void output()
{
	cout<<"Please input the a positive number:";
	int number;
	cin>>number;
	vector<vector<int>> v;
	get_sums_series(number,v);
	for(int i=0;i<v.size();++i)
	{
		cout<<number<<"=";
		for(int j=0;j<v[i].size()-1;++j)
		{
			cout<<v[i][j]<<"+";
		}
		cout<<v[i].back()<<endl;
	}
}

