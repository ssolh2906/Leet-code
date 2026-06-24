from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = defaultdict(int)

        for c in s:
            char_count[c] += 1

        for c in t:
            char_count[c] -= 1

        for count in char_count.values():
            if count != 0:
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    assert s.isAnagram("anagram","anagram") == True
    assert s.isAnagram("anaagram","anagram") == False
    assert s.isAnagram("anagram","nanagram") == False



    print("All test succeeded")
