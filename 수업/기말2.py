import random


def print_bingo_board(arg_list, col_num = 3):
    for index in range(len(arg_list)):
        print(arg_list[index], "\t", end="")
        
        if (index + 1)  % col_num == 0:
            print()

# N 값 입력
N = 3
bingo_element_num = N * N
# N X N 빙고 보드 작성: 1차원 배열, 1~36사이의 중복되지 않은 정수


bingo_board = [ 1, 2, 3,\
                4, 5, 6, \
                7, 8, 9]

print_bingo_board(bingo_board)

bingo_count = 0

# 가로 확인 알고리즘
for row in range(N):
    for col in range(N):
        if bingo_board[col] != "*":
            break
    else:
        bingo_count += 1

