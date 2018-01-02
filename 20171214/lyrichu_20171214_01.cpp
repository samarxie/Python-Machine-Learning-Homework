/*
Q1:
请实现两个函数，分别用来序列化和反序列化二叉树
*/
#include<iostream>
#include<cassert>
#include<vector>
#include<list>
typedef int type;
#define NONE 0
using namespace std;
typedef struct Node
{
	type data;
	struct Node *left;
	struct Node *right;
} NODE;
// 定义一个保存NODE 节点的全局链表
list<NODE*> LI;
// 插入节点
bool insert(NODE *root,type data);
// 前序遍历
void pre_print(NODE *root,vector<type> &v);
// 二叉树序列化
void serialize(NODE *root,list<type> &li);
// 二叉树反序列化
void deserialize(NODE **root,list<type> &li);
// 测试函数
void test();

int main(void)
{
	test();
	return 0;
}

// 插入节点
bool insert(NODE *root,type data)
{
	if(root == nullptr)
		return false;
	if(root->data == NONE)
	{
		root->data = data;
		LI.push_back(root);
		return true;
	}
	NODE *new_node = new NODE;
	new_node->data = data;
	new_node->left = new_node->right = nullptr;
	NODE *current_node = LI.front();
	if(current_node->left == nullptr)
	{
		current_node->left = new_node;
		LI.push_back(new_node);
	}
	else
	{
		current_node->right = new_node;
		LI.push_back(new_node);
		LI.pop_front();
	}
	return true;
}

// 前序遍历
void pre_print(NODE *root,vector<type> &v)
{
	if(root == nullptr)
		return;
	v.push_back(root->data);
	pre_print(root->left,v);
	pre_print(root->right,v);
}

// 二叉树序列化
void serialize(NODE *root,list<type> &li)
{
	if(root == nullptr)
	{
		li.push_back(NONE);
		return;
	}
	li.push_back(root->data);
	serialize(root->left,li);
	serialize(root->right,li);
}

// 二叉树反序列化
void deserialize(NODE **root,list<type> &li)
{
	type data = li.front();
	li.pop_front();
	while(!li.empty() && data != NONE)
	{
		*root = new NODE;
		(*root)->data = data;
		(*root)->left = nullptr;
		(*root)->right = nullptr;
		deserialize(&((*root)->left),li);
		deserialize(&((*root)->right),li);
	}
}

void test()
{
	NODE *root = new NODE; // create a tree root node
	root->data = NONE;
	root->left = root->right = nullptr;
	type data[] = {1,3,5,2,4};
	for(int i=0;i<5;++i)
		insert(root,data[i]);
	vector<type> v;
	pre_print(root,v);
	vector<type> tmp = {1,3,2,4,5};
	assert(v == tmp);
	cout<<"Test 1 succeed!"<<endl;
	delete root;
	root = new NODE;
	// 构造一个序列化数据,空节点用 NONE 表示
	list<type> li = {1,3,2,NONE,NONE,4,NONE,NONE,5,NONE,NONE};
	deserialize(&root,li);
	v.clear();
	pre_print(root,v);
	tmp = {1,3,2,4,5};
	assert(v == tmp);
	cout<<"Test 2 succeed!"<<endl;
	delete root;
}


