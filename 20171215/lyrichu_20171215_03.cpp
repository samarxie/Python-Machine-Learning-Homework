/*
 * Q3:
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，
每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。
 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
 但是，它不能进入方格（35,38），
因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
 */
#include <iostream>
#include <cstring>
#include <cassert>
using namespace std;
/*统计机器人最多可以到达多少个格子
 * k:阈值
 * rows:方格行数
 * cols:方格列数
 */
int moving_count(int k,int rows,int cols);
/*回溯法判断
 * k:阈值
 * rows:方格行数
 * cols:方格列数
 * row:当前行
 * col:当前列
 * visited: 记录每个格子是否被访问过的bool矩阵
 */
int moving_count_core(int k,int rows,int cols,int row,int col,bool *visited);
// 检测下一个格子是否可以访问
bool check(int k,int rows,int cols,int row,int col,bool *visited);
// 求一个数字各位数字和
int digits_sum(int n);
// 测试函数
void test();

int main(int argc,char *argv[])
{
    test();
    return 0;
}

/*统计机器人最多可以到达多少个格子
 * k:阈值
 * rows:方格行数
 * cols:方格列数
 */
int moving_count(int k,int rows,int cols)
{
    bool *visited = new bool[rows*cols];
    memset(visited, false,rows*cols);
    int count = moving_count_core(k,rows,cols,0,0,visited);
    delete [] visited;
    return count;
}


/*回溯法判断
 * k:阈值
 * rows:方格行数
 * cols:方格列数
 * row:当前行
 * col:当前列
 * visited: 记录每个格子是否被访问过的bool矩阵
 */
int moving_count_core(int k,int rows,int cols,int row,int col,bool *visited)
{
    int count = 0;
    if(check(k,rows,cols,row,col,visited))
    {
        visited[row*cols + col] = true;
        count = 1 + moving_count_core(k,rows,cols,row-1,col,visited)
                + moving_count_core(k,rows,cols,row,col-1,visited)
                + moving_count_core(k,rows,cols,row,col+1,visited)
                + moving_count_core(k,rows,cols,row+1,col,visited);
    }
    return count;
}

// 检测下一个格子是否可以访问
bool check(int k,int rows,int cols,int row,int col,bool *visited)
{
    if(row >= 0 && row < rows && col >= 0 && col < cols && digits_sum(row)+digits_sum(col) <= k
            && !visited[row*cols+col])
        return true;
    return false;
}

// 求一个数字各位数字和
int digits_sum(int n)
{
   int sum = 0;
    while(n)
    {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

// 测试
void test()
{
    int k,rows,cols;
    k = 2;
    rows = cols = 2;
    assert(moving_count(k,rows,cols) == 4);
    cout<<"Test 1 succeed!"<<endl;
    k = 3;
    rows = cols = 2;
    assert(moving_count(k,rows,cols) == 4);
    cout<<"Test 2 succeed!"<<endl;
}
