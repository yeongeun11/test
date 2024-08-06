# 예외처리는 마지막에 구현

# 메뉴 출력
print("-"*20)
print("1. 구구단 출력")
print("2. 삼각형 출력")
print("3. 종료")

# 사용자로부터 값 입력
input_value = int(input("값을 입력하세요: "))

# 해당 메뉴 실행
if input_value == 1:
    print("구구단 실행")
elif input_value == 2:
    print("삼각형 출력")
elif input_value == 3:
    print("프로그램 종료")
else:
    print("1~3 사이 정수를 입력하세요")    

if input_value == '1':
        dan = int(input("출력할 구구단을 아래 형식으로 입력하세요 (예: 2, 2~5)"))

        if  2 <= dan <= 9:
            for num in range(1, 10):
                print(dan, "X", num, "=", dan * num  )
                break    