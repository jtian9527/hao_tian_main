class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 因为左右都是负无穷，所以如果找到一个数比其相邻一个数大，那么按照这个方向找肯定有峰值
        start = 0
        end = len(nums) - 1
        if len(nums) <= 1: return 0
        if len(nums) == 2:
            if nums[0] >= nums[1]:
                return 0
            else:
                return 1
        while start <= end:
            mid = int((start + end) / 2)
            if mid ==0:
                return 0
            elif mid == len(nums)-1:
                return  len(nums)-1
            else:
                if nums[mid + 1] < nums[mid] and nums[mid] > nums[mid - 1]:
                    return mid
                elif nums[mid + 1] < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
        return start


if __name__ == '__main__':
    nums = [3,4,3,2,1]
    solution = Solution()
    print(solution.findPeakElement(nums))
