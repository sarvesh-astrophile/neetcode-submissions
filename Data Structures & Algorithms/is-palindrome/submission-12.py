class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while not self.isAlphanumeric(s[l]) and l < r:
                l += 1
            while not self.isAlphanumeric(s[r]) and l < r:
                r -= 1

            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False

        return True

    def isAlphanumeric(self, s: str) -> bool:
        if (
            ord("a") <= ord(s) <= ord("z")
            or ord("A") <= ord(s) <= ord("Z")
            or ord("0") <= ord(s) <= ord("9")
        ):
            return True
        else:
            return False
