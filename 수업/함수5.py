# 함수 사용의 순서
# 1) 함수를 정의한다
# 2) 정의된 한수를 호출한다

# Call-by-vlaue, Call-by-reference (기말)

bar = [20, 30, 40] 

def foo(argList): # Call-by-reference
    argList[2] = 100
    argList[0] = 300

foo(bar) 

print(bar)

# 야구게임 # 단어 두개 풀어보기