# 키보드로부터 정수를 입력 받고
# 0 또는 양수이면 "0 또는 양수"를 문자열로 출력
# 음수 이면 "음수" 문자열을 화면에 출력하는 프로그램 작성하라
number = int(input("정수를 입력하세요"))
if number > 0:
    print("양수 입니다.")
elif number == 0:
    print("0 입니다") 
else:
    print("음수 입니다.")