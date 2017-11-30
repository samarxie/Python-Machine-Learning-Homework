# -*- coding:utf-8 -*-
'''
Q2：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，
序列4，5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
'''

def is_pop_stack(push_stack,pop_stack):
	if(len(push_stack) == 0 or len(pop_stack)== 0 or len(push_stack)!=len(pop_stack)):
		return False
	# 模拟入栈和出栈
	n = len(push_stack) # 栈长
	# s 为模拟栈
	s = []
	# j 为 pop_stack 索引
	j = 0
	for i in range(n):
		# push_stack 元素入栈s
		s.append(push_stack[i])
		while(len(s)>0 and s[-1] == pop_stack[j]):
			s.pop()
			j += 1
	return True if len(s)== 0 else False
	
if __name__ == '__main__':
	push_stack = list(map(int,input("请输入入栈顺序,使用空格分隔:").split(" ")))
	pop_stack = list(map(int,input("请输入出栈顺序,使用空格分隔:").split(" ")))
	flag = is_pop_stack(push_stack,pop_stack)
	print("%s 的出栈序列!" %("合法" if flag else "不合法"))
	
	