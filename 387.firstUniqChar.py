'''
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.
 

注意事项：您可以假定该字符串只包含小写字母。
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_list = list(set(s))
        s_list.sort(key = s.index)
        for value in s_list:
            if s.count(value) == 1:
                return s.index(value)   
        return -1
'''
# best sol:
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.find(l) != -1 and s.find(l) == s.rfind(l)]
        return min(index) if len(index) > 0 else -1
'''
