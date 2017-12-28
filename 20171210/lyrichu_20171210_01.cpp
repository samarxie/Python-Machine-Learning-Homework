/*
Q1:
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 
数值为0或者字符串不是一个合法的数值则返回0
*/
#include<iostream>
#include<cassert>
#include<string>
#include<cctype>
using namespace std;
// IS_VALID_NUMBER 这全局变量用于判断字符串是否成功转化为整数
bool IS_VALID_NUMBER = true;
void output();
// 字符串转整数
int str_to_int(const string &s);
// 测试函数
void str_to_int_test();

int main(void)
{
	str_to_int_test();
	output();
	return 0;
}

int str_to_int(const string &s)
{
	if(s.size()==0)
		return 0;
	// c 用于记录数字符号(正数还是负数)
	// n 用于记录当前值
	int c,n;
	if(s[0] == '-' || s[0] == '+')
	{
		if(s.size()==1)
		{
			IS_VALID_NUMBER = false;
			return 0;
		}
		c = s[0]=='-'?-1:1;
		n = 0;
	}
	else if(isdigit(s[0]))
	{
		n = s[0]-'0';
		c = 1;
	}
	else
	{
		IS_VALID_NUMBER = false;
		return 0;
	}
	for(int i=1;i<s.size();++i)
	{
		if(!isdigit(s[i]))
		{
			IS_VALID_NUMBER = false;
			return 0;
		}
		n *= 10;
		n += s[i]-'0';
	}
	IS_VALID_NUMBER = true;
	return c*n;
}

// 测试函数
void str_to_int_test()
{
	assert(str_to_int("-23")==-23);
	assert(str_to_int("+")==0);
	assert(IS_VALID_NUMBER==false);
	assert(str_to_int("+012")==12);
	assert(IS_VALID_NUMBER==true);
	assert(str_to_int("3412")==3412);
}

void output()
{
	cout<<"Please input a number string:";
	string s;
	getline(cin,s);
	int n = str_to_int(s);
	if(IS_VALID_NUMBER)
		cout<<"Convert string to number succeed,the number is "<<n<<endl;
	else
		cerr<<s<<" can't convert to a number!"<<endl;
}




