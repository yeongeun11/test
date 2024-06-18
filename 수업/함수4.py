

# 함수 사용의 순서
# 1) 함수를 정의한다
# 2) 정의된 한수를 호출한다

# 한 개의 정수를 키보드로부터 입력 받아 "짝수", "홀수"를 판별하여 화면에 출력
# 함수로 작성 

def get_even_odd():
    input_value = int(input("입력: "))

    if input_value % 2 == 0:
        print("짝수")
    else:
        print("홀수")


input_vlaue = int(input("입력: "))
print(get_even_odd(input_vlaue))



# 함수 사용의 순서
# 1) 함수를 정의한다
# 2) 정의된 한수를 호출한다

# 함수에 인자 값 4개를 입력 받아 합계와 평균을 반환하는 함수를 작성하라
# 그리고 반환된 합계와 평균을 화면에 출력하라

def get_sum_arg(arg1, arg2, arg3, arg4,):
    sum = arg1 + arg2 + arg3 + arg4

    avg = sum / 4

    return sum, avg # 반환값이 두 개 이상이면 tuple로 변환 후 반환한다. 

# print(type(get_sum_arg(1, 2, 3, 4)))


sum, avg = get_sum_arg(1, 2, 3, 4)

sum, avg = (20, 2.5)

print(sum, avg)


# 함수 사용의 순서
# 1) 함수를 정의한다
# 2) 정의된 한수를 호출한다

# Call-by-vlaue, Call-by-reference

bar = 3

def foo(bar):
    bar = bar + 1
    print("1: ", bar)

foo(bar)

print("2: ", bar)




