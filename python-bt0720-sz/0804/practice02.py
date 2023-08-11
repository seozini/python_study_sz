### 클래스 생성, 생성자, 소멸자 예제 ###

class Character :
    def __init__(self, name, hp, strength) :
        self.name = name
        self.hp = hp
        self.strength = strength
        print(f'캐릭터 {self.name}이(가) 생성되었습니다. 체력은 {self.hp}, 힘은 {self.strength} 입니다.')

def attack(self, other_character) :
    print(f'{self.name}이(가) {other_character.name}을(를) 공격합니다')
    other_character.self       