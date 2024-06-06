# 문자열을 정수로 변환
num_str = input ("정수를 입력 하세요") # "123" 입력 가정
num_int = int(num_str) # 문자열 123"을 정수 123으로 변환 print(num_int) # 줄력: 123

print(num_int) # 출력: 123
print(type(num_int)) # 출력: <class 'int'>

# 정수를 부동 소수점 수로 변환
num_float =float(num_int), #정수 123을 부동 소수점 수 123.0으로 변환

print(num_float) # 출력: 123.0
print (type(num_float)) # 출력 ‹class 'float'›

# 정수를 문자열로 변환
num_int = 10
converted_str =str(num_int)

print(converted_str) # 출력: 10"
print(type(converted_str)) # 출력: <class 'str'>

# 정수를 Boolean 형으로 변환
print(bool(0)) # False
print (bool(-1)) # True
print(bool(10)) # True