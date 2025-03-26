class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        total_substrings = 0

        for right in range(len(s)):
            count[s[right]] += 1

            while all(count[ch] > 0 for ch in "abc"):
                total_substrings += len(s) - right  # Count substrings from left to end
                count[s[left]] -= 1  # Shrink the window from the left
                left += 1

        return total_substrings