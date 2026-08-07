class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ''.join(c.lower() for c in s if c.isalnum())
        return text[::-1] == text