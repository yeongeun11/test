result_1 = 3 // 2
result_2 = 3 / 2

print(result_1, result_2)

for divisor in range(6):
    print(divisor%3)
# 나머지 연산은 특정 패턴을 찾기 위해 빈번하게 사용
# 예) 특정 반복문 내에서 3번째 반복마다 특정 명령어 실행

count = 1

for dan in range(2, 10):
    for num in range(1, 10):
        print(dan, " X ", num, " = ", (dan*num))

        if count %  3 == 0:
            print("==========================")

        count += 1    