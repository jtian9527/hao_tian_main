# -*- coding: utf-8 -*-
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        leng = len(nums)
        for i in range(leng-1):
            for j in range(i+1,leng):
                if nums[i] + nums[j] == target:
                    return [i,j]

if __name__ == '__main__':
    nums = [3,2,4]
    target=6
    solution = Solution()
    print(solution.twoSum(nums,target))
