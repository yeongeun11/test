# 정수 3개를 입력 받아서 제일 큰 값을 출력하시오?

input_1 = int(input("1번"))
input_2 = int(input("2번"))
input_3 = int(input("3번"))

max = input_1

if max < input_2:
    max = input_2

if max < input_3:
    max = input_3
    
print(max)

