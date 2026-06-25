"""Given two binary strings s1 and s2 consisting of only 0s and 1s. Find the resultant string after adding the two Binary Strings.
Note: The input strings may contain leading zeros but the output string should not have any leading zeros.

Input: s1 = "1101", s2 = "111"
Output: 10100
Explanation:
 1101
+ 111
10100 """

class solution:
    def addBinary(self,s1,s2):
        i = len(s1) - 1
        j = len(s2) - 1
        result = []
        carry = 0

        while i>=0 or j>=0 or carry:
            if i>=0:
                bit1 = int(s1[i])
            else:
                bit1 = 0
            if j>=0:
                bit2 = int(s2[j])
            else:
                bit2 = 0

            total = bit1 + bit2 + carry

            result.append(str(total%2))
            carry = total//2

            i -= 1
            j -= 1
        
        ans = "".join(result[::-1])
        ans = ans.lstrip('0')

        return ans if ans else "0"

s1 = str(input("Enter binary s1 : "))
s2 = str(input("Enter binary s2 : "))

obj = solution()
result = obj.addBinary(s1,s2)

print(f"Addition of both binary is {result}")