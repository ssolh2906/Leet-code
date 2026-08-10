from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right

        if nums[left] > target or nums[right] < target:
            return -1

        while left < right:
            if nums[left] > target or nums[right] < target:
                return -1

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif mid == left or mid == right:
                return -1

            if nums[left] < target < nums[mid]:
                right = mid
            if nums[mid] < target < nums[right]:
                left = mid


        return -1



if __name__ == "__main__":
    s = Solution()

    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    assert s.search(nums, target) == 4

    nums = [-1,0,3,5,9,12]
    target = 1
    assert s.search(nums,target) == -1