from typing import List, Any


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        max_area = self.get_area(height, left, right)

        while right > left:
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

            max_area = self.update_max_area(height, left, max_area, right)

        return max_area

    def update_max_area(self, height: list[int], left: int, max_area, right: int) -> Any:
        move_right_area = self.get_area(height, left, right)
        if max_area < move_right_area:
            max_area = move_right_area
        return max_area

    def get_area(self, height, left, right):
        return (right - left) * min(height[right], height[left])


if __name__ == "__main__":
    s = Solution()
    height = [1, 2, 3, 2]
    assert s.maxArea(height) == 4

    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert s.maxArea(height) == 49

    height = [1,1]
    assert s.maxArea(height) == 1

    height = [8,7,2,1]
    assert s.maxArea(height) == 7

    height = [2, 3, 4, 5, 18, 17, 6]
    assert s.maxArea(height) == 17