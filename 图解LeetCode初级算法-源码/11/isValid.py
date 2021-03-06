#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#  File: /Users/king/Python初级算法/code/11/isValid.py
#  Project: /Users/king/Python初级算法/code/11
#  Created Date: 2019/03/12
#  Author: hstking hst_king@hotmail.com




def isValid(s):
    if len(s)%2 != 0:
        return False
    symbolDic = {'{':'}', '[': ']', '(': ')'}
    stack = []
    for i in range(len(s)):
        if len(stack) == 0:
            if s[i] in symbolDic.keys():
                stack.append(s[i])
            else:
                return False
        else: # len(stack) != 0
            if s[i] in symbolDic.keys():
                stack.append(s[i])
            else:
                if symbolDic[stack[-1]] == s[i]:
                    stack.pop()
                else:
                    return False
    if len(stack) == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    s = "{[]}"
    # s = "){"
    # s = "(([]){})"
    # s = "()[]{}"
    # s = "[({(())}[()])]"
    # s = "(("
    # s = "()"
    print(isValid(s))