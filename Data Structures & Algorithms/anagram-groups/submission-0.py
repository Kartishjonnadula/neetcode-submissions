class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        d=defaultdict(list)
        for word in strs:
            c=[0]*26
            for i in word:
                c[ord(i)-ord('a')]+=1
            d[tuple(c)].append(word)
        # print(d.values())
        return list(d.values())
        