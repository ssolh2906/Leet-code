from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = []
        p_product = 1

        surf = []
        s_product = 1
        for i in range(len(nums)):
            p_product *= nums[i]
            pref.append(p_product)
            s_product *= nums[-i-1]
            surf.insert(0,s_product)

        pref.insert(0,1)
        surf.append(1)

        print(pref)
        print(surf)

        # result = list(map(lambda x: x * 2, [1, 2, 3]))
        result = list(map(lambda x: pref[x] * surf[x+1], range(len(nums))))
        print(result)
        return result




if __name__ == "__main__":
    s = Solution()
    assert s.productExceptSelf([1,2,3,4]) == [24,12,8,6]
    assert s.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]

