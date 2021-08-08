#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#
# https://leetcode-cn.com/problems/valid-anagram/description/
#
# algorithms
# Easy (64.24%)
# Likes:    412
# Dislikes: 0
# Total Accepted:    266.4K
# Total Submissions: 414.6K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
# 
# 注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 
# 
# 示例 2:
# 
# 
# 输入: s = "rat", t = "car"
# 输出: false
# 
# 
# 
# 提示:
# 
# 
# 1 
# s 和 t 仅包含小写字母
# 
# 
# 
# 
# 进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
# 
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # import collections
        # ds = collections.defaultdict(int)
        # dt = collections.defaultdict(int)

        # for i in s:
        #     ds[i] += 1
        # for i in t:
        #     dt[i] += 1
        # return ds == dt


        flag = [0] * 26
        for i in s:
            flag[ord(i) - ord('a')] += 1
        for i in t:
            flag[ord(i) - ord('a')] -= 1
        for i in range(26):
            if flag[i] != 0:
                return False
        return True

# @lc code=end

