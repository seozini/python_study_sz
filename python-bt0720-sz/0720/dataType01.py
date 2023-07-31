# 파이썬의 기본 데이터 타입(자료형)

# 1. 숫자형 : 숫자(Number)형태로 이루어진 자료형
 # : 정수(integer)와 실수(float)

 # 16진수 / 0x로 시작하는 숫자 + (숫자 0부터 알파벳 f까지 입력 가능)
a = 0xa1b
a= 0xcab

num1 = 1
num2 = 2
print(num1 + num2)

# 2. 논리형(boolean : 불리언)
 # : 참(True)과 거짓(False)의 두 개의 값만 가지는 자료형
 # 파이썬의 예약어, 첫문자를 항상 대문자로 사용해야 한다.

bool1 = True
bool2 = False
# bool3 = true(Error)
print(type(bool1))
 # : type() = 해당 변수의 자료형을 확인하는 파이썬의 내장 함수
 # 출력값 : <class 'int'> = 변수 a의 자료형은 int이다

 # 논리형의 경우 조건문의 리턴 값으로 사용된다
print(1 == 1)
print(2 > 1)
print(2 < 1)

print(bool1 + bool2) # 출력값 1

 # 파이썬에서는 비어있는 자료형을 False로 인식
 # '', {}, [], ()
 # 숫자 0 또한 False로 인식
 # None(값이없음)도 False로 인식

# 3. 문자열
 # : 문자, 단어 등으로 구성된 문자들의 집합

# 3-1. 문자열 자료형 선언 방식(4가지)
 # 큰따옴표(""), 작은따옴표(''), 큰따옴표 3개 연속 표시(""""""), 작은따옴표 3개 연속 표시('''''')

sentence1 = "I'll be back"
sentence2 = '"I like Python", she says'
sentence3 = '''여러 줄로 문장을 표현하고 싶을 땐
따옴표 3개를 연속으로 표시합니다.'''
print(sentence1)
print(sentence2)
print(sentence3)

 # 이스케이프 코드 : 백 슬래시(|) 를 사용하여 표현
  # |n : 줄바꿈
  # |t : 탭 간격
  # || : 문자기호 | 그 자체를 표현
  # |', |" : 따옴표 그 자체를 표현

lines = "|'python is fun|' |n I like Python"
print(lines)

# 3-2. 문자열 자료형 연산
print(sentence1 + sentence2)
print(sentence1 * 2) # 문자열의 곱셈은 해당 문자열을 정수배 만큼 반복해서 연결

message = "I like you"
 # len() : 문자열의 길이를 구하는 파이썬 내장 함수 (length)
 # 문자열의 경우 공백, 기호를 포함
print(len(message)) # 출력값 : 11

# 3-3. 문자열 인덱싱과 슬라이싱
 # 문자열 인덱싱(Indexing) : 문자열 안의 특정한 값을 뽑아내는 역할
 # 변수명(인덱스 번호)
 # 문자열의 전체 인덱스 번호 == 문자열의 길이 - 1
print(message(0))
print(message(5))
print(message(9))

 # 파이썬은 0부터 숫자를 시작
 # 공백 문자도 문자와 동일하게 취급
 # 마이너스(-) 기호를 붙일 경우 문자열 뒤에서부터 읽음 (마이너스의 경우 -1부터 시작)
print(message(-1))
print(message(-3))

 # 문자열 슬라이싱(Slicing) : 문자열 안의 단어를 뽑아내는 역할
 # 변수명[시작번호 : 끝번호] (시작번호와 끝번호는 해당 위치의 인덱스 번호)
 # 슬라이싱의 경우 끝번호를 포함하지 않음
 # ex) word[2:5] = 2 <= word <5

word = "I like you!"
print(word[2:5]) #lik
print(word[2:6]) #like

# 3-4. 문자열 변경\
 # 문자열은 immutable 자료형
 # : 요솟값을 변경할 수 없는 자료형

word[0:2] #'I '
word[6:10] #' you!'
print(word[0:2]+ 'love' + word[6:10])
 #문자열의 슬라이싱의 경우 첫 인덱스 번호와 마지막 인덱스 번호는 생략 가능
 # ex) word[:2] , word[6:]

# 3-5. 문자열 포매팅
 # : 문자열 내에 어떤 값을 삽입하는 방법
  # 1) %포매팅 (교재 p.56)
    # %d : 숫자 포맷 코드
    # %s : 문자열 포맷 코드 (어떤 형태의 값이든 변환해서 삽입 가능)
print('Hello, %s' %'python')
print('I have %d apples.'%4)

print('나는 100%% 확신해') # 문자열 그 자체의 %를 출력하고 싶은 경우 : %%

  # 2) str.format()
print('Hello, {}'.format('python'))
print('I have {} apples'.format(4))
print('{} {} {}'.format('I', 'like', 'you'))

  # 3) f-string 포매팅
name = 'python'
age = 20
print(f'My name is {name} amd I am {age} years old')

# f-string 포매팅의 장점 : 표현식 지원(문자열 안에서 변수와, +, -의 수식을 함께 사용 가능)
a=5
b=3
print(f'Five times three is {a*b}')

# 3-6. 문자열 관련 함수(내장함수)
str = 'icecream'

 # 1. 문자열의 길이 : len()
print(len(str))

 # 2. 문자 개수 세기 : count()
print(str.count('c')) # 2

 # 3. 문자 위치 알려주기 : find()
print(str.find('r')) # 4
print(str.find('k')) # -1 : 문자열 안에 해당 문자가 없는 경우 -1 출력

 # 4. 문자 위치 알려주기 : index()
print(str.index('r')) # 4
print(str.index('k')) # 존재하지 않을 경우 오류 발생

 # 5. 문자열 바꾸기 : replace()
str2 = "strawberry chocolate cake"
str3 = str2.replace("strawberry", "banana")
print(str2)
print(str3)

# 기타 문자열 내장 함수
 #소문자를 대문자로 바꾸기(upper)
 #대문자를 소문자로 바꾸기(lower)
str = 'Hello, World!'
print(str.upper())  # 'HELLO, WORLD!'
print(str.lower())  # 'hello, world!'

 #문자열 나누기(split)
print(str.split())  # ['Hello,', 'World!']