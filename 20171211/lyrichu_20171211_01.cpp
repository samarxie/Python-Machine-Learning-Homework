/*
Q1:
��ʵ��һ����������ƥ�����'.'��'*'��������ʽ��
ģʽ�е��ַ�'.'��ʾ����һ���ַ�����'*'��ʾ��ǰ����ַ����Գ�������Σ�����0�Σ��� 
�ڱ����У�ƥ����ָ�ַ����������ַ�ƥ������ģʽ��
���磬�ַ���"aaa"��ģʽ"a.a"��"ab*ac*a"ƥ�䣬������"aa.a"��"ab*a"����ƥ��
--------------------------
�����ѶȽϴ�
���ǿ��Կ���ģʽ pattern �еĵڶ����ַ��ǲ���*
(1) ����ڶ����ַ�����*,�򿴵�һ���ַ��Ƿ�ƥ�䣬�����ƥ��ֱ�ӷ���false��
���ƥ��Ļ�����pattern �� string ����ǰ�ƶ�һ���ַ�������ƥ�䡣
(2) ����ڶ����ַ���*,��
(2.1) �����һ���ַ���ƥ��Ļ�����ģʽ����ƶ������ַ������൱�ڵ�һ���ַ�������0�Σ�
(2.2) �����һ���ַ�ƥ��Ļ�����string����ƶ�һ���ַ�����pattern ��������ƶ������ַ�(
�൱�ڵ�һ���ַ�����һ��)���߱��ֲ��䣬���൱��(2.1)�����
*/
#include<iostream>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cstring>
using namespace std;
void output();
// �ַ���str �� pattern �Ƿ�ƥ��
bool is_match(char *str,char *pattern);
// ���Ժ���
void is_match_test();

int main(void)
{
	is_match_test();
	output();
	return 0;
}

// �ַ���str �� pattern �Ƿ�ƥ��
bool is_match(char *str,char *pattern)
{
	if(str == NULL || pattern == NULL)
		return false;
	// ���str �� pattern ͬʱ����ĩβ����ƥ��ɹ�
	if(str[0] == '\0' && pattern[0] == '\0')
		return true;
	// ���pattern ����ĩβ,��str û�е���ĩβ����ƥ��ʧ��
	if(str[0] != '\0' && pattern[0] == '\0')
		return false;
	// ���pattern�ڶ�����*
	if(pattern[1]=='*')
	{
		// ��� pattern ��һ���ַ��� str��һ���ַ�ƥ��
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
