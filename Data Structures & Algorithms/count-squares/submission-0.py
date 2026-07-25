class CountSquares:

    def __init__(self):
        self.points={}
        

    def add(self, point: List[int]) -> None:
        new_x,new_y=point
        if (new_x,new_y) not in self.points:
            self.points[(new_x,new_y)]=0
        self.points[(new_x,new_y)]+=1
    def count(self, point: List[int]) -> int:
        px,py=point
        ans=0
        for tx,ty in self.points:
            if abs(px-tx)==abs(py-ty) and px!=tx and py!=ty:
                if (tx,py) in self.points and (px,ty) in self.points:
                    ans+=self.points[(tx,ty)]*self.points[(tx,py)]*self.points[(px,ty)]
        return ans
            