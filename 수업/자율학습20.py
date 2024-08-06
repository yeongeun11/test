# 구구단과 삼각형 출력 프로그램
import random
# 사용자에게 메뉴를 출력하고 입력 받기
while True:
    print("1. 구구단 출력")
    print("2. 랜덤값 삼각형 출력")
    print("3. 종료")

    menu = input("원하는 메뉴 번호를 입력하세요: ")
    
    if menu == '1':
        dan = int(input("출력할 구구단을 아래 형식으로 입력하세요 (예: 2, 2~5)"))

        if  2 <= dan <= 9:
            for num in range(1, 10):
                print(dan, "X", num, "=", dan * num  )
                break


# 입력이 1 ~ 3 범위 외의 값일 경우 에러 메시지 출력 후 재입력 요구하기

# 각 기능에 따른 추가 입력 요구와 에러 처리를 포함하기

# 구구단 출력
# 