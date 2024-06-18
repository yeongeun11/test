

# # 함수 사용의 순서
# # 1) 함수를 정의한다
# # 2) 정의된 함수를 호출한다.


def sum(arg_first , arg_second):
    sum = arg_first + arg_second

    if sum < 0:
        print("음수")
        return
    
    # 함수 정의 시 return이 있어도 되고 없어도 된다. 즉 Option 이다

    return sum # 두 가지 role -> 1) 함수 종료 2) 값 반환

result = sum(2, 3) # result -> 5
print(result)

result = sum(-2 ,-3) # result -> None
print(result)