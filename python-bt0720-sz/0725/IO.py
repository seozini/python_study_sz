# 파이썬의 입출력(Input/Outputf)

###파이썬의 기본 입출력###

# 1. 입력
 # Input()함수
 # : 사용자로부터 키보드로 입력을 얻는 파이썬 내장 함수

name = input('이름을 입력하세요 : ')

# input()함수와 형 변환
 # 1. 정수로 변환 : int()함수
string = input("정수를 입력하세요 : ")
number = int(string)

 # 2. 실수로 변환 : float()함수
string = input("실수를 입력하세요 : ")
float = float(string)

# 2. 출력
 # Output()함수
 # : 값을 출력하는 파이썬 내장 함수

print("안녕하세요,", name, "님!")

###형식화된 출력###

# %s : 문자열(모든 타입)
# %d : 숫자

name = "choi seozin"
age = 20
print("name : %s, age : %d"%(name,age))