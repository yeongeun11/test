# 1이상 30이하의 정수 중에, 짝수이면서 5의 배수를 출력하시오

for value in range(1, 31):
    if value % 2 == 0 and value % 5  == 0:
        print(value, "\t", end="")