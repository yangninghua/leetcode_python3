# @before-stub-for-debug-begin
from python3problem66 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
# https://leetcode-cn.com/problems/plus-one/description/
#
# algorithms
# Easy (45.86%)
# Likes:    725
# Dislikes: 0
# Total Accepted:    323.2K
# Total Submissions: 704.5K
# Testcase Example:  '[1,2,3]'
#
# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
# 
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：digits = [1,2,3]
# 输出：[1,2,4]
# 解释：输入数组表示数字 123。
# 
# 
# 示例 2：
# 
# 
# 输入：digits = [4,3,2,1]
# 输出：[4,3,2,2]
# 解释：输入数组表示数字 4321。
# 
# 
# 示例 3：
# 
# 
# 输入：digits = [0]
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # if len(digits)==1 and digits[0]==0:
        #     return [1]
        # new = [0] * (len(digits)+1)
        # new[1:] = digits[:]
        # for m in range(len(digits)-1, -1, -1):
        #     if digits[m]+1>=10:
        #         new[m+1] = 0
        #     else:
        #         new[m+1] = digits[m]+1
        #         return new[1:]
        # new[0] = 1
        # return new

        digits.reverse()
        for m in range(len(digits)):
            if digits[m]==9:
                digits[m]=0
            else:
                digits[m]+=1
                break
        if digits[-1]==0:
            digits.append(1)
        digits.reverse()
        return digits
                


# @lc code=end

