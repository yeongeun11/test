# 리스트를 사하기 위해서는 리스트를 생성
bar = []
foo = list()

# CRUD

# Create : 원소 삽입
bar.append(10) 
bar.append(20) 

# [10, 20]

bar.insert(1,     100) # [10, 100, 20]

# Read
# bar [10, 100, 20]
for index in range(0, len(bar)): # 0, 3 : len(리스트) -> 리스트의 원소 개수
    print(bar[index]) # index -> 2