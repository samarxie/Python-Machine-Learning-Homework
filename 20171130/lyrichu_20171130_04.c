/*
Q4：使用堆实现优先队列各种操作(出队,插入等)
*/
#include<stdio.h>
#include<stdlib.h>
#include<time.h>
const int inf = 1e8; // 正无穷
int LEN = 6; // 优先队列长度

// 获得优先队列队首元素(最大元素)
int top(int *);
// 删除并返回优先队列最大元素
int heap_extract_max(int *,int);
// 替换优先队列某一个位置的元素
void heap_increase_key(int *,int,int,int);
// 将某一个元素添加到优先队列
void max_heap_insert(int *,int,int);
// 调整最大堆
void max_heapify(int *,int,int);
// 构建最大堆
void build_heap(int *,int);
// 打印函数
void print(int *,int);

int main(void)
{
	srand(time(0));
	int *arr = (int*)calloc(LEN,sizeof(int));
	if(arr == NULL)
	{
		printf("Callloc memory failed!\n");
		exit(-1);
	}
	for(int i=0;i<LEN;++i)
		*(arr+i) = rand() % 10;
	printf("At first,the arr is:\n");
	print(arr,LEN);
	int t;
	// 构建一个最大堆
	build_heap(arr,LEN);
	// 取优先队列的最大元素
	t = top(arr);
	printf("At first,the top element is: %d\n",t);
	t = heap_extract_max(arr,LEN);
	printf("After extract max,the length of arr is %d,the arr is:\n",LEN);
	print(arr,LEN);
	// 增大优先队列第2个元素(从1开始)为10
	heap_increase_key(arr,LEN,2,10);
	t = top(arr);
	printf("After replace,the length of arr is %d,the top element is: %d\n",LEN,t);
	// 将 20 添加到优先队列
	max_heap_insert(arr,LEN,20);
	printf("After insert,the length of arr is %d,the arr is:\n",LEN);
	print(arr,LEN);
	free(arr);
	return 0;
}

// 调整最大堆
void max_heapify(int *arr,int heap_size,int n)
{
	int left = 2*n;
	int right = 2*n + 1;
	int largest;
	if(left <= heap_size && arr[left-1] > arr[n-1])
		largest = left;
	else
		largest = n;
	if(right <= heap_size && arr[right-1] > arr[largest-1])
		largest = right;
	if(largest != n)
	{
		int temp = arr[largest-1];
		arr[largest-1] = arr[n-1];
		arr[n-1] = temp;
		// 递归调整
		max_heapify(arr,heap_size,largest);
	}
}

// 构建最大堆 
void build_heap(int *arr,int heap_size)
{
	for(int i= heap_size/2;i>=1;--i)
		max_heapify(arr,heap_size,i);
}

// 获得优先队列队首元素(最大元素)
int top(int *arr)
{
	return *arr;
}

// 删除并返回优先队列最大元素
int heap_extract_max(int *arr,int heap_size)
{
	int max = *arr;
	--LEN; // 优先队列长度-1
	*arr = *(arr + heap_size-1);
	max_heapify(arr,heap_size-1,1);
	return max;
}
// 替换优先队列某一个位置的元素
// 把位置 n 的元素替换为 key
void heap_increase_key(int *arr,int heap_size,int n,int key)
{
	if(key < arr[n-1])
	{
		printf("key must not be less than %d!\n",arr[n]);
		return;
	}
	else
	{
		arr[n-1] = key;
		// 增大 key 也许需要调整父节点
		int temp;
		while(n >=2 && arr[n/2-1] < arr[n-1])
		{
			temp = arr[n/2-1];
			arr[n/2-1] = arr[n-1];
			arr[n-1] = temp;
			n /= 2;
		}
	}
}

// 将某一个元素添加到优先队列
void max_heap_insert(int *arr,int heap_size,int key)
{
	// 重新分配内存大小
	realloc(arr,(heap_size+1)*sizeof(int));
	*(arr + heap_size) = -inf; // 设置新增的元素为负无穷
	heap_increase_key(arr,heap_size+1,heap_size+1,key);
	++LEN; // 优先队列长度+1
}

void print(int *arr,int n)
{
	for(int i=0;i<n;++i)
		printf("%d ",*(arr+i));
	putchar('\n');
}