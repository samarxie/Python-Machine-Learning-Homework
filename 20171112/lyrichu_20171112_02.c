/*
Q2:HZż������Щרҵ������������Щ�Ǽ����רҵ��ͬѧ��
��������鿪����,���ַ�����:�ڹ��ϵ�һάģʽʶ����,
������Ҫ��������������������,������ȫΪ������ʱ��,����ܺý����
����,��������а�������,�Ƿ�Ӧ�ð���ĳ������,�������Աߵ��������ֲ����أ�
����:{6,-3,-2,7,-15,1,2,2},
����������������Ϊ8(�ӵ�0����ʼ,����3��Ϊֹ)����᲻�ᱻ������ס��(�������ĳ���������1)
*/
#include<stdio.h>
const int MAX = 100;
int arr[MAX];

int main(void)
{
	printf("Please input the number counts(total less than %d counts): ",MAX);
	// �û��������ָ���
	int input;
	scanf("%d",&input);
	printf("Please input %d numbers: ",input);
	int count = 0; // �������ָ���
	while(count < input && scanf("%d",arr+count))
		++count;
	// ��ʼ������������ֺ�Ϊһ���ǳ�С�ĸ���
	int max_sum = -1e-8;
	int sum = 0;
	// begin Ϊ����������ֺ���ʼλ��
	// len Ϊ����
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