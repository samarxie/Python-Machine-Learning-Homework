/*
Q1：实现字符串的Horspool 匹配算法(参考《算法设计与分析基础》7.2)
*/
#include<string>
#include<map>
#include<iostream>
#include<vector>
#include<cassert>
#include<cstdlib>
using namespace std;

void create_move_table(const string &target,map<char,int> &table);
void search_str_by_horspool(const string &target,const string &source,map<char,int> &table,vector<int> &v);
void create_move_table_test();
void search_str_by_horspool_test();
void test_all();

int main(void)
{
	// 测试函数
	test_all();
	return 0;
}

// 产生移动步长表
// target 为目标搜索字符串
// table 为移动步长表
void create_move_table(const string &target,map<char,int> &table)
{
	int len = target.size(); // 字符串长度
	for(int i=0;i<26;++i)
		table['a'+i] = len;
	for(int i=0;i<len-1;++i)
		table[target[i]] = len-1-i;
}

// 字符串搜索
// target 为搜索的目标字符串
// source 为源字符串
// table 移动步长表
// 返回所有出现位置索引组成的vector
void search_str_by_horspool(const string &target,const string &source,map<char,int> &table,vector<int> &v)
{
	int target_len = target.length();
	int source_len = source.length();
	if(source_len < target_len)
	{
		cout<<"Source string must be longer than target string!";
		exit(-1);
	}
	int index = target_len-1; // 初始目标字符串最右位置
	while(index < source_len)
	{
		int pos = 0;
		while(pos < target_len && target[target_len-1-pos] == source[index-pos])
			++pos;
		if(pos == target_len)
			v.push_back(index - target_len +1);
		index += table[source[index]];
	}
}

// create_move_table 测试函数
void create_move_table_test()
{
	const string target1 = "abc";
	map<char,int> table1;
	create_move_table(target1,table1);
	assert(table1['a']==2);
	assert(table1['b']==1);
	assert(table1['c']==3);
	assert(table1['z']==3);
	const string target2 = "barber";
	map<char,int> table2;
	create_move_table(target2,table2);
	assert(table2['b']==2);
	assert(table2['a']==4);
	assert(table2['r']==3);
	assert(table2['e']==1);
	assert(table2['d']==6);
}

// search_str_by_horspool 测试函数 
void search_str_by_horspool_test()
{
	const int num = 4;
	const string target[num] = {"abc","ab","ga","de"};
	const string source = "dabcfgaabc";
	vector<int> v[num];
	map<char,int> table[num];
	for(int i=0;i<num;++i)
	{
		create_move_table(target[i],table[i]);
		search_str_by_horspool(target[i],source,table[i],v[i]);
		if(i==0)
			assert(v[i].size()==2 &&v[i][0]==1 &&v[i][1]==7);
		else if(i==1)
			assert(v[i].size()==2 &&v[i][0]==1 &&v[i][1]==7);
		else if(i==2)
			assert(v[i].size()==1 &&v[i][0]==5);
		else if(i == 3)
			assert(v[i].empty());
	}
}

// 全部测试函数
void test_all()
{
	create_move_table_test();
	search_str_by_horspool_test();
}


