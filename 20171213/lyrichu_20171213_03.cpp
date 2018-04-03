/*
Q3:
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
---------------------思路--------------------------
其实就是二叉树的层次遍历，利用一个辅助链表就可以搞定。
---------------------伪代码----------------------
list<Node*> li; // 保存二叉树节点的辅助链表
if(root == NULL)
	return;
li.push(root)
while(!li.empty())
{
	current = li.front(); // 当前节点
	print(current->data);
	if(current->left)
		li.push(current->left);
	if(current->right)
		li.push(current->right);
	// 父节点从链表中删除
	li.pop_front();
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

void BinaryTree::level_print(vector<int> &v)
{
    list<NODE*> li;
    if(root == NULL)
        return;
    li.push_back(root);
    v.clear();
    while(!li.empty())
    {
        NODE *current_node = li.front();
        v.push_back(current_node->data);
        if(current_node->left)
            li.push_back(current_node->left);
        if(current_node->right)
            li.push_back(current_node->right);
        li.pop_front();
    }
}

// 测试函数
void test()
{
    BinaryTree *btree = new BinaryTree[3];
    vector<vector<int>> vec = {{1,2,3,4},{1,5,10,8,4,7},{2,2,3,67,3,4}};
    for(int i = 0;i<3;++i)
    {
        for(int j=0;j<vec[i].size();++j)
            btree[i].add_node(vec[i][j]);
    }
    vector<int> v;
    btree[0].level_print(v);
    check(1,v==vec[0]);
    btree[1].level_print(v);
    check(2,v==vec[1]);
    btree[2].level_print(v);
    check(3,v==vec[2]);
}

void check(int index,bool flag)
{
    if(flag)
        cout<<"Test "<<index<<" succeed!"<<endl;
    else
        cout<<"Test "<<index<<" failed!"<<endl;
}

