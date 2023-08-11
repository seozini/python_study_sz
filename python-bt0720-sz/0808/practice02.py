class Quiz :
    answer = ['경기도', '강원도', '충청남도', '충청북도', '전라남도', '전라북도', '경상남도', '경상북도', '제주특별자치도']
    
    @classmethod
    def challenge(cls) :
        user_input = input('도를 입력하세요 : ')
        if user_input in cls.answer :
            cls.answer.remove(user_input)
            print('정답입니다.')
            if len(cls.answer) == 0 :
                print('모든 도를 맞혔습니다. 성공입니다.')
                return
            cls.challenge()
        else :
            raise Exception('틀렸습니다.')
        
try :
    print('우리나라의 9개 모든 도를 맞히는 퀴즈입니다. 하나씩 대답하세요.')
    Quiz.challenge()
except Exception as e :
    print(e)