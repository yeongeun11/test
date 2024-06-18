# 중복되지 않은 난수 값 3개 생성(0 ~ 9)

import random


count = 0
rand_list = []

while count < 3:
    rand_value = random.randint(0, 2)
    
    for index in range(count):
        if rand_list[index] == rand_value:
            break
    else:
        rand_list.append(rand_value)
        count += 1
        
print(rand_list)