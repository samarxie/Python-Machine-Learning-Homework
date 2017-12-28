/*
Q1:
请实现一个函数用来匹配包括'.'和'*'的正则表达式。
模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 
在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
--------------------------
本题难度较大
我们可以考虑模式 pattern 中的第二个字符是不是*
(1) 如果第二个字符不是*,则看第一个字符是否匹配，如果不匹配直接返回false；
如果匹配的话，则pattern 与 string 都向前移动一个字符，接着匹配。
(2) 如果第二个字符是*,则
(2.1) 如果第一个字符不匹配的话，则将模式向后移动两个字符，这相当于第一个字符出现了0次；
(2.2) 如果第一个字符匹配的话，则string向后移动一个字符，而pattern 可以向后移动两个字符(
相当于第一个字符出现一次)或者保持不变，这相当于(2.1)的情况
*/
#include<iostream>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cstring>
using namespace std;
void output();
// 字符串str 与 pattern 是否匹配
bool is_match(char *str,char *pattern);
// 测试函数
void is_match_test();

int main(void)
{
	is_match_test();
	output();
	return 0;
}

// 字符串str 与 pattern 是否匹配
bool is_match(char *str,char *pattern)
{
	if(str == NULL || pattern == NULL)
		return false;
	// 如果str 与 pattern 同时到达末尾，则匹配成功
	if(str[0] == '\0' && pattern[0] == '\0')
		return true;
	// 如果pattern 到达末尾,而str 没有到达末尾，则匹配失败
	if(str[0] != '\0' && pattern[0] == '\0')
		return false;
	// 如果pattern第二个是*
	if(pattern[1]=='*')
	{
		// 如果 pattern 第一个字符和 str第一个字符匹配
		if(pattern[0]==str[0] || (pattern[0] == '.' && str[0] != '\0'))
			return is_match(str+1,pattern) || is_match(str+1,pattern+2);
		else
			return is_match(str,pattern+2);
	}
	else
	{
		if(str[0] == pattern[0] || (pattern[0] == '.' && str[0] != '\0'))
			return is_match(str+1,pattern+1);
		else
			return false;
	}
	return false;
}

void is_match_test()
{
	char *arr[3] = {"abcf","sdddhjsd","hsajhdsagds"};
	char *pattern[3] = {".bcf.*",".d*h..d","hsahdsg..*"};
	assert(is_match(arr[0],NULL)==false);
	assert(is_match(NULL,pattern[0])==false);
	assert(is_match(arr[0],pattern[0])==true);
	assert(is_match(arr[1],pattern[1])==true);
	assert(is_match(arr[2],pattern[2])==false);
}

void output()
{
	cout<<"Please input a string(less than 500 chars):"<<endl;
	const int N = 500;
	char s[N+1];
	char p[N+1];
	fgets(s,N,stdin);
	cout<<"Please input a pattern:"<<endl;
	fgets(p,N,stdin);
	cout<<"\""<<p<<"\""<<(is_match(s,p)?" match ":" is not match ")<<"\""<<s<<"\""<<endl;
}
