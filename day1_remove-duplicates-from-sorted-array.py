'''
26. 删除排序数组中的重复项
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
解题思路:
使用2个指针,第一个慢第二个快,第二个始终比第一个大1，进行逐一比较。
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first = 0
        second = 1
        while(second < len(nums)):
            if nums[first] == nums[second]:
                nums.pop(second)
            else:
                first,second=first+1,second+1
        return(len(nums))