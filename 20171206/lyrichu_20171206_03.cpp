/*
Q3:输入一棵二叉树，判断该二叉树是否是平衡二叉树。
*/
#include<iostream>
#include<list>
#include<cstdlib>
#include<cassert>
using namespace std;
// 测试函数
void is_balance_test();
#define MAX(a,b) ((a)>(b)?(a):(b))

// 定义节点
typedef struct Node
{
	int data;
	struct Node *left;
	struct Node *right;
} NODE;

class BinaryTree
{
	public:
		NODE *root = new NODE;
		list<NODE*> li;
		BinaryTree()
		{
			if(root == NULL)
			{
				cerr<<"tree root is NULL!"<<endl;
				exit(EXIT_FAILURE);
			}
			root->data = 0;
			root->left = NULL;
			root->right = NULL;
		}
		// 逐个添加节点
		void insert_data(int data);
		// 批量添加节点
		void insert_data(int *arr,int N);
		// 得到树的高度
		int get_height(NODE *root);
		// 判断是否是平衡二叉树
		bool is_balance(NODE *root);
};

// 主函数
int main(void)
{
	is_balance_test();
	return 0;
}

// 逐个添加节点
void BinaryTree::insert_data(int data)
{
	if(root->data == 0)
	{
		root->data = data;
		li.push_back(root);
	}
	else
	{
		NODE *new_node = new NODE;
		if(new_node == NULL)
			exit(-1);
		new_node->data = data;
		new_node->left = NULL;
		new_node->right = NULL;
		NODE *current_node = li.front();
		if(current_node->left==NULL)
		{
			current_node->left = new_node;
			li.push_back(current_node->left);
		}
		else
		{
			current_node->right = new_node;
			li.push_back(current_node->right);
			li.pop_front();
		}
	}
}

// 批量添加节点
void BinaryTree::insert_data(int *arr,int N)
{
	for(int i=0;i<N;++i)
		BinaryTree::insert_data(arr[i]);
}
// 得到树的高度
int BinaryTree::get_height(NODE *root)
{
	if(root == NULL)
		return 0;
	return MAX(BinaryTree::get_height(root->left),BinaryTree::get_height(root->right))+1;
}

// 判断是否是平衡二叉树
bool BinaryTree::is_balance(NODE *root)
{
	if(root == NULL)
		return true;
	if(BinaryTree::get_height(root->left)-BinaryTree::get_height(root->right)>1 ||
	   BinaryTree::get_height(root->left)-BinaryTree::get_height(root->right)<-1)
	   return false;
	return BinaryTree::is_balance(root->left) && BinaryTree::is_balance(root->right);
}

// is_balance 测试函数
void is_balance_test()
{
	BinaryTree bt1,bt2;
	bt1.root->data = 1;
	NODE *node_arr = new NODE[3];
	if(node_arr == NULL)
	{
		cout<<"New nodes failed!"<<endl;
		exit(-1);
	}
	bt1.root->left = node_arr;
	bt1.root->left->left = node_arr+1;
	bt1.root->left->left->right = node_arr+2;
	int arr[5] = {1,3,5,10,2};
	bt2.insert_data(arr,5);
	assert(bt1.is_balance(bt1.root) == false);
	assert(bt2.is_balance(bt2.root) == true);
	assert(bt2.is_balance(NULL) == true);
	delete bt1.root;
	delete bt2.root;
	delete node_arr;
}

