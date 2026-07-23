class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={
            '1':"",
            '2':"abc",
            '3':"def",
            '4':"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":'wxyz',
        }

        ans=[]
        
        def solve(i,curr):
            if i==len(digits):
                ans.append(curr)
                return
            for letter in d[digits[i]]:
                curr+=letter
                solve(i+1,curr)
                curr=curr[:-1]
            return 
        if digits=="":
            return ans
        solve(0,"")
        return ans