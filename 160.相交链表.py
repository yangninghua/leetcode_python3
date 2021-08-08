#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#
# https://leetcode-cn.com/problems/intersection-of-two-linked-lists/description/
#
# algorithms
# Easy (61.01%)
# Likes:    1302
# Dislikes: 0
# Total Accepted:    306.1K
# Total Submissions: 501.7K
# Testcase Example:  '8\n[4,1,8,4,5]\n[5,6,1,8,4,5]\n2\n3'
#
# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。
# 
# 图示两个链表在节点 c1 开始相交：
# 
# 
# 
# 题目数据 保证 整个链式结构中不存在环。
# 
# 注意，函数返回结果后，链表必须 保持其原始结构 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2,
# skipB = 3
# 输出：Intersected at '8'
# 解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
# 从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
# 在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB =
# 1
# 输出：Intersected at '2'
# 解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
# 从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。
# 在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
# 
# 
# 示例 3：
# 
# 
# 
# 
# 输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# 输出：null
# 解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
# 由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
# 这两个链表不相交，因此返回 null 。
# 
# 
# 
# 
# 提示：
# 
# 
# listA 中节点数目为 m
# listB 中节点数目为 n
# 0 
# 1 
# 0 
# 0 
# 如果 listA 和 listB 没有交点，intersectVal 为 0
# 如果 listA 和 listB 有交点，intersectVal == listA[skipA + 1] == listB[skipB +
# 1]
# 
# 
# 
# 
# 进阶：你能否设计一个时间复杂度 O(n) 、仅用 O(1) 内存的解决方案？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        # if headA is None or headB is None:
        #     return None

        # pa = headA # 2 pointers
        # pb = headB

        # while pa is not pb:
        #     # if either pointer hits the end, switch head and continue the second traversal, 
        #     # if not hit the end, just move on to next
        #     if pa is None:
        #         pa = headB
        #     else:
        #         pa = pa.next
            
            
        #     if pb is None:
        #         pb = headA
        #     else:
        #         pb = pb.next
            
        #     print("1\n")
        # return pa


        lengthA,lengthB = 0,0
        curA,curB = headA,headB
        while(curA!=None): #求链表A的长度
            curA = curA.next
            lengthA +=1
        
        while(curB!=None): #求链表B的长度
            curB = curB.next
            lengthB +=1
        
        curA, curB = headA, headB

        if lengthB>lengthA: #让curA为最长链表的头，lenA为其长度
            lengthA, lengthB = lengthB, lengthA
            curA, curB = curB, curA

        gap = lengthA - lengthB #求长度差
        while(gap!=0): 
            curA = curA.next #让curA和curB在同一起点上
            gap -= 1
        
        while(curA!=None):
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next
        return None
# @lc code=end

