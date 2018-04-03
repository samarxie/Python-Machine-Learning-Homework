/*
Q1：
汇编语言中有一种移位指令叫做循环左移（ROL），
现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。
是不是很简单？OK，搞定它！
----------------
如果要用string的话，那太简单了，取前K个子字符串，然后与后面的字符串拼接返回新的字符串
就可以了，但是显然这不是本题要考察的目的。一种不需要额外存储空间的做法是将字符串分割为
前k个字符和其余的字符，分别将这两部分反转，然后再将整个字符串反转即可，
比如 abc-->cba,XYZdef-->fedZYX,此时字符串为cbafedZYX,再反转一次，变为XYZdefabc
*/
#include<iostream>
#include<cassert>
#include<string>
using namespace std;
void output();
// 将字符串 str start 和 end 之间的字符序列反转
bool str_reverse(string &str,int start,int end);
// 将字符串 str 循环左移k位
bool str_left_move(string &str,int k);
// 测试函数
void str_reverse_test();
void str_left_move_test();
// 输出
void output();

int main(void)
{
	str_reverse_test();
	str_left_move_test();
	output();
	return 0;
}

// 将字符串 str start 和 end 之间的字符序列反转
bool str_reverse(string &str,int start,int end)
{
	// 字符串长度
	int str_len = str.length();
	if(str_len==0)
		return false;
	if(start < 0 || end > str_len || start>end)
	{
		cout<<"Out of string length!"<<endl;
		return false;
	}
	int tmp;
	int len = end - start;
	for(int i=0;i<=len/2;++i)
	{
		tmp = str[start+i];
		str[start+i] = str[start+len-i];
		str[start+len-i] = tmp;
	}
	return true;
}

// 将字符串 str 循环左移k位
bool str_left_move(string &str,int k)
{
	int str_len = str.length();
	if(str_len == 0)
		return false;
	if(k<=0 || k > str_len)
	{
		cerr<<"k must greater than 1 and no more than string length!"<<endl;
		return false;
	}
	str_reverse(str,0,k-1);
	str_reverse(str,k,str_len-1);
	str_reverse(str,0,str_len-1);
}

// 测试函数
void str_reverse_test()
{
	string str1 = "abcxyz";
	string str2 = "ghtsdfgs";
	str_reverse(str1,0,5);
	assert(str1.compare("zyxcba")==0);
	assert(str_reverse(str1,0,10)==false);
	str_reverse(str2,2,5);
	assert(str2.compare("ghfdstgs")==0);
	str_reverse(str2,0,7);
	assert(str2.compare("sgtsdfhg")==0);
}

void str_left_move_test()
{
	string str1 = "XYZdefabc";
	assert(str_left_move(str1,20)==false);
	str_left_move(str1,3);
	assert(str1.compare("defabcXYZ")==0);
	str_left_move(str1,9);
	assert(str1.compare("defabcXYZ")==0);
}

void output()
{
	cout<<"Please input a string:"<<endl;
	string str;
	getline(cin,str);
	cout<<"How many chars do you want to move from left:";
	int move;
	cin>>move;
	bool if_succeed = str_left_move(str,move);
	if(if_succeed)
	{
		cout<<"After move "<<move<<" chars from left,the string is:"<<endl;
		cout<<str<<endl;
	}
}
