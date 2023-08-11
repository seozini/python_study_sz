# 클래스 예제 #

# 사용자로부터 온전한 수식을 입력받고,
# 입력된 수식의 결과를 출력하는 Calculator 클래스

class Calculator :
    
    # 수식을 입력받아서 인스턴스 변수인 exper에 저장
    def input_exper(self) :
        exper = input('수식을 입력하세요 >> ')
        self.exper = exper # 우항의 exper = 9번 째 줄의 입력값
        
    def calculator(self) :
        # eval() : 문자열로 된 수식 자체를 계산할 수 있는 함수
        return eval(self.exper)
    
# Calculator 클래스를 기반으로 calc 인스턴스를 생성   
calc = Calculator()
# 사용자가 수식을 입력할 수 있는 콘솔창 생성
calc.input_exper()
# claculator() 매서드를 호출하면 수식 결과가 반환되면서 그 결과가 출력
print('수식 결과는 {}입니다.'.format(calc.calculator()))