/*
Q2����һ���ַ���(1<=�ַ�������<=10000��ȫ������ĸ���)
���ҵ���һ��ֻ����һ�ε��ַ�,����������λ��
*/
#include<iostream>
#include<list>
#include<string>
#include<algorithm>
using namespace std;

int main(void)
{
	cout<<"Please input some alphabets:\n";
	// ������ĸ
	list<char> li;
	string s;
	getline(cin,s);
	for(auto x:s)
	{
		auto pos = find(li.begin(),li.end(),x);
		// û�ҵ��ַ� x 
		if(pos == li.end())
		{
			li.push_back(x);
		}
		else
		{
			li.remove(x);
		}
	}
	if(li.empty())
		cout<<"There is not an alphabet that occurs only once!\n";
	else
		cout<<"The first alphabet that occurs only once is:"<<*li.begin()<<endl;
	return 0;
}