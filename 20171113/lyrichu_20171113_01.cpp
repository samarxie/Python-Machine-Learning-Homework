/*
Q1������һ�����������飬����������������ƴ�������ų�һ������
��ӡ��ƴ�ӳ���������������С��һ����
������������{3��32��321}�����ӡ���������������ųɵ���С����Ϊ321323��
*/
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;
// �Զ����������
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
	// ���� comp ��������
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

