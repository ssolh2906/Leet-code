from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = defaultdict(list)
        for s in strs:
            letters = list(s)
            letters.sort()
            sorted_str = ''.join(letters)
            str_dict[sorted_str].append(s)
        return list(str_dict.values())


if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]) )
