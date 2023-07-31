# 1.
# (교과서) 1부터 5사이에 존재하는 모든 정수를 역순으로 출력하는 프로그램을 구현

# range()함수 : 세 개의 인자(범위 시작점, 범위 끝점, 간격)

for i in range (5,0,-1) :
    print(i)

# 2.
# (교과서) 사용자로부터 임의의 양의 정수를 하나 입력 받은 뒤
# 그 숫자만큼 "과일 이름"을 입력받아 basket 리스트에 저장하는 프로그램을 구현

num_of_fruit = int(input("입력할 과일의 개수를 입력하세요 : "))
basket = []
for i in range(num_of_fruit) :
    fruit = input("과일 이름을 입력하세요 : ")
    basket.append(fruit)
print("과일 바구니 : ", basket)