# 야구 게임
import random
# 1) cp 랜덤으로 0~9중 3개의 숫자를 생성 시
cp_li = []  # 랜덤하게 생성한 숫자를 넣기 위한 리스트
while len(cp_li) < 3:
    cp_n = random.randint(0, 9) # 0~9 사이의 숫자 1개를 선택 -> random.randint(시작, 종료)

    flag = True                 # 중복되는 숫자가 없는지 확인하기 위한 flag를 True or False로 생성
    # 리스트를 반복 시켜서 한원소씩 같은 숫자가 없는지 check
    for i in cp_li:
          if i == cp_li:     # 만약에 숫자가 같으면
                flag = False             # flag를 False로 변경 
                
    # 만약에 중복된 숫자가 없으면 True이기 때문에 리스트에 추가 
    if flag:                # 참조 변수 -> 리스트의 이름
        cp_li.append(cp_n)  # 참조변수.append(리스트에 추가하고 싶은 원소)

    # 먼저 게임횟수, out횟수의 변수를 선언
game_count = 0
game_out = 0

# 3) 게임 시작(게임횟수, out횟수) !!!!!while을 사용!!!!!
while True:
    print(cp_li)
    # !!!!게임횟수 세기!!!!!!
    game_count += 1
    # 2) !!!!!! input 3개의 숫자를 동시에 입력 받기 (map) (예외 없음)!!!!!!!
    # !!!!!!!!!input_num을 리스트로 변환!!!!!!!!!
    input_li = list(map(int, input(f"시도 {game_count}: 입력한 숫자 - ").split()))
    # 게임이 반복될 때마다 strike와 ball의 횟수를 초기화
    game_strike = 0   # 원소가 같고 index 값도 같은 경우
    game_ball = 0     # 원소만 같은 경우
    
    # 3-1)index으로 결과를 확인 -> index는 리스트의 순번 (0부터 시작)
    for i in range(len(cp_li)):
        # !!!!!!!!위의 i를 j로 바꿔서 for문 만들기!!!!!!!!!
        for j in range(len(cp_li)):
            if cp_li[i] == input_li[j]:   # 만약에 리스트의 원소가 같으면
            # !!!!! strike와 ball의 횟수 세기 (+1) !!!!!! 
                if i == j:    
                    game_strike += 1  # (위의 조건이 만족되며)만약에 index값이 같으면 strike?? 아니면 ball???        
                            #(위의 조건이 만족되며) index값이 다를 때 strike?? 아니면 ball???
                else:
                    game_ball += 1
                    
    # 만약에 strike와 ball가 없으면 out 횟수 세기 (+1)
    if game_strike == 0 and game_ball == 0:
        game_out += 1
    # 3-2) 결과 출력 {}strike {}ball \ {}out
    # !!!!!! 만약에 out이 있으면 !!!!!!
    if game_out > 0:
        print(f"결과: {game_strike} Strike, {game_ball} Ball, {game_out} Out")
    # !!!!! out이 없으면 !!!!!
    else:
        print(f"결과: {game_strike} Strike, {game_ball} Ball")

        

    # !!!!!만약에 strike 횟수가 3번이상이면 msg를 정하고 brike !!!!!!
    if game_strike >= 3:
        msg = "승리"
        break
    # !!!!! 만약에 게임횟수가 5번 이상이면 msg를 정하고 brike !!!!!
    elif game_count >= 5:
        msg = "패배 (시도 횟수 5회 초과)"
        break

    # !!!!! out 횟수가 2번이상이면 msg를 정하고 brike !!!!!  과
    elif game_out >= 2:
        msg = "패배 (아웃 횟수 2회 초과)"
        break

# 4) 게임 종료 게임결과와 정답을 출력
# !!!!!! 게임 종료: (결과 msg) !!!!!!
print("게임 종료: ",msg)
print("정답:", *cp_li)
# print("정답:", *cp_li)