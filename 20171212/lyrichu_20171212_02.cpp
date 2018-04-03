/*
 * Q2:
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，
重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
 */
#include <iostream>
#include <cassert>
#include <cstdio>
using namespace std;
typedef int type;
typedef struct Node
{
    type data = 0;
    struct Node *next = nullptr;
} NODE;

typedef int type;
// 删除链表重复节点
NODE* delete_sort_list_repeat(NODE *root);
// 添加节点
bool add_node(NODE *root,type data);
// 测试
void test();

int main(int argc,char* argv[])
{
    test();
    cout<<"Test succeed!"<<endl;
    getchar();
    return 0;
}

// 添加节点
bool add_node(NODE *root,type data)
{
    if(root == nullptr)
        return false;
    NODE *current = root;
    while(current->next != nullptr)
        current = current->next;
    NODE *new_node = new NODE;
    new_node->data = data;
    new_node->next = nullptr;
    current->next = new_node;
    return true;
}
// 删除链表重复节点
NODE* delete_sort_list_repeat(NODE *root)
{
    if(root == nullptr)
        return nullptr;
    NODE *pre = root;
    NODE *begin = root->next;
    NODE *current = root->next;
    int count;
    while(current != nullptr)
    {
        count = 0;
        while(current->next != nullptr && current->next->data == begin->data)
        {
            current = current->next;
            ++count;
        }
        if(count > 0)
        {
            pre->next = current->next;
            begin = current->next;
            current = current->next;
        } else
        {
            pre = current;
            begin = current->next;
            current = current->next;
        }
    }
    return root;
}

void test()
{
    NODE *root = new NODE;
    type arr[7] = {1,2,2,3,3,4,5};
    for(int i=0;i<7;++i)
        add_node(root,arr[i]);
    delete_sort_list_repeat(root);
    assert(root->next->data == 1 && root->next->next->data == 4 && root->next->next->next->data == 5);
    cout<<"test 1 succeed!"<<endl;
    root->next = nullptr;
    type arr1[8] = {1,2,3,3,4,5,5,7};
    for(int i=0;i<8;++i)
        add_node(root,arr1[i]);
    delete_sort_list_repeat(root);
    assert(root->next->data == 1 && root->next->next->data == 2 && root->next->next->next->data == 4
        && root->next->next->next->next->data == 7);
    cout<<"test 2 succeed!"<<endl;
    delete root;
}


