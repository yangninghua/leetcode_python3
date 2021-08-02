# @before-stub-for-debug-begin
from python3problem215 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (64.67%)
# Likes:    1180
# Dislikes: 0
# Total Accepted:    376.6K
# Total Submissions: 582.3K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
# 
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 
# 
# 示例 2:
# 
# 
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
# 
# 
# 
# 提示： 
# 
# 
# 1 
# -10^4 
# 
# 
#

# @lc code=start
class Solution:

    def InsSort(self, arr,start,end):    
        for i in range(start+1,end+1):
            elem = arr[i]
            j = i-1
            while j>=start and elem<arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = elem
        return arr

    def merge(self, arr,start,mid,end):
        if mid==end:
            return arr
        first = arr[start:mid+1]
        last = arr[mid+1:end+1]
        len1 = mid-start+1
        len2 = end-mid
        ind1 = 0
        ind2 = 0
        ind  = start
        
        while ind1<len1 and ind2<len2:
            if first[ind1]<last[ind2]:
                arr[ind] = first[ind1]
                ind1 += 1
            else:
                arr[ind] = last[ind2]
                ind2 += 1
            ind += 1
        
        while ind1<len1:
            arr[ind] = first[ind1]
            ind1 += 1
            ind += 1
                
        while ind2<len2:
            arr[ind] = last[ind2]
            ind2 += 1
            ind += 1   
                
        return arr
                

    def TimSort(self, arr):
        #对于长度小于32数组直接进行二分插入排序
        #不会进行复杂的归并排序
        #因为在小数组中插入排序的性能已经足够好
        minrun = 32
        n = len(arr)
        
        for start in range(0,n,minrun):
            end = min(start+minrun-1,n-1)
            arr = self.InsSort(arr,start,end)
            
        curr_size = minrun
        while curr_size<n:    
            for start in range(0,n,curr_size*2):
                mid = min(n-1,start+curr_size-1)
                end = min(n-1,mid+curr_size)
                arr = self.merge(arr,start,mid,end)
            curr_size *= 2
        return arr

    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     return sorted(nums, reverse=True)[k-1]
    
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     # Tim Sort
    #     # https://github.com/discovermayank/Tim-Sort
    #     # https://www.cnblogs.com/sunshuyi/p/12680918.html
    #     return self.TimSort(nums)[::-1][k-1]


    # heapq 堆排序--默认小顶堆
    # heapq.heappush()函数把值加入堆中
    # heap.heapify(list)转换列表成为堆结构
    # heapq.heappop()函数弹出堆中最小值
    # heapq.heaprepalce()删除堆中最小元素并加入一个元素
    # heapq.nlargest(3, nums)获取堆中最大或最小的范围值
    # heapq.nsmallest(3, nums)获取堆中最大或最小的范围值
    # heapq.heappushpop(heap, item) 先把item加入到堆中，然后再pop
    #                               比heappush()再heappop()要快得多
    #heapq.heapreplace(heap, item) 先pop，然后再把item加入到堆中，
    #                               比heappop()再heappush()要快得多
    '''
    num1 = [32, 3, 5, 34, 54, 23, 132]
    num2 = [23, 2, 12, 656, 324, 23, 54]
    num1 = sorted(num1)
    num2 = sorted(num2)
    res = heapq.merge(num1, num2)
    '''
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     import heapq
    #     heap = []
    #     for num in nums:
    #         heapq.heappush(heap, num)
    #     # len=7 k=2 result=(0 1 2 3 4) [5] 6
    #     for _ in range(len(nums)-k):
    #         heapq.heappop(heap)
    #     return heapq.heappop(heap)

    # def findKthLargest(self, nums, k):
    #     import heapq
    #     heap = nums[:k]
    #     heapq.heapify(heap)
    #     for n in nums[k:]:
    #         heapq.heappushpop(heap, n)
    #     return heap[0]

    
    # O(n) time, quick selection
    # def findKthLargest(self, nums, k):
    #     # convert the kth largest to smallest
    #     return self.findKthSmallest(nums, len(nums)+1-k)
        
    # def findKthSmallest(self, nums, k):
    #     if nums:
    #         pos = self.partition(nums, 0, len(nums)-1)
    #         if k > pos+1:
    #             return self.findKthSmallest(nums[pos+1:], k-pos-1)
    #         elif k < pos+1:
    #             return self.findKthSmallest(nums[:pos], k)
    #         else:
    #             return nums[pos]
    
    # # choose the right-most element as pivot   
    # def partition(self, nums, l, r):
    #     low = l
    #     while l < r:
    #         if nums[l] < nums[r]:
    #             nums[l], nums[low] = nums[low], nums[l]
    #             low += 1
    #         l += 1
    #     nums[low], nums[r] = nums[r], nums[low]
    #     return low

    # def quick_sort(self, iList):
    #     if len(iList) < 1:
    #         return iList
    #     left = []
    #     right = []
    #     for i in iList[1:]:
    #         if i < iList[0]:
    #             left.append(i)
    #         else:
    #             right.append(i)
    #     return self.quick_sort(left) + [iList[0]] + self.quick_sort(right)

    # def findKthLargest(self, nums, k):
    #     if not nums:
    #         return nums
    #     nums = self.quick_sort(nums)
    #     return nums[-k]


    '''
    void maxHeapify(vector<int>& a, int i, int heapSize) {
        int l = i * 2 + 1, r = i * 2 + 2, largest = i;
        if (l < heapSize && a[l] > a[largest]) {
            largest = l;
        } 
        if (r < heapSize && a[r] > a[largest]) {
            largest = r;
        }
        if (largest != i) {
            swap(a[i], a[largest]);
            maxHeapify(a, largest, heapSize);
        }
    }
    '''
    def maxHeapify(self, a, i, heapSize):
        l = i * 2 + 1
        r = i * 2 + 2
        largest = i
        # 获取顶节点、左节点和右节点中的最大数字节点的位置
        if l<heapSize and a[l] > a[largest]:
            largest = l
        if r < heapSize and a[r] > a[largest]:
            largest = r
        if largest != i:
            a[largest], a[i] = a[i], a[largest]
            self.maxHeapify(a, largest, heapSize)

    def buildMaxHeap(self, a, heapSize):
        # 从第一个非子节点开始调整最大堆
        for i in range(heapSize//2, -1, -1):
            self.maxHeapify(a, i, heapSize)

    def findKthLargest(self, nums, k):
        heapSize = len(nums)
        self.buildMaxHeap(nums, heapSize)
        #return nums[k-1]
        for i in range(len(nums)-1, len(nums)-k+1 -1 , -1):
           nums[i], nums[0] = nums[0], nums[i]
           heapSize -= 1
           self.maxHeapify(nums, 0, heapSize)
        return nums[0]
    
    #堆调整建堆的时间复杂度为O(n)
    #插入法建堆的时间复杂度为O(nlgn) 
    #参考：https://github.com/Wu-GQ/MaxHeap/blob/master/MaxHeap.py
    #https://github.com/ccampo133/maxheap/blob/master/maxheap.py
    # https://www.runoob.com/python3/python-heap-sort.html

        

# @lc code=end

