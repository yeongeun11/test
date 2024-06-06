# 다음과 같이 출력하는 프로그램을 작성하시오
# 1, 3, 5, 7, 9, 11, 13, 15, 17, 19
# 조건 : for 문을 사용해서

for value in range(1, 20):
    if value % 2 != 0:
        print(value, "\t", end="")