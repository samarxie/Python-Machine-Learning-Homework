/*
Q3:
LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...他随机从中抽出了5张牌,想测测自己的手气,
看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！
！“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。
上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何。
为了方便起见,你可以认为大小王是0。
-----------
本题相当于是输入一些0-13的数字，0表示可以转化为任意整数，判断能否组成连续的整数
比如输入 0,0,1,3,5 可以转化为1,2,3,4,5 于是可以转化为顺子
思路是:将数字排序，然后判断非零数字之间的间隔数目是否小于等于0的数目
*/
#include<iostream>
#include<cassert>
#include<cstdlib>
using namespace std;

void output();
// 是否可以转化
bool if_convert_concrete(int *arr,int n);
// 测试
void if_convert_concrete_test();
// 比较函数
int cmp(const void *a,const void *b);

int main(void)
{
	if_convert_concrete_test();
	output();
	return 0;
}

// 是否可以转化
bool if_convert_concrete(int *arr,int n)
{
	if(arr == NULL || n < 1)
		return false;
	// zeros_num 为0的个数
	// gap_nums 为非零数字间隔
	int zeros_num,gap_nums;
	zeros_num = gap_nums = 0;
	// 首先排序
	qsort(arr,n,sizeof(int),cmp);
	// 统计0的个数
	while(arr[zeros_num]==0)
		++zeros_num;
	// 当前非零数字
	int current = zeros_num;
	// 下一个非零数字
	int next = zeros_num + 1;
	while(next < n)
	{
		//如果有两个数字相等，则一定构不成顺子
		if(arr[next]==arr[current])
			return false;
		gap_nums += arr[next] - arr[current] -1;
		current = next;
		next++;
	}
	return gap_nums <= zeros_num;
}
// 比较函数
int cmp(const void *a,const void *b)
{
	return *((int*)a) - *((int*)b);
}
// 测试
void if_convert_concrete_test()
{
	int arr1[5] = {0,0,1,3,5};
	int arr2[] = {0};
	int arr3[6] = {0,1,4,0,10,0};
	assert(if_convert_concrete(arr1,5));
	assert(if_convert_concrete(arr2,1));
	assert(!if_convert_concrete(arr3,6));
}

// 输出
void output()
{
	cout<<"How many numbers do you want to input:";
	int num;
	cin>>num;
	cout<<"Please input "<<num<<" numbers between 0 and 13:";
	int *arr;
	if((arr = new int[num]) == NULL)
		exit(-1);
	for(int i=0;i<num;++i)
		cin>>arr[i];
	bool res = if_convert_concrete(arr,num);
	cout<<"You "<<(res ? "can":"can't")<<" turn the input to concrete!"<<endl;
}