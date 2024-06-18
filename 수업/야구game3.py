# 중복되지 않은 난수 값 3개 생성(0 ~9)

import random


rand_list = [value for value in range(0, 9)]

for _ in range(7):
    del rand_list[random.randint(0, len(rand_list) - 1)]

    print(rand_list)  