# @before-stub-for-debug-begin
from python3problem217 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#
# https://leetcode-cn.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (56.13%)
# Likes:    429
# Dislikes: 0
# Total Accepted:    316.2K
# Total Submissions: 563.5K
# Testcase Example:  '[1,2,3,1]'
#
# 给定一个整数数组，判断是否存在重复元素。
# 
# 如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: [1,2,3,1]
# 输出: true
# 
# 示例 2:
# 
# 
# 输入: [1,2,3,4]
# 输出: false
# 
# 示例 3:
# 
# 
# 输入: [1,1,1,3,3,4,3,2,4,2]
# 输出: true
# 
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # if len(nums)<=1:
        #     return False
        # dup = {}
        # for i in range(0, len(nums), 1):
        #     if nums[i] in dup:
        #         return True
        #     else:
        #         dup[nums[i]] = 1
        # return False


        # if len(nums)<=1:
        #     return False
        # if len(set(nums)) != len(nums):
        #     return True
        # else:
        #     return False


        # if len(nums)<=1:
        #     return False
        # #nums.sort()
        # nums = sorted(nums)
        # for i in range(0, len(nums)-1, 1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False

        # 超时
        # if len(nums)<=1:
        #     return False
        # for i in range(0, len(nums)-1, 1):
        #     if nums[i] in nums[i+1:]:
        #         return True
        # return False

        

# @lc code=end

