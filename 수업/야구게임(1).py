# 야구 게임 
import random
# 랜덤으로 컴퓨터 난수 3개 생성 [list]
cp_li = []

while len(cp_li) < 3:
    random_n = random.randint(0, 9)
    flag = True
    for i in cp_li:
        if i == random_n:
            flag = False
    if flag:
        cp_li.append(random_n)  



out = 0
count = 0

# 게임 시작 
while True:
    # 게임 시도 횟수
    count += 1
    # 플레이어 입력 0 ~ 9 사이의 정수 3개 입력 받기
    inputlist = list(map(int,input(f"시도 {count}: 입력한 숫자 - ").split()))
    strike = 0
    ball = 0
    for cp_li_index in range(3):
        for inputlist_index in range(3):
            # 자릿수가 같고 "난수 값 == 입력 값" 일 경우 strike"
            if cp_li[cp_li_index] == inputlist[inputlist_index]:
                if cp_li_index == inputlist_index:
                    strike += 1 
                else:
                    ball += 1 
    if strike == 0 and ball == 0:
        out += 1    
    # 게임 결과 출력 (아웃이 있어야 출력 함)
    if out != 0:
        print(f"결과: {strike} Strike, {ball} ball, {out} Out")
    else:
        print(f"결과: {strike} Strike, {ball} ball")
    # 게임 패배 조건
    # 시도 횟수가 5번 이상일 경우
    if count == 5:
        print("게임 종료: 패배 (시도 횟수 5회 초과)")
        break
    # 아웃 횟수가 2번 이상일 경우
    elif out == 2:
        print("게임 종료: 패배 (아웃 횟수 2번 초과)")
        break
    # 게임 승리 조건  
    # 플레이어가 컴수퓨터가 생성한 난수 값을 자리 순서대로 모두 맞출 경우
    elif strike == 3:
        print("게임 종료: 승리")
        break

# 게임 종료 후 결과 출력 
# 정답 출력 
print("정답:", *cp_li)