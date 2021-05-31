"""
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

给的nums是一个升序排列好的数组。

"""


# Resolution
"""
用2个指针，一个A用于轮询整个数组，另外一个B用于原地替换数组元素。然后返回B当前的大小。
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not len(nums) : return 
        slow = fast = 0
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]  
        
        return slow+1

