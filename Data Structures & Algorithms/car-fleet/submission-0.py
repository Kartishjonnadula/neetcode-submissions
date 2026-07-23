class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # d/s = time
        pos=[(i,j) for i,j in zip(position,speed)]
        pos.sort()
        time=[(target-pos[i][0])/pos[i][1] for i in range(len(position))]
        stack=[]
        for ele in time:
            if not stack:
                stack.append(ele)
                continue
            while stack and stack[-1]<=ele:
                stack.pop()
            stack.append(ele)
        return len(stack)
            