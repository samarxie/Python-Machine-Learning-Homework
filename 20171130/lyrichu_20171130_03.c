/*
ʵ�ֶ�����
*/
#include<stdio.h>
#include<stdlib.h>
#include<time.h>
// ��������
void max_heapify(int *,int,int);
// ��������
void build_heap(int *,int);
// ������ 
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

// �������� 
// heap_size Ϊ�Ѵ�С
// n ΪҪ�����Ľڵ�
void max_heapify(int *arr,int heap_size,int n)
{
	int left = 2*n; // �������ڵ�
	int right = 2*n+1; // �������ڵ�
	int largest; // �������ڵ����
	if(left <= heap_size && arr[left-1] > arr[n-1])
		largest = left;
	else
		largest = n;
	if(right <= heap_size && arr[right-1] > arr[largest-1])
		largest = right;
	// ���� arr[largest-1] �� arr[n-1] ��ֵ
	if(largest != n)
	{
		int temp = arr[largest-1];
		arr[largest-1] = arr[n-1];
		arr[n-1] = temp;
		// �ݹ��������
		max_heapify(arr,heap_size,largest);
	}
}

// ��������

void build_heap(int *arr,int heap_size)
{
	// arr[heap_size/2],...,arr[heap_size-1] �������ѵ�Ҷ�ӽڵ�
	// ���Ǵ����һ����Ҷ�ӽڵ㿪ʼ,�ݹ����
	for(int i= heap_size/2;i>=1;--i)
		max_heapify(arr,heap_size,i);
}

// ������ 
void heap_sort(int *arr,int heap_size)
{
	// ���ȹ������� 
	build_heap(arr,heap_size);
	int temp;
	for(int i=heap_size;i>=2;--i)
	{
		// ���� arr[0] �� arr[i-1] ��ֵ 
		// ��ʱ arr[0] Ϊ���ֵ 
		temp = arr[0];
		arr[0] = arr[i-1];
		arr[i-1] = temp;
		//������1���ڵ㣬ͬʱ���ѳ��ȼ�һ
		max_heapify(arr,i-1,1);
	}
}

void print(int *arr,int n)
{
	for(int i=0;i<n;++i)
		printf("%d ",*(arr+i));
	printf("\n");
}


