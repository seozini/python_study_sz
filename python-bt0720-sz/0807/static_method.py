### 정적 매서드 ###

# 1. 정적 매서드 정의
# : @staticmethod 데코레이터를 사용하여 정의된 매서드
# : 클래스나 인스턴스의 상태를 수정하거나 엑세스(접근)하지 않는 매서드
# : 클래스나 인스턴스의 정보에 접근하지 않음

# 생성자 매서드 : __init__(self)
# 클래스 매서드 : def 클래스매서드명 (cls)
# 정적 매서드 : 필수 매개변수 없음

# 2. 정적 매서드 특징
# : 인스턴스 객체 없이도 호출 가능 (클래스 이름을 통해서도 호출)
# : 클래스나 인스턴스 상태와 무관하게 독립적인 로직을 수행할 때 사용

class MyClass :
    
    class_var = "클래스 변수"
    
    @classmethod
    def class_method(cls) :
        return cls.class_var
    
    @staticmethod
    def static_method(param1, param2) :
        return param1 + param2
    
print(MyClass.class_method())
print(MyClass.static_method(8,2))

class Korean :
    country = '한국'
    
    @staticmethod
    def slogan() :
        print('Imagine your Korea')
        
Korean.slogan()