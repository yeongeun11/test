




# 함수 호출 시 입력 값을 전달 할 수 있다.
# -> 1) Argument(인자 값)
# -> 2) Parameter(매개변수)

def get_sum (age_a, age_b, age_c):
    sum = age_a, age_b, age_c

    return sum


print(get_sum(1, 2, 3))
print(get_sum(4, 5, 6))

print("------------")

print(get_sum(7, 8, 9))

# -------------------------------------------------

def get_sum_avg (age_a, age_b, age_c):
    
    sum = age_a, age_b, age_c

    avg = sum/ 3

    return sum, avg # -> (sum, avg)
    # 함수  반환 값이 두 개 이상이면 -> 자동으로 tuple 자료형으로 구성 후 반환

    sum, avg = get_sum_avg(1, 2, 3)

    # call-by-value, call-by-reference



    