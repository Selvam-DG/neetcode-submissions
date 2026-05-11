class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # row wise check 
        for i in range(len(board)):
            row_num = set()
            for j in range(len(board)):
                if board[i][j] != '.':
                    if board[i][j] in row_num:
                        return False
                    else:
                        row_num.add(board[i][j])
        #  column wise check
        for m in range(len(board)):
            column_num = set()
            for n  in range(len(board)):
                if board[n][m] != ".":
                    if board[n][m] in column_num:
                        return False
                    else:
                        column_num.add(board[n][m])
        # 3x3 check
        i = 0
        j = 0
        square = 0
        while square < 9:
            nums = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) *3 + i
                    col = (square%3) *3 + j
                    if board[row][col] != ".":
                        if board[row][col] in nums:
                            return False
                        else:
                            nums.add(board[row][col])
            square+=1
        return True


            