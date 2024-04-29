# 정수를 입력 받아, 입력받은 정수를 화면에 출력하라. <- 무한반복
# 언제까지? 3의 배수 또는 4의 배수가 입력되면 프로그램을 종료하시오.

while True:
    import_value = int(input("정수 값 입력: "))

    if import_value % 3 == 0 or import_value % 4 == 0:
        break

print(import_value)


for count in range(1, 10):
    print(count % 5, "\t", end="")


# 정수를 입력 받아, 입력받은 정수를 화면에 출력하라. <- 무한반복
# 언제까지? 3의 배수 또는 4의 배수가 입력되면 프로그램을 종료하시오.

# for count in range(1, 10):
#     print(count % 5, "\t", end="")
    #1       2        3       4      0      1      2      3      4

print(5/2)  # 2.5
print(5//2) # 2
print(5%2)  # 1  

# 아래 함수는 문자열을 입력 받아, 입력 받은 문자열의 길이를 반환하는 함수 

foo = "hello"


count = 0
for value in foo:
    count += 1

print(count)
