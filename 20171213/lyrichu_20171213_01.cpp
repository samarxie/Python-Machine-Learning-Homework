/*
Q1:
请实现一个函数，用来判断一颗二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
-----------------------思路-----------------------------
二叉树
                   1
				2    3
			 4   5  6  7
其镜像二叉树为
                   1
				3     2
			 7    6  5  4
两棵二叉树不同，所以显然不是对称二叉树
而 二叉树  
                   1
				2     2
			 3   4  4   3
是镜像二叉树
--------------------------方法1------------------------------------
直观的一个想法是，按照定义，将二叉树反转成镜像二叉树，然后对原来的二叉树
和镜像二叉树分别层次遍历一下，如果得到的序列相同，那么显然就是一棵对称二叉树。
但是要注意一些特殊情况，比如下面这个二叉树
                        7
					  7
原来的二叉树和镜像二叉树层次遍历都是7 7,但是显然不对称，解决办法是将空节点也加入遍历序列
比如可以定义一个NONE 值表示空节点的值，然后比较层次遍历结果。
伪代码如下:
// 方法1，按定义
level_print(root,v1); // 对二叉树层次遍历，将结果存放在v1容器中
reverse_tree(root); // 反转二叉树
level_print(root,v2);// 对反转以后的镜像二叉树层次遍历，结果放在v2容器中
if(v1 == v2)
	return true; // 两次遍历结果一样，则是对称二叉树
else
	return false; // 不是对称二叉树
// 反转二叉树 reverse_tree()定义如下
void reverse_tree(root)
{
	if(root == NULL)
		return;
	left = root->left;
	right = root->right;
	root->right = left;
	root->left = right;
	reverse_tree(left);
	reverse_tree(right);
}
--------------------------------方法2---------------------------
方法1最大的缺点，是层次遍历需要一个辅助链表，而且还需要保存两次遍历的结果，再比较，有些浪费空间。
那能不能不用辅助链表呢？
不难发现，如果按照上面的方法，在考虑空节点的情况下，将层次遍历换做前序遍历，结论也是
一样成立的。考虑到将一个二叉树反转，所有节点原来的左子树和右子树都对调了，所以可以直接
在遍历的时候比较是否对称，而不需要将所有的结果保存下来再比较，这样极大地节省了存储空间。
伪代码如下:
is_symmetrical(root1,root2) 
{
	// root1 是原二叉树根节点
	// root2 是镜像二叉树根节点
	// 两个节点都为空
	if(root1 == NULL && root2 == NULL)
		return true;
	// 有且只有一个节点为空
	if(root1 == NULL || root2 == NULL)
		return false;
	// 两个节点都不为空,且值不等
	if(root1->data != root2->data)
		return false;
	return is_symmetrical(root1->left,root2->right) && 
		   is_symmetrical(root1->right,root2->left);
}
*/
#include<iostream>
#include<list>
#include<vector>
using namespace std;
const int NONE = 0;
typedef struct Node
{
	int data;
	struct Node *left;
	struct Node *right;
} NODE;
class BinaryTree
{
	public:
		NODE *root;
		BinaryTree(){root = new NODE;root->data = NONE;root->left=root->right = NULL;}
		~BinaryTree(){delete root;}
		bool add_node(int data);
		void level_print(vector<int> &v);
		void reverse_tree(NODE *root);
		bool is_symmetrical_m1(); // 方法1
		bool is_symmetrical_m2(NODE *root1,NODE *root2); // 方法2 
	private:
		list<NODE*> LI;
};
// 测试函数
void test();
void check(int index,bool flag);

int main(void)
{
	test();
	return 0;
}

bool BinaryTree::add_node(int data)
{
	if(root == NULL)
		return false;
	if(root->data == NONE)
	{
		if(data <= 0)
			return false; // 节点值只能是正数
		root->data = data;
		LI.push_back(root);
		return true;
	}
	NODE *new_node = new NODE;
	new_node->data = data;
	new_node->left = new_node->right = NULL;
	NODE *current_node = LI.front(); // 当前节点
	if(current_node->left == NULL)
	{
		current_node->left = new_node;
		LI.push_back(new_node);
		return true;
	}
	else
	{
		current_node->right = new_node;
		LI.push_back(new_node);
		LI.pop_front();
		return true;
	}
}
// 层次遍历,注意需要加入空节点值，用NONE 表示
void BinaryTree::level_print(vector<int> &v)
{
	if(root == NULL)
		return;
	list<NODE*> li;
	li.push_back(root);
	while(!li.empty())
	{
		NODE *current_node = li.front();
		if(current_node == NULL)
			v.push_back(NONE);
		else
			v.push_back(current_node->data);
		if(current_node != NULL)
		{
			li.push_back(current_node->left);
			li.push_back(current_node->right);
		}
		li.pop_front();
	}
}
// 反转二叉树
void BinaryTree::reverse_tree(NODE *root)
{
	if(root == NULL)
		return;
	NODE *left = root->left;
	NODE *right = root->right;
	root->right = left;
	root->left = right;
	reverse_tree(left);
	reverse_tree(right);
}
// 方法1
bool BinaryTree::is_symmetrical_m1() 
{
	vector<int> v1,v2;
	level_print(v1);
	reverse_tree(root);
	level_print(v2);
	return v1 == v2;
}
// 判断二叉树是否对称,方法2
bool BinaryTree::is_symmetrical_m2(NODE *root1,NODE *root2) 
{
	// root1 是原二叉树根节点
	// root2 是镜像二叉树根节点
	// 两个节点都为空
	if(root1 == NULL && root2 == NULL)
		return true;
	// 有且只有一个节点为空
	if(root1 == NULL || root2 == NULL)
		return false;
	// 两个节点都不为空,且值不等
	if(root1->data != root2->data)
		return false;
	return is_symmetrical_m2(root1->left,root2->right) && 
		   is_symmetrical_m2(root1->right,root2->left);
}
// 测试函数
void test()
{
	BinaryTree *btree = new BinaryTree[4];
	int arr1[3] = {1,3,3};
	int arr2[4] = {2,2,2,2};
	int arr3[7] = {1,3,3,2,4,4,1};
	int arr4[7] = {1,3,3,2,4,4,2};
	for(int i=0;i<3;++i)
		btree[0].add_node(arr1[i]);
	for(int i=0;i<4;++i)
		btree[1].add_node(arr2[i]);
	for(int i=0;i<7;++i)
		btree[2].add_node(arr3[i]);
	for(int i=0;i<7;++i)
		btree[3].add_node(arr4[i]);
	vector<int> v,tmp;
	btree[0].level_print(v);
	tmp = {1,3,3,NONE,NONE,NONE,NONE};
	check(1,tmp == v);
	check(2,btree[0].is_symmetrical_m2(btree[0].root,btree[0].root));
	check(3,btree[0].is_symmetrical_m1());
	check(4,!btree[1].is_symmetrical_m2(btree[1].root,btree[1].root));
	check(5,!btree[1].is_symmetrical_m1());
	check(6,!btree[2].is_symmetrical_m2(btree[2].root,btree[2].root));
	check(7,!btree[2].is_symmetrical_m1());
	check(8,btree[3].is_symmetrical_m2(btree[3].root,btree[3].root));
	check(9,btree[3].is_symmetrical_m1());
}

void check(int index,bool flag)
{
	if(flag)
		cout<<"Test "<<index<<" succeed!"<<endl;
	else
		cout<<"Test "<<index<<" failed!"<<endl;
}



