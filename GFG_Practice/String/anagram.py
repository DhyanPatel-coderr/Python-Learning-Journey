"""Given two non-empty strings s1 and s2, consisting only of lowercase English letters, determine whether they are anagrams of each other or not.
Two strings are considered anagrams if they contain the same characters with exactly the same frequencies, regardless of their order.

Examples:

Input: s1 = "geeks" s2 = "kseeg"
Output: true 
Explanation: Both the string have same characters with same frequency. So, they are anagrams."""

class Solution:
    def areAnagrams(self, s1, s2):
        
        freq = {}
        
        if len(s1) != len(s2):
            return False
            
        for ch in s1:
            freq[ch] = freq.get(ch,0) + 1
                
        for ch in s2:
            if ch not in freq:
                return False
            
            freq[ch] -= 1

            if freq[ch] < 0:
                return False
                 
        return all(value == 0 for value in freq.values())
    
s1 = str(input("Enter string s1 : "))
s2 = str(input("Enter string s2 : "))

obj = Solution()
result = obj.areAnagrams(s1,s2)

print("Strings are anagrams") if result else print("Strings are not anagrams")