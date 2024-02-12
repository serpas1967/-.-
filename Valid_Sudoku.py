class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        flag = True
        for i in range(9):
            for el in set(board[i]).difference('.'):
                if board[i].count(el) != 1:
                    flag = False
                    break
        for j in range(9):
            col = [board[i][j] for i in range(9)]
            for el in set(col).difference('.'):
                if col.count(el) != 1:
                    flag = False
                    break
        for sq in range(0, 9, 3):
            start_horisont, v, shift = 0, 0, 3
            square = []
            for v in range(0, 9, 3):
                for h in range(0, 9, 3):
                    for i in range(3):
                        # square += [board[v + i][start_horisont: start_horisont + shift]]
                        square.extend(board[v + i][start_horisont: start_horisont + shift])
                    for el in set(square).difference('.'):
                        if square.count(el) != 1:
                            flag = False
                            break
                    square = []
                    start_horisont += shift
                start_horisont = 0
        return flag


ex = Solution()
board =[[".",".",".",".","5",".",".","1","."],
        [".","4",".","3",".",".",".",".","."],
        [".",".",".",".",".","3",".",".","1"],
        ["8",".",".",".",".",".",".","2","."],
        [".",".","2",".","7",".",".",".","."],
        [".","1","5",".",".",".",".",".","."],
        [".",".",".",".",".","2",".",".","."],
        [".","2",".","9",".",".",".",".","."],
        [".",".","4",".",".",".",".",".","."]]

print(ex.isValidSudoku(board))

for i in range(0, 9, 3):
    print(i)

my = [[i+j for i in range(9)] for j in range(9)]
for row in list(my):
    print(row)


"""разбить квадрат 9*9 на последовательные(вначале по горизонтали(по 3), потом сместившись(на 3) по вертикали) квадратики 3*3"""
start_h, v, shift = 0, 0, 3
new = []
for v in range(0,9,3):
    for h in range(0,9,3):
        for i in range(3):
            new += [my[v + i][start_h: start_h + shift]]
        start_h += shift

        print("new",f'{v}')
        for row in new:
            print(row, end=",")
            print()
        new = []
    start_h = 0
