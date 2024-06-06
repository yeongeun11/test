

# 리스트 컴플리헨션 -> 리스트 내 원소를 동적으로 생성하는 방법
# 수식 for 선택항목 in 선택 리스트 if 조건식

#
# for else
# while else
# done_break = False

for value in range(3): # N -> N번 반복, 0 -> n-1, 5 -> 5번 반복, 0 -> 4

    input_value = int(int("입력 값: "))

    if input_value <= 0:
        done_break = True
        msg = "break 사용"
        break

    print(value)

# break
# continue
# pass (python)

# for i in range(1, 3):
#     for j in range(1, 4):
#         if i == 2:
#             break
#         print(i, ":", j)    

