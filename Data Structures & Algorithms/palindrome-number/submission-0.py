class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        num = str(x)
        l, r = 0, len(num) -1
        while l < r:
            if num[l] != num[r]:
                return False

            l += 1
            r -= 1

        return True