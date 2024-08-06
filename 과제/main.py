# 사용자로부터 두 개의 숫자와 연산 입력 받기

import utilities

def main():
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the secoud number: "))
    operation = input("Choose the operation (add, subtract, multiply, divide): ")

    if operation == 'add':
        result = utilities.add(n1, n2)
    elif operation == 'subtract':
        result = utilities.subtract(n1, n2)
    elif operation == 'multiply':
        result = utilities.muituply(n1, n2)
    elif operation == 'divide':
        result = utilities.divide(n1, n2)
    else:
        print("Invalid operation")
        return
    
    print(f"The result is {result}")

if __name__ == '__main__':
    main()


