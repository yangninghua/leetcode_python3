#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (70.12%)
# Likes:    996
# Dislikes: 0
# Total Accepted:    291.6K
# Total Submissions: 415.9K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
# 
# 
# 示例 2：
# 
# 
# 输入：head = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：head = [1]
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点的数目在范围 [0, 100] 内
# 0 
# 
# 
# 
# 
# 进阶：你能在不修改链表节点值的情况下解决这个问题吗?（也就是说，仅修改节点本身。）
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        

        # pre, pre.next = self, head
        # while pre.next and pre.next.next:
        #     a = pre.next
        #     b = a.next
        #     pre.next, b.next, a.next = b, a, b.next
        #     pre = a
        # return self.next

        pre = ListNode()
        pre.next = head
        cur = pre

        while cur.next and cur.next.next:
            a = cur.next
            b = cur.next.next
            c = cur.next.next.next

            cur.next = b
            b.next = a
            a.next = c
            cur = cur.next.next
        return pre.next


# @lc code=end

