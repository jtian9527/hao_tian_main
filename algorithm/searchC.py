class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = int((end + start) / 2)
            if nums[mid] == target:
                return mid
            # 如果前半端有序
            elif nums[mid] >= nums[start]:
                # 如果taget位于前半段，则搜索前半段，否则后半段
                if nums[start] <= target and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            # 如果后半段有序 nums[mid] < nums[start]:
            else:
                # 如果taget位于前半段，则搜索前半段，否则后半段
                if nums[mid] < target and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1


if __name__ == '__main__':
    nums = [5, 1, 3]
    target = 5
    solution = Solution()
    print(solution.search(nums, target))
