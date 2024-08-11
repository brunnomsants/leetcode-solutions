class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        word = ""
        for i in range(len(s)):
            if s[i] in word:
                max_length = max(max_length, len(word))
                index = word.index(s[i])
                word = word[index + 1:]
            word += s[i]
        max_length = max(max_length, len(word))
        return max_length

print(Solution.lengthOfLongestSubstring(0, "pwwekw")) 