def vending_machine(money) :
    drink_price = 700

    num_drink = money // drink_price
    change = money % drink_price

# 출력
print(f"음료수 = {num_drink}, 잔돈 = {change}원")
vending_machine(3000)




def average(*args) :
    return sum(args) / len(args)

print(average(1, 2, 3, 4, 5))