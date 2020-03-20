'''
88. 合并两个有序数组
https://leetcode-cn.com/problems/merge-sorted-array/
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 num1 成为一个有序数组。
解题思路:
倒序对比插入nums1的尾部，通过对比nums1比较大的移到后面，最后在指针p2之前的位置用nums2覆盖nums1
'''
        
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        
        while p1 >= 0 and p2 >= 0:
           
            if nums1[p1] < nums2[p2]: 
                nums1[p] = nums2[p2]
                p2 -= 1
            elif nums1[p1] >= nums2[p2]:
                nums1[p] =  nums1[p1]
                p1 -= 1
            p -= 1

        nums1[:p2+1] = nums2[:p2+1]