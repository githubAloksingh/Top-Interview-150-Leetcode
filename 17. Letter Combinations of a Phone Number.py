class Solution:
    def __init__(self):
        self.result=[]
    
    def solve(self, idx, digits, temp, mp):
        if idx>=len(digits):
            self.result.append("".join(temp))
            return
        ch=digits[idx]
        str=mp[ch]

        for char in str:
            temp.append(char)
            self.solve(idx+1,digits, temp,mp)
            temp.pop()
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        mp = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }
        self.result=[]
        temp=[]
        self.solve(0,digits,temp,mp)
        return self.result


