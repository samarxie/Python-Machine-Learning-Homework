/*
*date    : 2018-05-05 15:03:48
*author  : lyrichu
*email   :919987476@qq.com
*link    : https://www.github.com/Lyrichu
*version : 0.1
*description:
*Q2:给定一个严格递增数组arr和一个数字target,arr中的数字都是正数且唯一，
target为正整数,求出arr中和为target的所有数字组合,数字可以重复使用，返回所有可能的组合.比如arr=[1,2,3,5,7],
target = 5,返回[[1,1,1,1,1],[1,1,1,2],[1,2,2],[1,1,3],[2,3],[5]]
(回溯法)
*/
//LeetCode Combination Sum
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Solution
{
public:
	/*
	@param nums:传入原数组
	@param target:目标和
	*/
	vector< vector<int>> combinationSum(vector<int> &nums,int target)
	{
		// 排序
		sort(nums.begin(),nums.end());
		vector<vector<int>> result; //最终结果
		vector<int> tmp; //中间结果
		dfs(nums,target,0,tmp,result);
		return result;
	}
private:
	/*
	@param nums:原数组(排序之后)
	@param target:当前目标和
	@param level:
	@param tmp:存放中间结果
	@param result:存放最终结果
	*/
	void dfs(vector<int> &nums,int target,int level,vector<int> &tmp,vector<vector<int>> &result)
	{
		if(target == 0) // 找到一个合法解
		{
			result.push_back(tmp);
			return;
		}
		for(size_t i=level;i<nums.size();++i) //扩展状态
		{
			if(target < nums[i]) // 剪枝
				return;
			// 扩展动作
			tmp.push_back(nums[i]);
			dfs(nums,target-nums[i],i,tmp,result);
			//撤销动作
			tmp.pop_back();
		}
	}
};

int main(int argc, char const *argv[])
{
	int N; //数组长度
	int target; //目标和
	cin>>N;
	vector<int> v(N);
	for(int i=0;i<N;++i)
		cin>>v[i];
	cin>>target;
	Solution* s = new Solution;
	vector<vector<int>> result = s->combinationSum(v,target);
	for(auto i = result.begin();i != result.end();i++)
	{
		for(auto j = i->begin();j != i->end();j++)
		{
			cout<<*j<<" ";
		}
		cout<<endl;
	}
	return 0;
}

