/*
 * Q2:
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
 例如 a b c e s f c s a d e e 矩阵中包含一条字符串"bcced"的路径，
 但是矩阵中不包含"abcb"路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
 */
#include <iostream>
#include <cassert>
#include <cstring>
using namespace std;
/*判断矩阵中是否存在含有字符串的路径
 * matrix:矩阵
 * rows:矩阵行数
 * cols:矩阵列数
 * str:字符串
 */
bool has_path(char *matrix,int rows,int cols,const char *str);
/*采用回溯法进行搜索的核心算法
 * matrix:矩阵
 * rows:矩阵行数
 * cols:矩阵列数
 * row:当前行
 * col:当前列
 * str:字符串
 * path_length:当前路径长度
 * visited:判断每个矩阵元素是否被访问过的bool矩阵
 */
bool has_path_core(char *matrix,int rows,int cols,int row,int col,
                    const char *str,int &path_length, bool *visited);

// 测试函数
void test();

int main(int argc,char *argv[])
{
    test();
    return 0;
}

/*判断矩阵中是否存在含有字符串的路径
 * matrix:矩阵
 * rows:矩阵行数
 * cols:矩阵列数
 * str:字符串
 */
bool has_path(char *matrix,int rows,int cols,const char *str)
{
    if(matrix == nullptr || rows < 1 || cols < 1 || str == nullptr)
        return false;
    bool *visited = new bool[rows*cols];
    memset(visited,0,rows*cols); // 设置全0
    int path_length = 0; // 访问路径长度
    for(int row = 0;row < rows;++row)
    {
        for(int col = 0;col < cols;++col)
        {
            if(has_path_core(matrix,rows,cols,row,col,str,path_length,visited))
                return true;
        }
    }
    delete[] visited;
    return false;
}

/*采用回溯法进行搜索的核心算法
 * matrix:矩阵
 * rows:矩阵行数
 * cols:矩阵列数
 * row:当前行
 * col:当前列
 * str:字符串
 * path_length:当前路径长度
 * visited:判断每个矩阵元素是否被访问过的bool矩阵
 */
bool has_path_core(char *matrix,int rows,int cols,int row,int col,
                   const char *str,int &path_length, bool *visited)
{
    // 如果到达字符串末尾
    if(str[path_length] == '\0')
        return true;
    bool if_has_path = false;
    if(row >=0 && row < rows && col >=0 && col < cols && matrix[row*cols + col] == str[path_length]
            && !visited[row*cols+col])
    {
        ++path_length;
        visited[row*cols + col] = true;
        if_has_path = has_path_core(matrix,rows,cols,row,col-1,str,path_length,visited)
                ||    has_path_core(matrix,rows,cols,row-1,col,str,path_length,visited)
                ||    has_path_core(matrix,rows,cols,row,col+1,str,path_length,visited)
                ||    has_path_core(matrix,rows,cols,row+1,col,str,path_length,visited);
        if(!if_has_path)
        {
            --path_length;
            visited[row*cols+col] = false;
        }
    }
    return if_has_path;
}

// 测试函数
void test()
{
    const int rows = 3;
    const int cols = 4;
    char matrix[rows*cols] = {'a','b','c','e',
                              's','f','c','s',
                              'a','d','e','e'};
    const char *str1 = "abce";// true
    const char *str2 = "abfb";//false
    const char *str3 = "abfdeese";//true
    assert(has_path(matrix,rows,cols,str1));
    cout<<"Test 1 succeed!"<<endl;
    assert(!has_path(matrix,rows,cols,str2));
    cout<<"Test 2 succeed!"<<endl;
    assert(has_path(matrix,rows,cols,str3));
    cout<<"Test 3 succeed!"<<endl;
}
