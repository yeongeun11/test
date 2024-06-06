def getCalcVlues(argA, argB):
    # argA와 argB의 +, -, *, / 값을 반환하는 함수 작성
    # 값 반환 시 tuple 자료형으로....
    return argA + argB, argA - argB, argA * argB,argA / argB

sum, substract, multiply, division = getCalcVlues(2, 3)

print(f"{sum}, {substract}, {multiply}, {division}")