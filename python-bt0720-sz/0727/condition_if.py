# 1.
# (교과서) if문 : 임의의 정수 3개를 입력받아 그 중에서 가장 큰 수를 출력하는 프로그램을 구현하세요.
# 관계 연산자, 논리 연산자

num1 = int(input("첫 번째 숫자를 입력하세요 : "))
num2 = int(input("두 번째 숫자를 입력하세요 : "))
num3 = int(input("세 번재 숫자를 입력하세요 : "))

if num1 >= num2 and num1 >= num3 :
    largest = num1
elif num2 >= num1 and num2 >= num3 :
    largest = num2
else :
    largest = num3
print("가장 큰 수는", largest, "입니다.")

'''
if num1 >= num2 :
    if num2 >= num3 :
        print(num1)
    else :
        if num1 >= num3 :
            print(num1)
        else :
            print(num3)
else :
    if num1 >= num3 :
        print(num2)
    else :
        if num2 >= num3 :
            print(num2)
        else :
            print(num3)
'''


# 2.
# (교과서) if문 : 미세먼지 저감 활동의 일환으로 차량 2부제를 실시하고자 합니다.
# 사용자로부터 차량번호를 입력받아 차량번호가 짝수로 끝나면 "운행가능"
# , 아니면 "운행불가"를 출력하는 프로그램을 구현하세요.
# 단, 차량번호는 "82가 0813"과 같은 형식으로 입력받는다고 가정합니다.


carNumber = input("차량 번호를 입력하세요(예 : 82가 0813) : ")
lastNumber = int(carNumber[-1])
if lastNumber % 2 == 0 :
    print("운행가능")
else :
    print("운행불가")