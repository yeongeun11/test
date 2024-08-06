
# 사용자로부터 행과 열의 수를 입력 받기 
def create_list(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def input_li(matrix, rows, cols):
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = input(f"Enter value for [{i}][{j}]: ")

def print_list(matrix):
    for row in matrix:
        print(row)

def print_2d_list(matrix):
    # 리스트 출력
    for row in matrix:
        print(" ".join(map(str, row)))

def run_program():
    # 행과 열의 수 입력 받기
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    # 2차원 리스트 생성
    matrix = create_list(rows, cols)
    
    # 리스트 값 입력
    input_li(matrix, rows, cols)
    
    # 리스트 출력
    print_2d_list(matrix)

# 프로그램 실행
run_program()