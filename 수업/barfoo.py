bar = [2, 3, 4, 5, 6]
bar[1] = 20


bar[0:3] = [100, 200, 300]

# print(bar)

bar = [100, 200, 300, 400, 500, 600, 700]

# CRUD : Delete
# 원소 삭제 : 원소 한 개 삭제, 리스트 내 전체 원소 삭제
# 원소 한 개 삭제 : 세 가지 방법
# 1) del 명령어를 사용해서 해당 index의 원소를 삭제
# 2) remove 함수를 이용해서 값을 이용해서 해당 원소를 삭제
# 3) pop 함수를 이용, 해당 index의 원소를 삭제하고 삭제된 값을 반환 

bar = [10, 20, 30, 40, 50, 60]
print("before : ", bar, len(bar)) #[10, 20, 30, 40, 50, 60]
# del bar[1]
# print("after : ", bar, len(bar)) # [10, 50, 30, 40, 50, 60]

bar.remove(50)
print("after : ", bar, len(bar)) #[10, 30, 40, 50, 60]

print(bar.pop(2)) # 30
print("after : ", bar, len(bar)) # [10, 50, 40, 50, 60] 5