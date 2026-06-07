class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not self.isAlphanum(s[i]):
                i += 1
            while j > i and not self.isAlphanum(s[j]):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True

        return True

    def isAlphanum(self, char: str) -> bool:
        if (
            ord("a") <= ord(char) <= ord("z")
            or ord("A") <= ord(char) <= ord("Z")
            or ord("0") <= ord(char) <= ord("9")
        ):
            return True
        else:
            False
