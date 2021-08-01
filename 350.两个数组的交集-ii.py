# @before-stub-for-debug-begin
from python3problem350 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#
# https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/description/
#
# algorithms
# Easy (54.59%)
# Likes:    528
# Dislikes: 0
# Total Accepted:    222.1K
# Total Submissions: 405.4K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# 给定两个数组，编写一个函数来计算它们的交集。
# 
# 
# 
# 示例 1：
# 
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2,2]
# 
# 
# 示例 2:
# 
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[4,9]
# 
# 
# 
# 说明：
# 
# 
# 输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
# 我们可以不考虑输出结果的顺序。
# 
# 
# 进阶：
# 
# 
# 如果给定的数组已经排好序呢？你将如何优化你的算法？
# 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
# 如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
# 
# 
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        #[1,2,2,1]
        #[2,2]
        #Expected Answer[2,2]
        #error
        # if len(nums1) > len(nums2):
        #     temp = set(nums1)-set(nums2)
        #     return list(set(nums1)-set(temp))
        # else:
        #     temp = set(nums2)-set(nums1)
        #     return list(set(nums2)-set(temp))




        # nums1.sort()
        # nums2.sort()
        # p1 = 0 #nums1的指针
        # p2 = 0
        # result = []
        # #指针+滑动窗口
        # while p1<len(nums1) and p2<len(nums2):
        #     if nums1[p1] == nums2[p2]:
        #         result.append(nums1[p1])
        #         p1 += 1
        #         p2 += 1
        #     elif nums1[p1] < nums2[p2]:
        #         p1 += 1
        #     else:
        #         p2 += 1
        # return result 


        # if len(nums1) > len(nums2):
        #     nums1, nums2 = nums2,nums1
        # result = []
        # for m in nums1:
        #     if m in nums2:
        #         result.append(m)
        #         nums2.remove(m)
        # return result 


# @lc code=end

