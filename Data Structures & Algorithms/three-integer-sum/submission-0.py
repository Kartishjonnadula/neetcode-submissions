class Solution:
    def threeSum(self, a: List[int]) -> List[List[int]]:
        a.sort()
        ans = []
        for i in range(len(a)):
            if i != 0 and a[i] == a[i - 1]:
                continue
            start = i + 1
            end = len(a) - 1
            target = -1 * a[i]
            while start < end:
                if target == a[start] + a[end]:
                    ans.append([a[i], a[start], a[end]])
                    while start < end and a[start] == a[start + 1]:
                        start += 1
                    while start < end and a[end] == a[end - 1]:
                        end -= 1
                if a[end] + a[start] > target:
                    end -= 1
                else:
                    start += 1
        return ans
