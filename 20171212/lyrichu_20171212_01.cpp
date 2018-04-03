/*
 * Q1:
一个链表中包含环，请找出该链表的环的入口结点。
 */
#include <iostream>
#include <cassert>
#include <cstdio>
using namespace std;

typedef struct Node
{
    int data;
    struct Node *next;
} NODE;

typedef struct SingleList
{
    NODE *head = nullptr;
} SINGLELIST;

// 链表初始化
bool init_singlelist(SINGLELIST *singlelist);
// 增加节点
bool add_node(SINGLELIST *singlelist,int data);
// 删除节点
bool delete_node(SINGLELIST *singlelist,int data);
// 插入节点
bool insert_node(SINGLELIST *singlelist,int pos,int data);
// 得到第pos个位置节点的data
int get_node_data(SINGLELIST *singlelist,int pos);
// 得到链表长度
int get_length(SINGLELIST *singlelist);
// 打印链表数据
int print_singlelist(SINGLELIST *singlelist);
// 设置一快一慢两个指针,得到其相遇的节点
NODE* meeting(SINGLELIST *singlelist);
// 得到链表中环的节点个数,并且找到环的入口节点
NODE* get_entrynode_of_loop(SINGLELIST *singlelist);
// 测试函数
void test();

int main(void)
{
    test();
    cout<<"Test succeed!"<<endl;
    getchar();
    return 0;
}

// 链表初始化
bool init_singlelist(SINGLELIST *singlelist)
{
    singlelist->head = new NODE;
    if(!singlelist->head)
        return false;
    singlelist->head->data = 0;
    singlelist->head->next = nullptr;
    return true;
}

// 增加节点
bool add_node(SINGLELIST *singlelist,int data)
{
    if(!singlelist->head)
        return false;
    NODE *new_node = new NODE;
    new_node->data = data;
    new_node->next = nullptr;
    NODE *current_node = singlelist->head;
    while(current_node->next)
        current_node = current_node->next;
    current_node->next = new_node;
    return true;
}


// 删除节点
bool delete_node(SINGLELIST *singlelist,int data)
{
    if(!singlelist->head)
        return false;
    NODE *current_node = singlelist->head;
    bool flag = false;
    while(current_node->next)
    {
        if(current_node->next->data == data)
        {
            flag = true;
            current_node->next = current_node->next->next;
        }
        else
            current_node = current_node->next;
    }
    return flag;
}

// 插入节点
bool insert_node(SINGLELIST *singlelist,int pos,int data)
{
    if(!singlelist->head)
        return false;
    NODE *current_node = singlelist->head;
    int count = 0;
    while(current_node->next)
    {
        ++count;
        if(count == pos)
        {
            NODE *new_node = new NODE;
            new_node->data = data;
            new_node->next = current_node->next;
            current_node->next = new_node;
            return true;
        }
        current_node = current_node->next;
    }
    return false;
}
// 得到第pos个位置节点的data
int get_node_data(SINGLELIST *singlelist,int pos)
{
    if(!singlelist->head)
        return 0;
    NODE *current_node = singlelist->head;
    int count = 0;
    while(current_node->next)
    {
        ++count;
        if(count == pos)
            return current_node->next->data;
        current_node = current_node->next;
    }
    return 0;
}
// 得到链表长度
int get_length(SINGLELIST *singlelist)
{
    if(!singlelist->head)
        return false;
    NODE *current_node = singlelist->head;
    int length = 0;
    while(current_node->next)
    {
        ++length;
        current_node = current_node->next;
    }
    return length;
}

// 打印链表数据
int print_singlelist(SINGLELIST *singlelist)
{
    if(!singlelist->head)
        return -1;
    NODE *current_node = singlelist->head;
    int count = 0;
    while(current_node->next)
    {
        ++count;
        cout<<current_node->next->data<<" ";
        current_node = current_node->next;
    }
    return count;
}

// 设置一快一慢两个指针,得到其相遇的节点
NODE* meeting(SINGLELIST *singlelist)
{
    if(!singlelist->head)
        return nullptr;
    NODE *slow_node = singlelist->head->next;
    if(slow_node == nullptr)
        return nullptr;
    NODE *quick_node = slow_node->next;
    while(slow_node != nullptr && quick_node != nullptr)
    {
        // 如果两个指针相遇
        if(slow_node == quick_node)
            return slow_node;
        // 慢的指针移动一次
        slow_node = slow_node->next;
        // 快的指针移动两次
        quick_node = quick_node->next;
        if(quick_node != nullptr)
            quick_node = quick_node->next;
    }
    return nullptr;
}

// 得到链表中环的节点个数,并且找到环的入口节点
NODE* get_entrynode_of_loop(SINGLELIST *singlelist)
{
    NODE *meeting_node = meeting(singlelist);
    if(meeting_node == nullptr)
        return nullptr;
    NODE *current_node = meeting_node->next;
    // 环中节点个数
    int loop_node_count = 1;
    while(current_node != meeting_node)
    {
        loop_node_count++;
        current_node = current_node->next;
    }
    NODE *quick_node = singlelist->head;
    for(int i=0;i<loop_node_count;++i)
        quick_node = quick_node->next;
    NODE *slow_node = singlelist->head;
    while(slow_node != quick_node)
    {
        slow_node = slow_node->next;
        quick_node = quick_node->next;
    }
    return slow_node;
}

void test()
{
    SINGLELIST *singlelist = new SINGLELIST;
    init_singlelist(singlelist);
    assert(singlelist->head->next == nullptr && singlelist->head->data == 0);
    cout<<"test 1 succeed!"<<endl;
    bool res = add_node(singlelist,1);
    assert(res && get_length(singlelist) == 1 && singlelist->head->next->data == 1);
    cout<<"test 2 succeed!"<<endl;
    res = insert_node(singlelist,1,3);
    assert(res && get_length(singlelist) == 2 && get_node_data(singlelist,1) == 3);
    cout<<"test 3 succeed!"<<endl;
    res = delete_node(singlelist,3);
    assert(res && get_length(singlelist) == 1 && get_node_data(singlelist,1) == 1);
    cout<<"test 4 succeed!"<<endl;
    int data_arr[5] = {2,3,4,5,6};
    add_node(singlelist,data_arr[0]);
    add_node(singlelist,data_arr[1]);
    NODE *meeting_node = singlelist->head->next->next->next;
    for(int i=2;i<5;++i)
        add_node(singlelist,data_arr[i]);
    NODE *current = singlelist->head;
    for(int i=0;i<5;++i)
        current = current->next;
    current->next = meeting_node;
    assert(get_entrynode_of_loop(singlelist) == meeting_node);
    cout<<"test 5 succeed!"<<endl;
    delete singlelist;
}

