class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=[i for i in s if (i.isalpha() or i.isdigit())]
        return s==s[::-1]