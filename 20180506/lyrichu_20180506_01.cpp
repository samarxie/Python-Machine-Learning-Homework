/*
*date    : 2018-05-06 10:59:15
*author  : lyrichu
*email   :919987476@qq.com
*link    : https://www.github.com/Lyrichu
*version : 0.1
*description:
*走迷宫
分析:求最短,用bfs,假设入口是左上角(0,0),从入口开始用bfs遍历迷宫，算出入口到所有点的最短路径，
以及这些路径上每个节点的前驱
*/
#include <cstdio>
#include <cstring>
#include <queue>
using namespace std;

const int MAXN = 5; // 最大行数和列数
// 迷宫的行数和列数
int m = MAXN,n = MAXN;
// 迷宫，0表示空地，１表示障碍物
int matrix[MAXN][MAXN];

// 4个方向,'U':上,'R':右,'D':下,'L':左
const char name[4] = {'U','R','D','L'};
const int dx[4] = {-1,0,1,0}; //行
const int dy[4] = {0,1,0,-1}; //列

typedef struct state_t
{
	int data;
	int action;
	int father;
} state_t;

// 状态总数
const int STATE_MAX = MAXN*MAXN;
state_t nodes[STATE_MAX];

int state_hash(const state_t &s);

int state_index(const state_t &s)
{
	return state_hash(s);
}

void print_action(const int end)
{
	if(nodes[end].father == -1) return;
	print_action(nodes[end].father);
	putchar(name[nodes[end].action]);
}

void print_path(const int end)
{
	if(nodes[end].father == -1)
	{
		printf("(%d,%d)\n",end/n,end %n);
		return;
	}
	print_path(nodes[end].father);
	printf("(%d,%d)\n",end/n,end %n);
}

void hashset_init();
bool hashset_find(const state_t &s);
void hashset_insert(const state_t &s);
void state_extend_init(const state_t &s);
bool state_extend(const state_t &s,state_t &next);
bool state_is_target(const state_t &s);

int bfs(state_t &start)
{
	queue<state_t> q;
	hashset_init();
	start.action = -1;
	start.father = -1;
	nodes[state_index(start)] = start;
	hashset_insert(start);
	if (state_is_target(start))
	{
		return state_index(start);
	}
	q.push(start);
	while(!q.empty())
	{
		const state_t s = q.front();
		q.pop();
		state_t next;
		state_extend_init(s);
		while(state_extend(s,next))
		{
			if(state_is_target(next))
				return state_index(next);
			q.push(next);
			hashset_insert(next);
		}
	}
	return -1;
}

int main(int argc, char const *argv[])
{
	state_t start = {0,-1,-1};  //左上角为起点
	int end;
	for (int i = 0; i < m; ++i)
	{
		for (int j = 0; j < n; ++i)
		{
			scanf("%d",&matrix[i][j]);
		}
	}
	end = bfs(start);
	print_path(end);
	return 0;
}

// functions implement
const int HASH_CAPACITY = STATE_MAX;
bool visited[HASH_CAPACITY];

int state_hash(const state_t &s)
{
	return s.data;
}

void hashset_init()
{
	memset(visited,0,sizeof(visited));  // 初始化
}

bool hashset_find(const state_t &s)
{
	return visited[state_hash(s)] == true;
}

void hashset_insert(const state_t &s)
{
	visited[state_hash(s)] = true;
}

int action_cur;
#define ACTION_BEGIN 0
#define ACTION_END 4

// 扩展点，当前位置
int x,y;
void state_extend_init(const state_t &s)
{
	action_cur = ACTION_BEGIN;
	x = s.data /n;
	y = s.data % n;
}

bool state_extend(const state_t &s,state_t &next)
{
	while(action_cur < ACTION_END)
	{
		const int nx = x + dx[action_cur];
		const int ny = y + dy[action_cur];
		if(nx >= 0 && nx < m && ny >= 0 && ny <n && !matrix[nx][ny])
		{
			next.data = nx*n + ny;
			// 判重
			if(!hashset_find(next))
			{
				// 记录路径
				next.action = action_cur;
				next.father = state_hash(s);
				nodes[state_index(next)] = next;
				action_cur++;
				return true;
			}
		}
		action_cur++;
	}
	return false;
}

const state_t END = {24,-1,-1};
bool state_is_target(const state_t &s)
{
	return s.data == END.data;
}

