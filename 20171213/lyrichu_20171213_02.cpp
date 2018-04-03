/*
Q2:
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
--------------------思路-------------------------------
对于二叉树
                   1
			2            3
		4      5      6     7
	 8    9  10  11 12 13  14 15
其之字形打印顺序为:1 3 2 4 5 6 7 15 14 13 12 11 10 9 8
注意到奇数层是从左到右打印，先打印左节点，再打印右节点；
偶数层是从右到左打印，先打印右节点，再打印左节点。利用栈先进
后出的特点，我们可以定义两个栈，分别保存奇数层和偶数层的节点，
对于奇数层，由于下一层是偶数层，先打印右节点，再打印左节点，所以
这一层应该先保存左节点，再保存右节点；对于偶数层，正好相反，先保存
右节点，再保存左节点。
-------------------伪代码------------------------------
stack1,stack2; // stack1，stack2 分别保存奇数层和偶数层的节点
if(root == NULL)
	return;
stack1.push(root);
print(root->data);
stack1.pop();
if(root->left)
	stack2.push(root->left);
if(root->right)
	stack2.push(root->right);
while(!stack1.empty() || !stack2.empty())
{
	// 如果 stack1 为空，说明当前要打印stack2中的节点
	if(stack1.empty())
	{
		while(!stack2.empty())
		{
			current = stack2.back();
			print(current->data);
			// 偶数层，先保存右节点，再保存左节点
			if(current->right)
				stack1.push(current->right);
			if(current->left)
				stack1.push(current->left);
			// 将父节点出栈
			stack2.pop();
		}
	}
	else if(stack2.empty())
	{
		while(!stack1.empty())
		{
			current = stack1.back();
			print(current->data);
			// 奇数层，先保存左节点，再保存右节点
			if(current->left)
				stack2.push(current->left);
			if(current->right)
				stack2.push(current->right);
			// 将父节点出栈
			stack1.pop();
		}
	}
}
*/
#include<iostream>
#include<list>
#include<stack>
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
    // 添加节点
    bool add_node(int data);
    // 之字形打印
    void zhi_print(vector<int> &v);
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
// 之字形打印
void BinaryTree::zhi_print(vector<int> &v)
{
    // stack1 保存二叉树奇数层节点
    // stack2 保存二叉树偶数层节点
    stack<NODE*> stack1,stack2;
    if(root == NULL)
        return;
    stack1.push(root);
    v.clear();
    v.push_back(root->data);
    stack1.pop();
    if(root->left)
        stack2.push(root->left);
    if(root->right)
        stack2.push(root->right);
    while(!stack1.empty() || !stack2.empty())
    {
        // 如果 stack1 为空，说明当前要打印stack2中的节点
        if(stack1.empty())
        {
            while(!stack2.empty())
            {
                NODE *current = stack2.top();
                v.push_back(current->data);
                // 偶数层，先保存右节点，再保存左节点
                if(current->right)
                    stack1.push(current->right);
                if(current->left)
                    stack1.push(current->left);
                // 将父节点出栈
                stack2.pop();
            }
        }
        else if(stack2.empty())
        {
            while(!stack1.empty())
            {
                NODE *current = stack1.top();
                v.push_back(current->data);
                // 奇数层，先保存左节点，再保存右节点
                if(current->left)
                    stack2.push(current->left);
                if(current->right)
                    stack2.push(current->right);
                // 将父节点出栈
                stack1.pop();
            }
        }
    }
}

void test()
{
    BinaryTree *btree = new BinaryTree[3];
    int arr1[3] = {1,4,5};
    int arr2[5] = {10,8,2,3,9};
    int arr3[7] = {1,2,3,5,4,8,9};
    for(int i=0;i<3;++i)
        btree[0].add_node(arr1[i]);
    for(int i=0;i<5;++i)
        btree[1].add_node(arr2[i]);
    for(int i=0;i<7;++i)
        btree[2].add_node(arr3[i]);
    vector<int> v,tmp;
    btree[0].zhi_print(v);
    tmp = {1,5,4};
    check(1,v == tmp);
    btree[1].zhi_print(v);
    tmp = {10,2,8,3,9};
    check(2,v == tmp);
    btree[2].zhi_print(v);
    tmp = {1,3,2,5,4,8,9};
    check(3,v == tmp);
}

// check if true
void check(int index, bool flag)
{
    if(flag)
        cout<<"Test "<<index<<" succeeds!"<<endl;
    else
        cout<<"Test "<<index<<" fails!"<<endl;
}

