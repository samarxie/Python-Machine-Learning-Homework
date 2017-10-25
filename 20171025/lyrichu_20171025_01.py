# -*- coding:utf-8 -*-
'''
@author:lyrichu
@email:919987476@qq.com
@description:
Q1:
Implement regular expression matching with support for '.' and '*'.
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
'''

def isMatch(source_str,pattern):
	if not pattern:
		return not source_str
	first_match = bool(source_str) and pattern[0] in {source_str[0], '.'}
	if len(pattern) >= 2 and pattern[1] == '*':
		return (isMatch(source_str, pattern[2:]) or
			first_match and isMatch(source_str[1:], pattern))
	else:
		return first_match and isMatch(source_str[1:], pattern[1:])
	
if __name__ == '__main__':
	print("please input the source string:")
	source_str = input()
	print("please input the pattern string:")
	pattern = input()
	flag = isMatch(source_str,pattern)
	if_match = "match" if flag else "not match"
	print("{pattern} {if_match} {source_str}".format(pattern=pattern,if_match=if_match,source_str=source_str))
	
				
				
	