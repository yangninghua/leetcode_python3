# @before-stub-for-debug-begin
from python3problem15 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (32.98%)
# Likes:    3608
# Dislikes: 0
# Total Accepted:    594.2K
# Total Submissions: 1.8M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0
# 且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [0]
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# -10^5 
# 
# 
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        for ind, val in enumerate(nums):


            # 必须放在循环里面， 每次初始化
            first  = nums[ind]
            left = ind + 1
            right = len(nums) - 1

            if nums[ind] > 0:
                break
            
            if ind>0 and nums[ind]==nums[ind-1]:
                continue
            

            while left < right:
                sum = first + nums[left] + nums[right]
                if sum >0:
                    right-=1
                elif sum < 0:
                    left +=1
                else:
                    res.append([first, nums[left], nums[right]])

                    while (left < right) and nums[right]==nums[right-1]:
                        right -= 1
                    
                    while (left < right) and nums[left]==nums[left+1]:
                        left += 1
                    
                    left += 1
                    right -= 1
        return res


# @lc code=end

