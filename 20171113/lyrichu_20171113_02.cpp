/*
Q2：在一个字符串(1<=字符串长度<=10000，全部由字母组成)
中找到第一个只出现一次的字符,并返回它的位置
*/
#include<iostream>
#include<list>
#include<string>
#include<algorithm>
using namespace std;

int main(void)
{
	cout<<"Please input some alphabets:\n";
	// 保存字母
	list<char> li;
	string s;
	getline(cin,s);
	for(auto x:s)
	{
		auto pos = find(li.begin(),li.end(),x);
		// 没找到字符 x 
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