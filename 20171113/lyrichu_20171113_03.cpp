/*
Q3：
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
输入描述:

题目保证输入的数组中没有的相同的数字

数据范围：

	对于%50的数据,size<=10^4

	对于%75的数据,size<=10^5

	对于%100的数据,size<=2*10^5

示例1
输入

1,2,3,4,5,6,7,0

输出

7
*/
#include<iostream>
#include<vector>
using namespace std;

int main(void)
{
	cout<<"Please input the numbers count: ";
	int count;
	cin>>count;
	cout<<"Please input "<<count<<" numbers:\n";
	vector<int> v(count);
	for(int i=0;i<count;++i)
	{
		cin>>v[i];
	}
	// 保存逆序对数
	int num = 0;
	for(int i=count-1;i>=0;--i)
	{
		for(int j=i-1;j>=0;--j)
		{
			if(v[j] > v[i])
				++num;
		}
	}
	cout<<"The reverse numbers count is: "<<num<<endl;
	return 0;
}