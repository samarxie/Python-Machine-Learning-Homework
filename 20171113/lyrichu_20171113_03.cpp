/*
Q3��
�������е��������֣����ǰ��һ�����ִ��ں�������֣����������������һ������ԡ�����һ������,�����������е�����Ե�����P������P��1000000007ȡģ�Ľ������� �����P%1000000007
��������:

��Ŀ��֤�����������û�е���ͬ������

���ݷ�Χ��

	����%50������,size<=10^4

	����%75������,size<=10^5

	����%100������,size<=2*10^5

ʾ��1
����

1,2,3,4,5,6,7,0

���

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
	// �����������
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