from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], key: int) -> List[int]:
        '''
        dd = defaultdict(int)
        for n in nums:
            dd[n] += 1

        s_dd = sorted(dd.items(), key=lambda item: item[1], reverse=True)

        kth_count = s_dd[k - 1][1]
        result = []

        for i in range(0, len(s_dd)):
            curr_count = s_dd[i][1]
            if curr_count >= kth_count:
                result.append(s_dd[i][0])
            else:
                break

        return result
        '''

        # Bucket sort

        dd = defaultdict(int)
        for n in nums:
            dd[n] += 1

        len_nums = len(nums)
        bucket = []
        for n in range(len_nums):
            bucket.append([])

        for key, val in dd.items():
            bucket[val - 1].append(key)

        result = []
        j = 0
        for i in reversed(range(len_nums)):
            if len(bucket[i]) != 0:
                result.extend(bucket[i])
                j += len(bucket[i])
                if j == k:
                    break

        return result


if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    assert s.topKFrequent(nums, k) == [1, 2]

    nums = [1]
    k = 1
    assert s.topKFrequent(nums, k) == [1]

    nums = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
    k = 2
    assert s.topKFrequent(nums, k) == [1, 2]

    nums = [3, 0, 1, 0]
    k = 1
    assert s.topKFrequent(nums, k) == [0]

    print("All test succeeded")
