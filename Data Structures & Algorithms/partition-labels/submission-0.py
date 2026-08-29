class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen={}
        for i,j in enumerate(s):
            last_seen[j]=i
        # print(last_seen)
        res=[]
        if not s:
            return res
        prev=-1
        curr_max=last_seen[s[0]]
        for i,val in enumerate(s):
            curr_max=max(last_seen[val],curr_max)
            if i==curr_max:
                curr=curr_max-prev
                res.append(curr)
                prev=curr_max
        return res
        
            