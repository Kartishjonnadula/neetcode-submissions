class TimeMap:

    def __init__(self):
        self.map=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        search_space=self.map[key]
        if not search_space or timestamp<search_space[0][0]:
            return ""
        l,r=0,len(search_space)-1
        ans=0
        while l<=r:
            m=(l+r)//2
            if search_space[m][0]<=timestamp:
                ans=m
                l=m+1
            else:
                r=m-1
            
        return search_space[ans][1]

        
