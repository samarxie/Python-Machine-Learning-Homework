/*
Q1:一个整型数组里除了两个数字之外，
其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
----------
这里采用异或运算的方式
*/
#include<iostream>
#include<cstdlib>
#include<cassert>
using namespace std;

void output();
// 找到两个只出现一次的数字
void find_two_nums(int *arr,int N,int *first,int *second);
// 测试函数
void find_two_nums_test();
// 得到从低位到高位第一次出现1的位置
int get_first1(int);
// n 第 pos 位是否是1
bool is1(int n,int pos);

int main(void)
{
	find_two_nums_test();
	output();
	return 0;
}

// 找到两个只出现一次的数字
void find_two_nums(int *arr,int N,int *first,int *second)
{
	int res = 0;
	/*一个数字和自己进行异或运算一定为0
      由于除了两个数字只出现一次之外，其他数字均出现两次
	  所有将所有数字进行异或运算的结果相当于是这两个只出现一次
	  的数字进行异或运算，而且结果一定不为0，找到最终结果从低位到高位
	  第一次出现1的地方，然后可以按照这一位为1或者0将所有数字分为两组，
	  且出现一次的数字一定位于不同组,两次的数字一定位于相同组。再对每组
	  进行异或运算即可。
	*/
	for(int i=0;i<N;++i)
		res ^= arr[i];
	// 得到 res 从低位到高位第一次出现1的位置
	int first1 = get_first1(res);
	int first_num,second_num;
	first_num = second_num = 0;
	for(int i=0;i<N;++i)
	{
		// 如果 first1 位是1
		if(is1(arr[i],first1))
			first_num ^= arr[i];
		else
			second_num ^= arr[i];	
	}
	*first = first_num;
	*second = second_num;
}
// 测试函数
void find_two_nums_test()
{
	int *first = new int;
	int *second = new int;
	if(first == NULL || second == NULL)
		exit(-1);
	int arr1[6] = {1,1,2,2,3,4};
	int arr2[10] = {3,5,6,7,10,10,3,7,5,9};
	find_two_nums(arr1,6,first,second);
	assert(*first==3 || *first == 4);
	assert((*first)*(*second)==12);
	find_two_nums(arr2,10,first,second);
	assert(*first==6 || *first == 9);
	assert((*first)*(*second)==6*9);
	delete first;
	delete second;
}
// 得到从低位到高位第一次出现1的位置
int get_first1(int n)
{
	if(n == 0)
		return 0;
	int flag = 1;
	int pos = 1;
	while(!n&flag)
	{
		n>>1;
		pos++;
	}
	return pos;
}

// n 第 pos 位是否是1
bool is1(int n,int pos)
{
	n>>(pos-1);
	return n&1;
}

void output()
{
	cout<<"How many numbers do you want to input:";
	int count;
	cin>>count;
	cout<<"Please input "<<count<<" numbers,you should ensure only"<<endl;
	cout<<"two numbers occur once,the other numbers occur twice."<<endl;
	int *arr;
	if((arr = new int[count]) == NULL)
	{
		cout<<"New memory failed!"<<endl;
		exit(-1);
	}
	for(int i=0;i<count;++i)
		cin>>arr[i];
	int *first = new int;
	int *second = new int;
	if(first == NULL || second == NULL)
		exit(-1);
	find_two_nums(arr,count,first,second);
	cout<<"The two numbers that occur only once is:"<<*first<<","<<*second<<endl;
	delete arr;
	delete first;
	delete second;
}


