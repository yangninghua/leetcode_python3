# @before-stub-for-debug-begin
from python3problem977 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#
# https://leetcode-cn.com/problems/squares-of-a-sorted-array/description/
#
# algorithms
# Easy (72.14%)
# Likes:    266
# Dislikes: 0
# Total Accepted:    134.5K
# Total Submissions: 186.5K
# Testcase Example:  '[-4,-1,0,3,10]'
#
# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
# 解释：平方后，数组变为 [16,1,0,9,100]
# 排序后，数组变为 [0,1,9,16,100]
# 
# 示例 2：
# 
# 
# 输入：nums = [-7,-3,2,3,11]
# 输出：[4,9,9,49,121]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 10^4
# -10^4 
# nums 已按 非递减顺序 排序
# 
# 
# 
# 
# 进阶：
# 
# 
# 请你设计时间复杂度为 O(n) 的算法解决本问题
# 
# 
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        # for i in range(len(nums)):
        #     nums[i] = nums[i]*nums[i]
        # nums.sort()
        # return nums

        # 双指针
        # 前后双指针可使用双向队列替换，但是会增加额外内存

        # size = len(nums)
        # left = 0
        # right = size - 1

        # res = [0] * size
        # index = size - 1
        # while left<=right:
        #     if nums[left]*nums[left] > nums[right]*nums[right]:
        #         res[index]=(nums[left]*nums[left])
        #         left += 1
        #         index -= 1
        #     else:
        #         res[index]=(nums[right]*nums[right])
        #         right -= 1
        #         index -= 1
        # return res

        nums_deque = collections.deque(nums)
        res = []
        while nums_deque:
            left = nums_deque[0] ** 2
            right = nums_deque[-1] ** 2
            if left > right:
                res.append(left)
                nums_deque.popleft()
            else:
                res.append(right)
                nums_deque.pop()
        return res[::-1]


# @lc code=end

