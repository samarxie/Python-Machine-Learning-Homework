/*
Q1：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
*/
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;
// 自定义排序规则
string to_string(int);

bool comp(const int &,const int &);

int main(void)
{
	cout<<"Please input the numbers count: ";
	int count;
	cin>>count;
	cout<<"Please input some numbers: ";
	vector<int> v(count);
	for(int i=0;i<count;++i)
		cin>>v[i];
	// 按照 comp 规则排序
	sort(v.begin(),v.end(),comp);
	cout<<"The minimize number is: ";
	for(auto x:v)
		cout<<x;
	cout<<endl;
	return 0;
}

bool comp(const int &a,const int &b)
{
	return to_string(a) + to_string(b) < to_string(b) + to_string(a);
}

string to_string(int n)
{
	string s("");
	while(n)
	{
		char c = n % 10;
		s = c + s;
		n /= 10;
	}
	return s;
}

