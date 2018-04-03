/*
Q1：
求最长公共子序列。
*/
#include<iostream>
#include<string>
#include<cstdlib>
#include<cassert>
using namespace std;
// 求解最长公共子序列
int lcs(string &s1,int n1,string &s2,int n2);
void lcs_test();
void input();
inline int max(int a,int b){return a>b ? a:b;}

int main(void)
{
	lcs_test();
	input();
	return 0;
}

int lcs(string &s1,int n1,string &s2,int n2)
{
	// arr[i][j] 存放字符串1长度为i，字符串2长度为j的LCS长度
	int (*arr)[n2+1] = new int[n1+1][n2+1];
	if(arr == NULL)
	{
		cout<<"New memory failed!\n";
		exit(EXIT_FAILURE);
	}
	for(int i=0;i<=n1;++i)
	{
		for(int j=0;j<=n2;++j)
		{
			if(i==0 || j == 0)
				arr[i][j] = 0;
			else if(s1[i-1]==s2[j-1])
				arr[i][j] = arr[i-1][j-1]+1;
			else
				arr[i][j] = max(arr[i][j-1],arr[i-1][j]);
		}
	}
	int res = arr[n1][n2];
	delete [] arr;
	return res;
}

void lcs_test()
{
	string s_arr[4] = {"abcfg","abdfg","afgcf","bcplg"};
	assert(lcs(s_arr[0],5,s_arr[1],5)==4);
	assert(lcs(s_arr[0],5,s_arr[2],5)==3);
	assert(lcs(s_arr[2],5,s_arr[3],5)==1);
}

void input()
{
	string s1,s2;
	cout<<"Please input the first string:";
	getline(cin,s1);
	cout<<"Please input the second string:";
	getline(cin,s2);
	int LCS = lcs(s1,s1.size(),s2,s2.size());
	cout<<"The lcs between \""<<s1<<"\" and \""<<s2<<"\""<<" is "<<LCS<<endl;
}