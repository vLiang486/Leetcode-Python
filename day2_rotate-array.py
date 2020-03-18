'''
189. 旋转数组
https://leetcode-cn.com/problems/rotate-array/
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
解题思路:
分为2部分，移动的K位置的左边和右边，拼接后为最后的完整数组
        for i in range(k):
        	length = len(nums)
            nums[:] = nums[length-i:]+nums[:length-i]
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        nums[:] = nums[length-k:]+nums[:length-k]
