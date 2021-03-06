# @before-stub-for-debug-begin
from python3problem1002 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找常用字符
#
# https://leetcode-cn.com/problems/find-common-characters/description/
#
# algorithms
# Easy (73.93%)
# Likes:    233
# Dislikes: 0
# Total Accepted:    54.2K
# Total Submissions: 73.3K
# Testcase Example:  '["bella","label","roller"]'
#
# 给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3
# 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
# 
# 你可以按任意顺序返回答案。
# 
# 
# 
# 示例 1：
# 
# 输入：["bella","label","roller"]
# 输出：["e","l","l"]
# 
# 
# 示例 2：
# 
# 输入：["cool","lock","cook"]
# 输出：["c","o"]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# A[i][j] 是小写字母
# 
# 
#

# @lc code=start
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        # if len(words)<=1:
        #     return list(words[0])
        
        # import collections
        # count = collections.Counter(words[0])

        # for m in words[1:]:
        #     count = count & collections.Counter(m)
        # temp = count.elements()
        # return list(temp)

        if len(words)<=1:
            return list(words[0])
        
        flag = [0]*26
        for m in words[0]:
            flag[ord(m) - ord('a')] += 1
        
        for x in words[1:]:
            
            sec_flag = [0]*26
            for g in x:
                sec_flag[ord(g) - ord('a')] += 1

            
            for pp in range(26):
                flag[pp] = min(flag[pp], sec_flag[pp])
        
        res = []
        for pp in range(26):
            if flag[pp] == 0:
                continue
            else:
                for ppp in range(flag[pp]):
                    res.append(chr(pp+ord('a')))
        return res


        

# @lc code=end

