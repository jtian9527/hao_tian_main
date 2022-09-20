# class Solution:
#     def searchRange(self, nums, target):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         leng = len(nums)
#         if leng == 0:
#             return [-1, -1]
#         firstPosition = self.findFirstPosition(nums, target)
#         if firstPosition == -1:
#             return [-1, -1]
#         lastPosition = self.findLastPosition(nums, target)
#         return [firstPosition, lastPosition]
#
#     def findFirstPosition(self, nums, target):
#         left = 0
#         right = len(nums) - 1
#         while left < right:
#             # 向下取整
#             mid = int((left + right) / 2)
#             if nums[mid] < target:
#                 left = mid + 1
#             elif nums[mid] == target:
#                 # 中间元素的右边一定不是第一个位置
#                 right = mid
#             else:
#                 # nums[mid] > target
#                 right = mid - 1
#         if nums[left] == target:
#             return left
#         else:
#             return -1
#
#     def findLastPosition(self, nums, target):
#         left = 0
#         right = len(nums) - 1
#         while left < right:
#             # 向上取整
#             mid = int((left + right + 1) / 2)
#             if nums[mid] < target:
#                 left = mid + 1
#             elif nums[mid] == target:
#                 # 中间元素的右边一定不是第一个位置
#                 left = mid
#             else:
#                 # nums[mid] > target
#                 right = mid - 1
#         return left

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0: return [-1,-1]
        first_index = find_first_target(nums,target)
        if first_index == -1:
            return [-1,-1]
        end_index = find_end_target(nums,target)
        return [first_index,end_index]

        def find_first_target(nums,target):
            start = 0
            end =len(nums)-1
            while start < end:
                mid = start + (end-start)/2
                if nums[mid]<target:
                    #目标在中值右侧，则start = mid + 1，因为mid并不等于target
                    start = mid + 1
                elif nums[mid] >target:
                    #目标在中值左侧，则 end = mid -1,因为mid并不等于target
                    end = mid - 1
                else:
                    #目标在中值，则end = mid，因为mid在中值上，这样第一个数慢慢靠近开始位置
                    end = mid
            if nums[end] == target:
                return start
            else:
                return -1

        def find_end_target(nums,target):
            start = 0
            end =len(nums)-1
            while start < end:
                mid = start + (end-start)/2
                if nums[mid]<target:
                    #目标在中值右侧，则start = mid + 1，因为mid并不等于target
                    start = mid + 1
                elif nums[mid] >target:
                    #目标在中值左侧，则 end = mid -1,因为mid并不等于target
                    end = mid - 1
                else:
                    #目标在中值，则end = mid，因为mid在中值上，这样第一个数慢慢靠近开始位置
                    start = mid
            if nums[start] == target:
                return start
            else:
                return -1

if __name__ == '__main__':
    nums = [2, 2, 3, 4, 5, 5, 5, 6, 7]
    target = 5
    solution = Solution()
    print(solution.searchRange(nums, target))
