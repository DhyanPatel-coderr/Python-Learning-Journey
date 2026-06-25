'''Given two strings, a text string txt and a pattern string pat, both consisting of lowercase English alphabets. Return the starting indices (0-based) of all the occurrences of the pattern string pat in the text string txt.

Note: Return an empty list in case of no occurrences of pattern.

Examples:

Input: txt = "geeksforgeeks", pat = "geek"
Output: [0, 8]
Explanation: The string "geek" occurs twice in txt, one starts at index 0 and the other at index 8.'''

class Solution:
    def search(self, txt, pat):
        ans = []

        for i in range(len(txt)-len(pat)+1):
            if txt[i:i+len(pat)] == pat:
                ans.append(i)
        return ans

result = Solution().search("GeeksforGeeks","Geeks")
print(f"Result : {result}")