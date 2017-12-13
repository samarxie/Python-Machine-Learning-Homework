/*
Q2:输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，
最长路径的长度为树的深度。
*/
#include<iostream>
#include<list>
#include<cstdlib>
using namespace std;
// 输入输出函数
void output();
inline int max(int x,int y){return x>y ?x:y;}
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
			root->data = 0;
			root->left = NULL;
			root->right = NULL;
		}
		// 逐个添加节点
		void insert_data(int data);
		// 批量添加节点
		void insert_data(int *arr,int N);
		// 前序遍历
		void pre_print(NODE *root);
		// 中序遍历
		void mid_print(NODE *root);
		// 后序遍历
		void back_print(NODE *root);
		// 层次遍历
		void level_print(NODE *root);
		// 获取树的高度
		int get_height(NODE *root);
};

// 主函数
int main(void)
{
	output();
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

// 前序遍历
void BinaryTree::pre_print(NODE *root)
{
	if(root == NULL)
		return;
	cout<<root->data<<" ";
	BinaryTree::pre_print(root->left);
	BinaryTree::pre_print(root->right);
}

// 中序遍历
void BinaryTree::mid_print(NODE *root)
{
	if(root == NULL)
		return;
	BinaryTree::mid_print(root->left);
	cout<<root->data<<" ";
	BinaryTree::mid_print(root->right);
}

// 后序遍历
void BinaryTree::back_print(NODE *root)
{
	if(root == NULL)
		return;
	BinaryTree::back_print(root->left);
	BinaryTree::back_print(root->right);
	cout<<root->data<<" ";
}

// 层次遍历
void BinaryTree::level_print(NODE *root)
{
	if(root == NULL || root->data == 0)
		return;
	list<NODE*> L;
	L.push_back(root);
	NODE *current_node;
	while(!L.empty())
	{
		current_node = L.front();
		L.pop_front();
		cout<<current_node->data<<" ";
		if(current_node->left)
			L.push_back(current_node->left);
		if(current_node->right)
			L.push_back(current_node->right);
		
	}
}

// 获取树的高度
int BinaryTree::get_height(NODE *root)
{
	if(root == NULL)
		return 0;
	return max(BinaryTree::get_height(root->left),BinaryTree::get_height(root->right))+1;
}

void output()
{
	BinaryTree binary_tree;
	int arr[5] = {1,2,3,5,6};
	// 插入数据
	binary_tree.insert_data(arr,5);
	// 前序遍历 
	binary_tree.pre_print(binary_tree.root);
	cout<<endl;
	// 中序遍历 
	binary_tree.mid_print(binary_tree.root);
	cout<<endl;
	// 后序遍历 
	binary_tree.back_print(binary_tree.root);
	cout<<endl;
	// 层次遍历 
	binary_tree.level_print(binary_tree.root);
	cout<<endl;
	// 得到树的高度
	cout<<"The tree height is:"<<binary_tree.get_height(binary_tree.root)<<endl;
	delete binary_tree.root;
}

