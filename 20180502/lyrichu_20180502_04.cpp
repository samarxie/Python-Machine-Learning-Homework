/*
*date    : 2018-05-05 22:26:26
*author  : lyrichu
*email   :919987476@qq.com
*link    : https://www.github.com/Lyrichu
*version : 0.1
*description:
*Q4:将Q2中的条件改为每个数字只能使用一次，求解之.
*/
//Leetcode combination sum 2
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution 
{
public:
	vector<vector<int>> combinationSum2(const vector<int> &arr,int target)
	{
		vector<int> tmp; // 存放中间结果
		vector<vector<int>> result; // 存放最后结果
		dfs(arr,target,0,tmp,result);
		return result;
	}

private:
	void dfs(const vector<int> &arr,int target,int index,vector<int> &tmp,vector<vector<int>> &result)
	{
		if(target == 0)
		{
			result.push_back(tmp);
			return;
		}
		int previous = -1; // 之前访问
		for(int i=index;i<arr.size();++i)
		{
			if(previous == arr[i]) // 如果arr[i]之前访问过了，就不应该再访问
				continue;
			if(target < arr[i]) // 剪枝
				return;
			previous = arr[i];
			tmp.push_back(arr[i]);
			dfs(arr,target-arr[i],i+1,tmp,result);
			// 恢复
			tmp.pop_back();
		}
	}
};

int main(int argc, char const *argv[])
{
	int N; // 数组长度
	int target;
	cin>>N;
	vector<int> arr(N);
	for(int i=0;i<N;++i)
		cin>>arr[i];
	sort(arr.begin(),arr.end());
	cin>>target;
	vector<vector<int>> result;
	Solution* s = new Solution;
	result = s->combinationSum2(arr,target);
	for(auto i = result.begin();i != result.end();++i)
    {
            for(auto j = i->begin();j != i->end();++j)
            {
                    cout<<*j<<" ";
            }
            cout<<endl;
    }
	return 0;
}
