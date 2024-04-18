class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        max_length = 0
        start = 0
        char_index = {}
        
        for i, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            else:
                max_length = max(max_length, i - start + 1)
            char_index[char] = i
        print(char_index["b"])
        print(enumerate(s))
        return max_length
print(Solution.lengthOfLongestSubstring(0, "abcabcbb")) 

class Solution:
    def lengthLongestSubstring(self, s: str) -> int:
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

print(Solution.lengthLongestSubstring(0, "pwwekw")) 