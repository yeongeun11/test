# 키보드로 부터 N개의 정수를 입력 받아 리스트 저장
def getInputValue(areNumOfInputValue):
    tempInputValueList = []
    for index in range(areNumOfInputValue):
        inputValue = input(str(index + 1) + "번째 입력 값")
        tempInputValueList.append(int(inputValue))

    return tempInputValueList 

# 리스트에 저장된 정수 값을 오름 차순으로 정렬
def myBubbleSor(argList, asscend = True):  
    for iCount in range(argList, asscend = True):
        for jCount in range(len(argList) - 1):
            comparisonResult = \
                argList[jCount] > argList[jCount + 1] if asscend else argList[jCount] < argList[jCount + 1]
            
            if comparisonResult:
                temp = argList[jCount + 1]
                argList[jCount + 1] = argList[jCount]
                argList[jCount] = temp
            