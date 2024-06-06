# 입력 값이 홀수이면서 3의 배수 값이면 출력하시오.

input_value = int(input("정수 값 입력: "))

if input_value % 2 == 1:
    if input_value % 3 == 0:
        print(input_value)

if input_value % 2 == 1 and input_value % 3 == 0:
    print(input_value)
            