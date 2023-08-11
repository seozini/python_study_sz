# 학생 - 사람의 클래스를 상속관계로 구현 #

class Person : #슈퍼 클래스
    
    def __init__(self, name) :
        self.name = name
        
    def eat(self, food) :
        print(self.name + '가' + food + '를 먹습니다.')
        
class Student(Person) : # 서브 클래스
    
    def __init__(self, name, school): 
        super().__init__(name) # 부모 클래스의  __init__ 매서드 호출
        self.school = school
        
    def study(self) :
        print(self.name + '는' + self.school + '에서 공부를 합니다.')

mark = Student('마크', '엔시티')
mark.eat('수박')
mark.study()

jaemin = Person('나재민')
jaemin.eat('초콜릿')