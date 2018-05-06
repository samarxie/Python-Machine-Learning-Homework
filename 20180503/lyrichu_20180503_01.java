/*
*date    : 2018-05-05 14:33:08
*author  : lyrichu
*email   :919987476@qq.com
*link    : https://www.github.com/Lyrichu
*version : 0.1
*description:
*Q1:
求数组的最长公共递增子序列
输入:一个无序数组
输出:最长公共递增子序列长度以及递增子序列
*/
import java.util.Stack;

public class lyrichu_20180503_01
{
	public static int lcs(int [] arr)
	{
		int [] arr1 = new int[arr.length]; //arr1 存放各元素作为最大元素的最长递增子序列的长度
		// pre　记录以该元素作为最大元素的递增序列中，该元素的前驱元素
		int [] pre = new int[arr.length];
		for(int i=0;i<arr.length;++i)
		{
			arr1[i] = 1;
			pre[i] = i;
		}
		for(int j=1;j<arr.length;++j)
		{
			for(int i=0;i<j;i++)
			{
				if(arr[j] > arr[i] && arr1[j] < arr1[i]+1)
				{
					arr1[j] = arr1[i] + 1;
					pre[j] = i;
				}
			}
		}
		int max = 0,index = 0;
		for(int k=0;k<arr1.length;++k)
		{
			if(arr1[k]>max)
			{
				max = arr1[k];
				index = k;
			}
		}
		System.out.println("最长递增子序列长度为:" + max);
		Stack<Integer> stack = new Stack<Integer>();
		while(index != pre[index])
		{
			stack.push(arr[index]);
			index = pre[index];
		}
		if(index == pre[index])
		{
			stack.push(arr[index]);
		}
		while (!stack.isEmpty()){
			System.out.print(stack.pop()+" ");
		}
		System.out.println();
		return max;
	}
	public static void main(String args[])
	{
		int [] arr = {35, 36, 39, 3, 15, 27, 6, 42};
		lcs(arr);
	}
}
