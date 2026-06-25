"""Given a string s consisting of lowercase English Letters. return the first non-repeating character in s. If there is no non-repeating character, return '$'.

Examples:

Input: s = "geeksforgeeks"
Output: 'f'
Explanation: In the given string, 'f' is the first character in the string which does not repeat."""

class Solution:
    def nonRepeatingChar(self,s):
        freq = {}
        
        for ch in s:
            freq[ch] = freq.get(ch,0) + 1        
        for ch in s:
            if freq[ch] == 1:
                return ch
        return '$'
    
s = str(input("Enter string s : "))

result = Solution().nonRepeatingChar(s)
if result == "$": print("No non repeating characters are there") 
else: print(f"First non repeating character is {result}")