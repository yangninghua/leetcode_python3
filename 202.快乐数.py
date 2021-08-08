# @before-stub-for-debug-begin
from python3problem202 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#
# https://leetcode-cn.com/problems/happy-number/description/
#
# algorithms
# Easy (61.68%)
# Likes:    647
# Dislikes: 0
# Total Accepted:    156.7K
# Total Submissions: 254K
# Testcase Example:  '19'
#
# 编写一个算法来判断一个数 n 是不是快乐数。
# 
# 「快乐数」定义为：
# 
# 
# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果 可以变为  1，那么这个数就是快乐数。
# 
# 
# 如果 n 是快乐数就返回 true ；不是，则返回 false 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：19
# 输出：true
# 解释：
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# 
# 
# 示例 2：
# 
# 
# 输入：n = 2
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 
# 
#

# @lc code=start
class Solution:

    def isHappy(self, n: int) -> bool:
        
        # set --- add
        # def getsum(num):
        #     temp = 0
        #     alist = []
        #     while num>0:
        #         a = num%10
        #         num = num // 10
        #         alist.append(a)
        #         temp += (a ** 2)
        #     alist = alist[::-1]
        #     return temp
        
        # happ = set()
        # while 1:
        #     sum = getsum(n)
        #     if sum == 1:
        #         return True
        #     elif sum in happ:
        #         return False
        #     else:
        #         happ.add(sum)
        #         n = sum
        

        mem = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in mem:
                return False
            else:
                mem.add(n)
        else:
            return True
# @lc code=end

