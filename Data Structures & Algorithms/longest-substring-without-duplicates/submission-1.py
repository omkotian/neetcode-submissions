class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        for start in range(len(s)):
            seen = set()

            for end in range(start, len(s)):
                if s[end] in seen:
                    break

                seen.add(s[end])
                longest = max(longest, len(seen))

        return longest