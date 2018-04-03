/*
Q2:
牛客最近来了一个新员工Fish，
每天早晨总是会拿着一本英文杂志，写些句子在本子上。
同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。
例如，“student. a am I”。
后来才意识到，这家伙原来把句子单词的顺序翻转了，
正确的句子应该是“I am a student.”。
Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
-------------
字符串的反转
这里可以先把整个句子反转，再将单词反转
*/
#include<iostream>
#include<string>
#include<cassert>
using namespace std;
void output();
// 将字符串 str start 和 end 之间的字符序列反转
bool str_reverse(string &str,int start,int end);
void sentence_reverse(string &sentence);
// 测试函数
void str_reverse_test();
void sentence_reverse_test();
void output();

int main(void)
{
	str_reverse_test();
	sentence_reverse_test();
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
void sentence_reverse(string &sentence)
{
	int len = sentence.size();
	if(len==0)
		return;
	// 先把整个句子反转
	str_reverse(sentence,0,len-1);
	// 记录单词起始和终止位置
	int first,last;
	first = last = 0;
	while(last < len)
	{
		while(last < len && sentence[last] != ' ')
			last++;
		str_reverse(sentence,first,last-1);
		while(last < len && sentence[last] == ' ')
			last++;
		first = last;
	}
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

void sentence_reverse_test()
{
	string str("student. a am I");
	sentence_reverse(str);
	assert(str=="I am a student.");
}

void output()
{
	cout<<"Please input a sentence:"<<endl;
	string sentence;
	getline(cin,sentence);
	sentence_reverse(sentence);
	cout<<"After reverse,the sentence is:"<<endl<<sentence<<endl;
}


