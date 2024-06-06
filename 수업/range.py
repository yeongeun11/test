# range(반복 회수)
# range(시작값, 종료값) : 시작 값은 첫 번째 증감값에 대한 적용이 가능할 때 선택
# range(시작값, 종료값, 증감값)


for value in range(5, -20, -5): # 5, 0, -5, -10, -15
    print(value)

# 1에서 20까지 정수로 구성된 리스트를 생성하세요.
# list comprehension (리스트 컴플리헨션)
#  -> 리스트 내 원소 값들을 for 문을 사용하여 동적으로 생성
#     [expression for item in item_list if condited expression]
bar = [ value for value in range(21)]
print(bar)

# 7로 초기화된 8개의 원소를 가지는 리스트를 생성하라.

# bar = [ 7 for _ in range(8)]
# print(bar)

# bar = [ value for value in range(1, 21) if value % 3== 0 ]

# 아래 리스트 중 'C'가 포함된 단어만 선택해서 리스트로 구성하라
foo = ["abc", "dcd", "ef", "gh"]

# s_list = [msg for msg in foo if "c" in msg]
# print(s_list)

# 아래 리스트 중 'C'글자 개수기 3개 이상인 단어만 선택하여 리스트로 생성하라
foo = ["abc", "dcd", "ef", "gh"]

s_list = [ word for word in foo if len(word) >= 3]

# 1에서 10사이 정수 중, 홀수는 10을 곱하고, 짝수는 20을 곱한 리스트를 생성하라
[10, 40, 30, 80, 50, 120, 70, 160, 90, 200]

# 삼항 연산자 : 참 if 조건식 else 거짓 -> 수식 
# s_list = [value * 20 if value %2 == 0 else value * 10 for value in range(1, 11)]
# print(s_list)

# s_list = [value for value in range(1, 21) if value % 3 == 0 if value % 4 == 0]
# print(s_list)

