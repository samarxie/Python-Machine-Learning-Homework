/*
*date    : 2018-04-09 22:00:16
*author  : lyrichu
*email   :919987476@qq.com
*link    : https://www.github.com/Lyrichu
*version : 0.1
*description:
*(暴力枚举)输入正整数n,按从小到大的顺序输出所有形如abcde/fghij=n的
表达式,其中a~j恰好是数字0-9的一个排列(可以有前导０),2<=n<=79
样例输入:
62
样例输出:
79546/01283 = 62
94736/01528 = 62
*/
#include <set>
#include <iostream>
#include <string>
using namespace std;

bool legal1(int n);
bool legal2(int m,int n,string &str);

int main(int argc, char const *argv[])
{
	int n,i,j;
	cin>>n;
	// 枚举fghij
	for(i=1;i<99999;++i)
	{
		if(legal1(i))
		{
			if(i%n == 0)
			{
				j = i/n;
				string s;
				if(legal2(i,j,s))
				{
					cout<<i<<"/"<<s<<"="<<n<<endl;
				}
			}
		}
	}
	return 0;
}

bool legal1(int n)
{
	set<int> s;
	int d;
	while(n)
	{
		d = n % 10;
		s.insert(d);
		n = (n-d)/10;
	}
	return s.size() == 5;
}

bool legal2(int m,int n,string &str)
{
	set<int> s;
	int d;
	while(n)
	{
		d = n % 10;
		s.insert(d);
		str = char('0'+d)+str;
		n = (n-d)/10;
	}
	while(m)
	{
		d = m % 10;
		s.insert(d);
		m = (m-d)/10;
	}
	if(s.size()==10)
		return true;
	if(s.size()==9 && s.find(0) == s.end())
	{
		str = '0' + str;
		return true;
	}
	return false;
}