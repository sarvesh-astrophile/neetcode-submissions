class Solution:
    def isPalindrome(self, s: str) -> bool:
        truncated_s = ""
        for char in s:
            if self.isAlphanum(char):
                truncated_s += char.lower()

        i, j = 0, len(truncated_s) - 1
        while i < j:
            if truncated_s[i] != truncated_s[j]:
                return False

            i += 1
            j -= 1

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
