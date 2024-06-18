

# # 함수 사용의 순서
# # 1) 함수를 정의한다
# # 2) 정의된 함수를 호출한다.


# # 정수 3개를 입력 받아 합계와 평균을 출력하는 프로그램을 작성하라

# def get_int(avg_num):
#     input_vlaues = []
#     for _ in range(avg_num):
#         input_vlaues.append(int(input("입력 값: ")))

#     return input_vlaues

# def get_sum_avg(avg_list):
    





# def get_sum():
#     input_value_1  = int(input("입력 값 : "))
#     input_value_2  = int(input("입력 값 : "))
#     input_value_3  = int(input("입력 값 : "))

# # def 함수명(매개변수):
# #     함수 호출 시 실행 명령어

# # 함수 정의 : -> 1번
# def print_name(name):
#     print(name, "님 안녕하세요:")

# # 함수 호출 : -> 2번    
# print_name("리차드")
# print_name("정영철")

# # 함수 호출 : call 



# # 함수 사용의 순서
# # 1) 함수를 정의한다
# # 2) 정의된 함수를 호출한다.


# # 정수 3개를 입력 받아 합계와 평균을 출력하는 프로그램을 작성하라.

# def get_int(arg_num):
#     input_values = []
#     for _ in range(arg_num):
#         input_values.append(int(input("입력값: ")))
        
#     return input_values

# def get_sum_avg(arg_list):
#     sum = 0
#     for value in arg_list:
#         sum += value
    
#     avg = sum / len(arg_list)
    
#     return sum, avg

# def get_sum(arg_list):
#     sum = 0
#     for value in arg_list:
#         sum += value
    
#     return sum
 

# input_list = get_int(13)

# sum, avg = get_sum_avg(input_list)

# print(sum, avg)