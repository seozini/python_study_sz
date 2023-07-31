numbers = [1, 2, 3, 4]
numbers.append(5)
print(numbers)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)

list1.extend(list2)
print(list1)

fruits = ["apple", "orange", "grape"]
fruits.insert(1,"banana")
print(fruits)

numbers = [1, 2, 3, 4, 5]
removed_numbers = numbers.pop(4)
print(removed_numbers)
print(numbers)