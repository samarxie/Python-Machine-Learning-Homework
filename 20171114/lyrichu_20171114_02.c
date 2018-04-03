/*
Q2: 实现采用链接方法的散列表。
假设有2000个字符串,每个字符串长度均不超过8,要求每次查找查找失败的次数近似为3。
采用 散列函数为 除法散列法,散列表的长度取701(接近 2000/3 的质数)。将字符串映射为自然数采用基数为5，比如ab对应的自然数为
97*5 + 98 = 583
*/
#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

const int MAX_LEN = 8;
const int K = 5; // 基数值
const int N = 2000000;
const int m = 7001;
char str_arr[N][MAX_LEN+1];
typedef struct Node
{
	char *str; // 字符串指针
	int count; // 字符串出现次数
	struct Node *next;
}NODE;
// 随机产生 一定长度的小写字母字符串
char * random_str(int,int);
// 将字符串映射为自然数 
int str_to_int(char *,int);
// 除数散列法计算散列值
int hash(char*,int,int);
// 散列表初始化
void hash_init(NODE**,int);
// 散列表插入
void hash_insert(NODE**,int,int,char*);
// 散列表查找,返回出现次数
int hash_search(NODE**,int,int,char*);
// 散列表删除某个关键字
int hash_delete(NODE**,int,int,char*);
// 随机生成字符串并写入文件
int str_to_file(char *,char *,int,int,int);
// 从文件读取一行字符串
char * getline(FILE*,char*,int);

int main(void)
{
	srand(time(0));
	NODE* hash_table[m];
	hash_init(hash_table,m);
	char filename[] = "str.txt";
	//str_to_file(filename,"a",N,1,8);
	FILE *fp = fopen(filename,"r");
	for(int i=0;i<N;++i)
	{
		// 读取一行字符串
		if((i+1)% 10000 == 0)
			printf("%d\n",i+1);
		getline(fp,str_arr[i],MAX_LEN);
		hash_insert(hash_table,m,K,str_arr[i]);
	}
	fclose(fp);
	// 查找
	char *target = "h";
	printf("%s occurs %d times\n",target,hash_search(hash_table,m,K,target));
	// 散列表删除 
	hash_delete(hash_table,m,K,target);
	printf("After delete,%s occurs %d times\n",target,hash_search(hash_table,m,K,target));
	// 释放指针
	for(int i=0;i<m;++i)
		free(hash_table[i]);
	return 0;
}

// 从文件读取一行字符串
// 从 fp 读取一行字符串到str,最多读取n个字符
char * getline(FILE* fp,char* str,int n)
{
	int i = 0;
	int c;
	while((c = fgetc(fp)) != EOF && c != '\n' && i<n)
		str[i++] = c;
	str[i] = '\0';
	while(c != '\n')
		c = fgetc(fp);
	return str;
}
// 随机生成字符串并写入文件
// filename 文件名
// mode 打开文件模式
// count 写入字符串个数
// min 字符串最小长度
// max 字符串最大长度
int str_to_file(char *filename,char *mode,int count,int min,int max)
{
	FILE *fp;
	fp = fopen(filename,mode);
	if(fp==NULL)
	{
		printf("Can't open file!\n");
		exit(-1);
	}
	char *str;
	for(int i=0;i<count;++i)
	{
		str = random_str(1,8);
		fputs(str,fp);
		// 写入一个换行符
		fputc('\n',fp);
	}
	fclose(fp);
}

// 随机产生 一定长度的小写字母字符串
char * random_str(int m,int n)
{
	if(m < 0)
		m = 0;
	if(n > MAX_LEN)
		n = MAX_LEN;
	static char str[MAX_LEN+1];
	int r = m + (rand() %(n-m+1));
	for(int i=0;i<r;++i)
		*(str+i) = 'a' + (rand() %('z'-'a'+1));
	*(str+r) = '\0';
	return str;
}
// 将字符串映射为自然数 
// k 是基数
int str_to_int(char *str,int k)
{
	int sum = 0;
	int n = 0;
	while(*(str+n))
	{
		sum += *(str+n);
		++n;
		if(*(str+n))
			sum *= k;
	}
	return sum;
}

// 除数散列法计算散列值
int hash(char *str,int k,int m)
{
	int sum = str_to_int(str,k);
	return sum % m;
}
// 散列表初始化
void hash_init(NODE** node,int m)
{
	for(int i=0;i<m;++i)
	{
		node[i] = (NODE*)malloc(sizeof(NODE));
		if(node[i] == NULL)
		{
			printf("Malloc memory failed!\n");
			exit(-1);
		}
		node[i]->str =NULL;
		node[i]->next = NULL;
	}
}
// 散列表插入
// node 为指向散列表的指针
// m 为散列表长度
// k 为基数值
// str 为字符串
void hash_insert(NODE** node,int m,int k,char *str)
{
	// 计算字符串hash值
	int h = hash(str,k,m);
	// 遍历到链表尾部
	NODE *current_node = node[h];
	while(current_node->next)
	{
		if(strcmp(current_node->next->str,str)==0)
		{
			++current_node->next->count;
			break;
		}
		else
			current_node = current_node->next;
	}
	if(!current_node->next)
	{
		current_node->next = (NODE*)malloc(sizeof(NODE));
		if(current_node->next == NULL)
		{
			printf("Malloc memory failed!\n");
			exit(-1);
		}
		current_node->next->str = str;
		current_node->next->next = NULL;
		current_node->next->count = 1;
	}
}

// 散列表查找,返回出现次数
int hash_search(NODE** node,int m,int k,char *str)
{
	// 计算字符串hash值
	int h = hash(str,k,m);
	// 遍历到链表尾部
	NODE *current_node = node[h];
	while(current_node->next)
	{
		// 如果查找到一个相等的字符串
		if(strcmp(str,current_node->next->str) == 0)
			return current_node->next->count;
		current_node = current_node->next;
	}
	return 0;
}

// 散列表删除某个关键字
int hash_delete(NODE** node,int m,int k,char *str)
{
	// 计算字符串hash值
	int h = hash(str,k,m);
	// 遍历到链表尾部
	NODE *current_node = node[h];
	while(current_node->next)
	{
		// 如果查找到一个相等的字符串
		if(strcmp(str,current_node->next->str) == 0)
		{
			current_node->next = current_node->next->next;
			break;
		}
		else
			current_node = current_node->next;
	}
}





