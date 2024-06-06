line1 = int(input("첫 번째 변의 길이를 입력하세요"))
line2 = int(input("두 번째 변의 길이를 입력하세요"))
line3 = int(input("세 번째 변의 길이를 입력하세요"))

if line1 + line2 <= line3 or line1 + line3 <= line2 or line2 + line3 <= line1:
    print("입력하신 변의 길이로는 삼각형을 만들 수 없습니다.")
    print("삼각형을 만들기 위해서는 어떤 두 변의 길이의 합이 다른 한 변의 길이보다 커야 합니다.")
elif line1 == line2 == line3:
    print("입력하신 변의 길이로는 정삼각형을 만들 수 있습니다.")
elif (line1 == line2) or (line2 == line3) or (line1 == line3): 
    print("입력하신 변의 길이로는 이등변삼각형을 만들 수 있습니다.")
elif line1 != line2 != line3:
    print("입력하신 변의 길이로는 부등변 삼각형을 만들 수 있습니다.")       
