# -*- coding: utf-8 -*-
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        while start < end:
            mid = start + (end-start)/2
            if nums[mid]>target:
                end = mid - 1
            elif nums[mid]<target:
                start = mid + 1
            else:
                return mid
        return -1
if __name__ == '__main__':
    nums = [5]
    target=5
    solution = Solution()
    print(solution.search(nums,target))
