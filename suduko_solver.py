class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def f():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for k in range(1, 10):
                            if check(i, j, k):
                                board[i][j] = str(k)

                                if f():
                                    return True
                                else:
                                    board[i][j] = "."

                        return False
            return True

        def check(i, j, k):
            for l in range(9):
                if board[i][l] == str(k):
                    return False

                if board[l][j] == str(k):
                    return False

                if board[3 * (i // 3) + l // 3][3 * (j // 3) + l % 3] == str(k):
                    return False

            return True

        f()
