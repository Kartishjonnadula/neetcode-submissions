class Solution:
    def longestConsecutive(self, nums):
        s = set(nums)
        visited = set()
        ans = 0

        for num in s:
            if num in visited:
                continue

            visited.add(num)
            length = 1

            x = num - 1
            while x in s:
                visited.add(x)
                length += 1
                x -= 1

            x = num + 1
            while x in s:
                visited.add(x)
                length += 1
                x += 1

            ans = max(ans, length)

        return ans