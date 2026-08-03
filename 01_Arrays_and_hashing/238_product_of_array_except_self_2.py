from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_len = len(nums)
        pre = [1] * (num_len + 2)
        nums.insert(0,1)
        nums.append(1)
        post = 1
        for i in range(num_len+1):
            pre[i] *= nums[i] * pre[i-1]
        print(pre)

        post_prod = 1
        for i in range(num_len):
            post_prod *= nums[-i-1]
            print(f"post prod: {post_prod}, pre[-i] : {pre[-i-2]}")
            pre[-i-3] *= post_prod
            print(post_prod)
        pre.pop(-1)
        pre.pop(-1)
        print(post_prod)
        print(pre)


        return pre


if __name__ == "__main__":
    s = Solution()
    s.productExceptSelf([2,3,4,5])
    assert s.productExceptSelf([1,2,3,4]) == [24,12,8,6]
    assert s.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]

