# 양의 정수 5개를 입력 받아, 합과 평균을 출력하는 프로그램을 작성하시오.

input_value_1 = int(input("1번째 값 : "))
input_value_2 = int(input("2번째 값 : "))
input_value_3 = int(input("3번째 값 : "))
input_value_4 = int(input("4번째 값 : "))
input_value_5 = int(input("5번째 값 : "))

# 양의 정수 5개를 입력 받아, 합과 평균을 출력하는 프로그램을 작성하시오

input_num = 5

sum = 0
avg = 0.0

for trial_count in range(1, input_num + 1):
 input_value = int(input(msg))
sum = sum + input_value

avg = sum / input_num

print(sum, avg)
