# 1 ~ 10 사이 정수 중, 중복되지 않은 정수 N개 선택

import random
n = 5
max_num = 6

sample_list = [ value for value in range(1, 11) ]

# 1 ~ 10 사이 정수 중, 중복되지 않은 정수 N개 선택

import random
n = 5
max_num = 6

sample_list = [ value for value in range(1, 11) ]

# sample_list -> [1,2,3,4,5,6,7,8,9,10]

n = 5
random_list = []

for trial_count in range(0, n):
    random_index = random.randint(0, len(sample_list) - 1)
    random_num = sample_list.pop(random_index)
    random_list.append(random_num)    
    
    print("이번에 삭제할 원소",random_num)
    print("삭제한 원소 리스트", random_list)
    print("원소가 삭제된 sample list", sample_list)
    print()


print(random_list)







