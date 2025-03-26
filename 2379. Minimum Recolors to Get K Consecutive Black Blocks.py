class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        current_count = sum(1 for i in range(k) if blocks[i] == 'W')
        min_count = current_count

        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                current_count -= 1
            if blocks[i] == 'W':
                current_count += 1
            min_count = min(min_count, current_count)

        return min_count