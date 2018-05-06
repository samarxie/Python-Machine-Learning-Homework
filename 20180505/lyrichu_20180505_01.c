/*
四色问题
*/
#include <stdio.h>
#include <string.h>

#define MAXN 8

int N;
int g[MAXN][MAXN];

// 记录每个点的颜色，四种颜色用1,2,3,4表示，０表示未染色
int history[MAXN];
int count; // 方案个数

/*
深度优先搜索，给第i个节点涂色
@param i:第i个地点
@return:None
*/
void dfs(int i)
{
	int j,c;
	if(i == N)
	{
		count++;
		return;
	}
	for(c = 1;c<5;c++)
	{
		int ok = 1;
		for(j=0;j<i;j++)
		{
			if(g[i][j] && c == history[j])
				ok = 0; // 相邻且同色
		}
		if(ok)
		{
			history[i] = c;
			dfs(i+1);
		}
	}
}

int main(int argc, char const *argv[])
{
	int i,j;
	scanf("%d",&N);
	for(i=0;i<N;i++)
		for(j=0;j<N;j++)
			scanf("%d",&g[i][j]);
	dfs(0);
	printf("%d\n",count);
	return 0;
}
