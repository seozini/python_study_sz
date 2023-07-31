# 1.  어떤 수가 양수인지, 음수인지, 아니면 0인지 판단하는 중첩 if-else문

'''
num = int(input())
if num > 0 :
    print("양수입니다")
elif num == 0 :
    print("0입니다")
else :
    print("음수입니다")
'''

num = int(input())
if num > 0 :
    print("The number is positive.")
else :
    if num < 0 :
        print("The number is negative.")
    else :
        print("The number is zero.")

# 2. 1부터 10까지 합을 구하는 프로그램 작성
#    for 반복문과 산술 연산자를 사용
total = 0
#    합계를 저장할 변수를 0으로 초기화
#    1부터 10까지의 모든 정수를 순화하면서 합계를 업데이트
for i in range(1,11) :
    total += i
#    최종 합계 출력
print("The sum from 1 to 10 is ", total)