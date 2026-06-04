class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = []
        alphabet_set = set(list("abcdefghijklmnopqrstuvwxyz"))
        num_set = set(list("0123456789"))
        for char in s:
            char = char.lower()
            if char in alphabet_set or char in num_set:
                s_list.append(char)

        i, j = 0, len(s_list) - 1
        while i <= j:
            if s_list[i] != s_list[j]:
                return False
            i += 1
            j -= 1

        return True
