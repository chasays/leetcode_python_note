```md


```


Resolution

```py

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

```
