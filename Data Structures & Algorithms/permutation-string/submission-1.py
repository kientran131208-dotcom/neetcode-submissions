class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def check_COUNT(s):
            counting = {}
            for c in s:
                counting[c] = counting.get(c, 0) + 1
            return counting

        m = len(s1)
        n = len(s2)

        if m > n:
            return False

        target = check_COUNT(s1)
        window = check_COUNT(s2[:m])

        if target == window:
            return True

        for i in range(m, n):
            # Remove the character leaving the window
            left_char = s2[i - m]
            window[left_char] -= 1

            if window[left_char] == 0:
                del window[left_char]

            # Add the new character entering the window
            right_char = s2[i]
            window[right_char] = window.get(right_char, 0) + 1

            if target == window:
                return True

        return False