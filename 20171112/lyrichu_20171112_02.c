/*
Q2:HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。
今天测试组开完会后,他又发话了:在古老的一维模式识别中,
常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。
但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？
例如:{6,-3,-2,7,-15,1,2,2},
连续子向量的最大和为8(从第0个开始,到第3个为止)。你会不会被他忽悠住？(子向量的长度至少是1)
*/
#include<stdio.h>
const int MAX = 100;
int arr[MAX];

int main(void)
{
	printf("Please input the number counts(total less than %d counts): ",MAX);
	// 用户输入数字个数
	int input;
	scanf("%d",&input);
	printf("Please input %d numbers: ",input);
	int count = 0; // 输入数字个数
	while(count < input && scanf("%d",arr+count))
		++count;
	// 初始化最大连续数字和为一个非常小的负数
	int max_sum = -1e-8;
	int sum = 0;
	// begin 为最大连续数字和起始位置
	// len 为长度
	int begin = 0;
	int len = 0;
	for(int i=0;i<count;++i)
	{
		if(sum>=0)
		{
			sum += arr[i];
			++len;
		}
		else
		{
			sum = arr[i];
			begin = i;
			len = 1;
		}
		if(sum > max_sum)
			max_sum = sum;
	}
	printf("The max sub series is:\n");
	for(int i=0;i<len;++i)
		printf("%d ",arr[begin+i]);
	printf("\n");
	printf("The max continues sum is: %d\n",max_sum);
	return 0;
}