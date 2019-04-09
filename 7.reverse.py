'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
'''
class Solution:
    def reverse(self, x: int) -> int:
        s = list(str(x))
        if s[0] == '-':
            temp = s[1:]
            temp.reverse()
            s[1:] = temp
            r = int("".join(s))
            if r < (-2)**31 or r > (2)**31 - 1:
                return 0
            else:
                return r
        else:
            s.reverse()
            r = int("".join(s))
            if r < (-2)**31 or r > (2)**31 - 1:
                return 0
            else:
                return r
'''
# best sol:
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        while x != 0:
            pop = x % 10 - 10 if x < 0 and x % 10 != 0 else x % 10
            x = int(x / 10)
            if rev > (2 ** 31 - 1) / 10:
                return 0
            if rev < - (2 ** 31) / 10:
                return 0
            rev = rev * 10 + pop
        return rev
'''

