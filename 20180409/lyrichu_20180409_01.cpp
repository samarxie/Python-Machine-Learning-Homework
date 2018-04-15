/*
*date    : 2018-04-09 21:12:07
*author  : lyrichu
*email   :919987476@qq.com
*link    : https://www.github.com/Lyrichu
*version : 0.1
*description:
*Q1:现有Ｎ个大理石,每个大理石上写了一个非负整数,首先把各个数从小到大排序,
然后回答Ｑ个问题。每个问题询问是否有一个大理石上写着某一个整数x,如果是还要回答
哪个大理石上写着x，排序后的大理石从左到右编号为1-N
样例输入:
4 1
2 3 5 1
5
5 2
1 3 3 3 1
2 3
样例输出:
CASE# 1:
5 found at 4
CASE# 2:
2 not found
3 found at 3
*/
#include <cstdio>
#include <algorithm>
using namespace std;
const int maxn = 10000;

int main(int argc, char const *argv[])
{
	int n,q,x,a[maxn],k = 0; // n 个大理石,q个问题
	while(scanf("%d%d",&n,&q) == 2 && n)
	{
		printf("CASE# %d:\n",++k);
		for(int i=0;i<n;++i) scanf("%d",a+i);
		sort(a,a+n); // 排序
		while(q--)
		{
			scanf("%d",&x);
			int p = lower_bound(a,a+n,x) - a;// 已排序数组a中寻找x
			if(a[p] == x) printf("%d found at %d\n",x,p+1);
			else printf("%d not found\n",x);
		}
	}
	return 0;
}