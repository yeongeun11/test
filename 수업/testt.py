# 1. 컴퓨터 난수 생성
import random

# 1-1. 중복되지 않은 정수 3개
# 중복되지 않은 경우만 리스트로 받기
com_list = [] # 랜덤 난수 빈 리스트 생성

def com_choice():    
    while True:   # 중복되지 않은 3개의 수 뽑을 때 까지 반복
        com_num = random.randint(1,9) #1~9까지의 수 중에서 선택 
        
        if com_num not in com_list: # 리스트에 선택 한 숫자가 없다면
            com_list.append(com_num) # 리스트에 추가
        
        if len(com_list) == 3: # 1-1 충족시 종료
            break

com_choice()
print(com_list)

play_num = 1
out_count = 0

while True:
    strike_count = 0
    ball_count = 0
    user_list = []
    
    # 2. 플레이어 입력
    user_list = list(map(int, input(f"시도 {play_num}: ").split()))
    print(user_list)

    #3. 게임 실행
    for i in range(3): # 0~3까지 
        if com_list[i] in user_list: # 유저 리스트 안에 값이 있다면
            if com_list[i] == user_list[i]:
                strike_count += 1
            else:
                ball_count += 1
    
    if strike_count == 0 and ball_count == 0:
        out_count +=1
    
    play_num += 1

    print(f"결과: 스트라이크 :{strike_count} 볼 : {ball_count} 아웃 : {out_count}")
    
    if play_num == 5:
        print("시도횟수 5회 초과")
        print("정답",com_list)
        break
    
    if out_count == 2:
        print("아웃횟수 2회 초과")
        print("정답",com_list)
        break
    
    if strike_count == 3:
        print("정답입니다")
        print("정답",com_list)
        break