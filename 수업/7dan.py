# 1 ~ 100 사이 정수 중, 3의 배수와 7의 배수를 출력하시오.

for value in range(1, 101):
    if value % 3 == 0 or value % 7 == 0:
        print(value, "\t", end="")
