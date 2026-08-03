class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        i = 0
        sorted_nums = sorted(nums)
        result = []

        while i < len(nums) - 2:
            left = i + 1
            right = len(nums) - 1

            while left < right:
                print(i, left, right)
                print(sorted_nums[i], sorted_nums[left], sorted_nums[right])
                three_sum = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                print("three sum: ", three_sum)

                if three_sum > 0:
                    right -= 1
                    while sorted_nums[right] == sorted_nums[right + 1] and left < right:
                        right -= 1

                elif three_sum < 0:
                    left += 1
                    while sorted_nums[left] == sorted_nums[left - 1] and left < right:
                        left += 1
                else:
                    result.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    right -= 1
                    left += 1
                    while sorted_nums[left] == sorted_nums[left - 1] and left < right:
                        left += 1
                    while sorted_nums[right] == sorted_nums[right + 1] and left < right:
                        right -= 1


            i += 1
            while sorted_nums[i] == sorted_nums[i-1] and i < len(nums) - 2:
                i += 1

        print(result)
        return result


if __name__ == "__main__":
    s = Solution()
    # nums = [-1, 0, 1, 2, -1, -4]
    # assert s.threeSum(nums) == [[-1, -1, 2], [-1, 0, 1]]
    #
    # nums = [0, 0, 0, 0]
    # assert s.threeSum(nums) == [[0, 0, 0]]
    #
    # nums = [-100, -70, -60, 110, 120, 130, 160]
    # assert s.threeSum(nums) == [[-100, -60, 160], [-70, -60, 130]]

    nums = [1,2,0,1,0,0,0,0]
    assert s.threeSum(nums) == [[0,0,0]]
