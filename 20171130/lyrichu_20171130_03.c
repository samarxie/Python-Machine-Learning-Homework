/*
实现堆排序
*/
#include<stdio.h>
#include<stdlib.h>
#include<time.h>
// 调整最大堆
void max_heapify(int *,int,int);
// 构建最大堆
void build_heap(int *,int);
// 堆排序 
void heap_sort(int *,int);
void print(int *,int);

int main(void)
{
	srand(time(0));
	printf("Please input the numbers count: ");
	int count;
	scanf("%d",&count);
	int *arr = (int*)calloc(count,sizeof(int));
	if(arr == NULL)
	{
		printf("Calloc memory failed!\n");
		exit(EXIT_FAILURE);
	}
	for(int i=0;i<count;++i)
		*(arr+i) = rand() % 100;
	printf("Before heap sort,the arr is:\n");
	print(arr,count);
	heap_sort(arr,count);
	printf("After heap sort,the arr is:\n");
	print(arr,count);
	free(arr);
	return 0;
}

// 调整最大堆 
// heap_size 为堆大小
// n 为要调整的节点
void max_heapify(int *arr,int heap_size,int n)
{
	int left = 2*n; // 左子树节点
	int right = 2*n+1; // 右子树节点
	int largest; // 保存最大节点序号
	if(left <= heap_size && arr[left-1] > arr[n-1])
		largest = left;
	else
		largest = n;
	if(right <= heap_size && arr[right-1] > arr[largest-1])
		largest = right;
	// 交换 arr[largest-1] 和 arr[n-1] 的值
	if(largest != n)
	{
		int temp = arr[largest-1];
		arr[largest-1] = arr[n-1];
		arr[n-1] = temp;
		// 递归调整最大堆
		max_heapify(arr,heap_size,largest);
	}
}

// 建立最大堆

void build_heap(int *arr,int heap_size)
{
	// arr[heap_size/2],...,arr[heap_size-1] 都是最大堆的叶子节点
	// 我们从最后一个非叶子节点开始,递归调整
	for(int i= heap_size/2;i>=1;--i)
		max_heapify(arr,heap_size,i);
}

// 堆排序 
void heap_sort(int *arr,int heap_size)
{
	// 首先构建最大堆 
	build_heap(arr,heap_size);
	int temp;
	for(int i=heap_size;i>=2;--i)
	{
		// 交换 arr[0] 和 arr[i-1] 的值 
		// 此时 arr[0] 为最大值 
		temp = arr[0];
		arr[0] = arr[i-1];
		arr[i-1] = temp;
		//调整第1个节点，同时最大堆长度减一
		max_heapify(arr,i-1,1);
	}
}

void print(int *arr,int n)
{
	for(int i=0;i<n;++i)
		printf("%d ",*(arr+i));
	printf("\n");
}


