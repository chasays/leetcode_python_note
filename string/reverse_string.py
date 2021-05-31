"""
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

e.g.
[1,2,3,4]
output:
[4,3,2,1]

还有就是python内置的切片函数，s[::-1],但是这个比较占内存

"""

# resolution

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        if not len(s):return s
        start = 0
        end = len(s)-1
        while end > start:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
            
        return s
