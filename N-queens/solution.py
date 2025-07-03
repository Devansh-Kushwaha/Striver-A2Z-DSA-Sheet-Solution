class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        occupiedCols=set()
        options=set(range(n))
        answers=[]
        queens=[-1]*n
        def valid(row,col):
            for i in range(row):
                if row-i==abs(col-queens[i]):
                    return False
            return True
        def setQueen(row):
            if row==n:
                answers.append(tuple(queens))
            available = options-occupiedCols
            for col in available:
                if valid(row,col):
                    queens[row]=col
                    occupiedCols.add(col)
                    setQueen(row+1)
                    queens[row]=-1
                    occupiedCols.remove(col)
        setQueen(0)
        empty="."*n
        ans=[]
        for queens in answers:
            ans.append([])
            for i in queens:
                ans[-1].append(empty[:i]+'Q'+empty[i+1:])
        return ans
