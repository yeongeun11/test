# while

# while 조건식:
#    참 일때 실행되는 문장

# 키보드로부터 정수를 입력 받고, 양수일 경우 출력,
# 음수 또는 0인 경우 재입력 -> 양수가 입력 될 때까지

# while True:
#     input_value = int(input("값 입력: "))

#     # 탈출!!! -> 입력 값이 양수 일 경우
#     if input_value > 0:
#         break

# while 문을 이용하여 1에서 10까지 출력하는 프로그램을 작성하라.
# n = 1

# while n <= 10:
#     print(n)
#     n += 1

bar = ["hello", "world", "Richard"]
# found_word = False # Flag 변수 -> 깃발 : Boolean

for word in bar:

    if word == "world":
        print("단어를 찾았음")
        # found_word = True
        break
else:
    print("단어를 찾지 못했음.")

# if not found_word: 