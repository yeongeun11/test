for i in range(1, 3):
    for j in range(1, 4):
        if i == 2:
            break
        print(i, ":", j)   

# ***
# ***
# ***
# ***
for row in range(4):
    for _ in range(3):
        print("*", end = "") # ***

    if row != 3:
        print("")

for k in range(1, 5):
    for i in range(1, 3): # 1 -> 2
        for j in range(1, 4):# 1 -> 3
              if i == 2:
                break
              print(i, ":", j)   

# break 동작 절차:
# 1) 위로 올라간다.
# 2) 첫 번째 만나는 반복을 종료한다          

#i가 1일때
# 1:1 # j가 1
# 1:2 # j가 2    
# 1:3 # j가 3

#i가 2일때
# 2:1 # j가 1
# 2:2 # j가 2    
# 2:3 # j가 3


