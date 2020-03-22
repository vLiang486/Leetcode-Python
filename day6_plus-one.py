'''
66. 加一
https://leetcode-cn.com/problems/plus-one/
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
解题思路:
数组转到整数+1后转回数组
'''
        
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(lambda x:str(x),digits)))+1
        return [int(x) for x in str(num)]