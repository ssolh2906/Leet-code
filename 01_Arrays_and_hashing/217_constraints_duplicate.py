'''
2026-06-15
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/description/
Easy
'''
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False

# I tried nested iteration. Takes too long when list is long.


if __name__ == "__main__":
    s = Solution()
    assert s.containsDuplicate([1, 2, 3, 3]) == True
    assert s.containsDuplicate([1]) == False
    assert s.containsDuplicate([1, 2, 3, 4, 5, -1]) == False
    print("All test succeeded")
