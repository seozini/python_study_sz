### 클래스의 구성 ###

# 사람
# : 이름, 나이, 연락처, 주소, ...
# : 잔다, 먹는다, 공부한다, 걷는다, ...

# 1. 클래스 구성 : 변수 & 함수
 # 변수 - 값(상태)
 # 함수 - 기능(동작)
 
# 클래스를 구성하는 변수 :클래스 변수 & 인스턴스 변수
 # : 클래스 변수 & 인스턴스 변수

# 클래스를 구성하는 함수 : 매서드(method)
 # : 클래스 매서드, 정적 매서드, 인스턴스 매서드

# 2. 인스턴스 변수 & 인스턴스 매서드

 # 2-1. 인스턴스 변수
  # : 클래스를 기반으로 만들어지는 모든 인스턴스(객체)들이 각각 따로 저장하는 변수
  # : 클래스 내에 정의되지만 각 클래스 인스턴스(객체)에서 개별적으로 가지는 변수
  # : 각 객체의 상태 저장
  
  # 인스턴스 변수의 형태 : self.variable_name
  
 # 2-2. 인스턴스 매서드
  # : 클래스 내에 정의된 함수, 클래스의 객체가 수행할 수 있는 동작을 나타냄
  # : 인스턴스 변수를 사용하는 매서드
  # : 첫 번째 인자로 'self'를 받아야 함
  # slef : 매서드를 호출하는 객체 자신을 참조
  
class Person :
    # 첫 번째 매개변수가 self -> 인스턴스 매서드
    def who_am_i(self, name, age, tel, address) :
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address

mark = Person()
mark.who_am_i('mark', 25, '010-0802-0315', '서울특별시')
print(mark.tel)
print(mark.name)

jaemin = Person()
jaemin.who_am_i('jaemin', 24, '010-0813-0315', '서울특별시')
print(jaemin.name)
print(jaemin.age)