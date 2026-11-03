class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
        # sub_start = 0
        # sub_mid = len(nums) // 2
        # sub_last = len(nums) - 1
        # print(f"s:{sub_start}, m: {sub_mid}, l: {sub_last} ")
        # while sub_start < sub_mid < sub_last:
        #     if nums[sub_start] > nums[sub_mid]:
        #         # min is in the left subarray
        #         sub_last = sub_mid
        #     elif nums[sub_mid] > nums[sub_last]:
        #         # min is in the right subarray
        #         sub_start = sub_mid
        #     else:
        #         return 0
        #     sub_mid = (sub_start + sub_last) // 2
        #     print(f"s:{sub_start}, m: {sub_mid}, l: {sub_last} ")
        #
        # return sub_mid


if __name__ == "__main__":
    s = Solution()
    print(s.findMin([0,1,2,3,4,5,6,7,8,9,10]))
    print(s.findMin([4,5,6,7,0,1,2]))