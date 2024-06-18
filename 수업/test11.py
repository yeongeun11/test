# a) 모든 파라메터에 초기 값을 설정한다.
# b) 초기 값을 가지는 파라메터는 제일 뒷쪽에 위치한다.


# variable prrameter : 가변 파라메터
# 1) *
# 2) **
        # * -> 가변 : tuple로 받겠다
        #               
def foo(*args):
    print(len(args))
    for value in args:
        print(value)

foo(1)
foo(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12) # 12


def bar(*args):
    if len(args) == 1:
        start = args[0]
        end = start + 1
    elif len(args) == 2:
        start, end = args
    else:
        return

    for dan in range(start, end + 1):
        for num in range(1, 10):
            print(f"{dan} X {num} = {dan * num}")        
bar(2)
bar(2, 3)


        # * -> 가변 : Dicionary로 받겠다
        #               key : value        
def foo(**args):
    print(len(args))

    for key, value in args.items():
        print(f"key: {key}, value : {value}")

foo(test = 2, king = 3) # 1
foo(test = 2, king = 3, lion = 4) # 4    