### 클래스 매서드 ###

# 1. 클래스 매서드 정의
# : @classmethod 데코레이터를 사용하여 정의된 매서드

class Myclass :
    class_var = '클래스 변수'
    
    @classmethod
    def class_method(cls) :
        return cls.class_var
    
# 2. 클래스 매서드 특징
# 2-1. 첫 번째 매개변수로 클래스 객체를 받는다. (cls 이름 사용)
# 2-2. 인스턴스 객체 없이도 호출 가능
#      : 클래스 매서드는 클래스 이름을 통해 호출 가능(인스턴스 & 클래스 호출 모두 가능)

class Korean :
    country = '한국' # 클래스 변수
    
    @classmethod
    def trip(cls, country) : # cls : 클래스 객체, country : 매개변수
        if cls.country == country :
            print('국내 여행입니다.')
        else :
            print('해외 여행입니다.')
            
Korean.trip('한국')
Korean.trip('캐나다') # cls.country == country (한국 == 캐나다)