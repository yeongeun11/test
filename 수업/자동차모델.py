model = input("자동차 모델을 입력 하세요: ")

# M1, M2, M4, M6, M8, M9, M3, M5, M7    -> BMW, 
# Y, X          -> Tesla, 
# ES, LS        -> Lexus
# G80, G90      -> Hyundai
# 이외 모델      -> "알수 없는 모델입니다."
list_bmw = ["M1", "M2", "M4"]
list_tesla = ["Y", "X"]
list_lexus = ["ES", "LS"]
list_genesis = ["G80", "G90"]

list_model = "list_bmw, list_tesla, list_lexus, list_genesis"

# 회사 목록을 가지고 온다. 반복 -> 4회 bmw, tesla, lexus, genesis
# 세로 반복
make_name_list = ["bmw", "tesla", "lexus", "genesis"]
index_count = 0

for maker_list in list_model:
    # 회사별 자동차 모델을 가지고온다 -> 반복 회수? 회사 별 모델 개수에 따라
    # 가로 반복
    for model_in_list in maker_list: 
        if model == model_in_list:
            print("make 값 설정")






