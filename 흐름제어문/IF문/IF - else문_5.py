# 키보드로부터 정수를 입력 받아
# 아래 성적으로 환산하는 프로그램을 작성하라
# 90 <= 점수      이면 "A"
# 80 <= 점수 < 90 이면 "B"
# 70 <= 점수 < 80 이면 "C"
# 60 <= 점수 < 70 이면 "D"

inputValue = input("정수를 입력하세요")
inputValue = int(inputValue) # 문자형 -> 정수형 형 변환

if inputValue >= 90 :
    print("A")
elif inputValue >= 80 :
    print("B")
elif inputValue >= 70 :
    print("C")    
elif inputValue >= 60 :
    print("D")

print("프로그램 종료")                    

