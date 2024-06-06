# 참조 변수란(Reference variable)?
# 변수다! -> 메모리 공간에 값을 저장하는 것
# 일반변수(Primitive variable)과 차이점은?
# 일반변수와 달리, 참조변수는 메모리 주소 값을 저장한다.


bar = [90, 10, 20]

def test(argValue):
    for index in range(0, len(argValue)):
        argValue [index] += 1

test (bar)

print(bar) # 91, 11, 21




# 1) Ordered (순서)
# 2) Mutable (가변)
# 3) 하나의 리스트에 다양한 데이터 타입의 원소를 가질 수 있다.

# 자료구조를 공부할 때
# 각 자료구조의 CRUD (Create, Read, Update, Delete)

# CRUD : [Create & insert] 
# Create : 기본 자료구조를 메모리장에 할당
# insert : 자료구조에 원소를 추가 하는 것.

# Create : 두 가지 방법 제공
# [], list()

# insert : 원소를 추가 하는 방법
# append(), insert()

bar = [] # 원소는 0개

bar.append(10) # bar -> [] -> [10]
bar.append(20) # bar -> [10] -> [10, 20]
bar.append(3)  # bar -> [10, 20] -> [10, 20, 3]

#             0   1  2
print(bar) # 10, 20, 3

# bar -> [10, 20, 3]
bar.insert(1, 9) # index 삽입 위치, value 삽입 값.
print(bar)

# bar -> [200, 9, 20, 3] 

bar.insert(0, 200)
# bar -> [200, 9, 20, 3]
print(bar)
