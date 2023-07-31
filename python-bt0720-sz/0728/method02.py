###리스트 매소드###

# 1. append() 매소드 : 리스트의 끝에 새로운 요소 추가
animals = ["cat", "dog"]
animals.append("panda")
print(animals)

# 2. extend() 매소드 : 리스트의 끝에 다른 리스트를 연결하여 확장
animals = ["cat", "dog"]
more_animals = ["tiger", "lion"]
animals.extend(more_animals)
print(animals)

# 3. insert() 매소드 : 리스트의 특정 위치에 새로운 요소를 삽입
animals = ["cat", "dog"]
animals.insert(1, "panda")
print(animals)

# 4. clear() 매소드 : 리스트의 모든 요소를 제거, 빈 리스트 생성
animals = ["cat", "dog"]
print(animals.clear()) # None

# 5. pop() 매소드 : 리스트의 특정 위치의 요소를 제거, 그 요소를 반환
 # 인덱스번호를 작성하지 않을 경우 마지막 요소를 제거하고 반환
animals = ["cat", "dog", "panda"]
removed_animal = animals.pop(1)
print(animals)

# 6. remove() 매소드 : 리스트에서 첫 번째로 나타나는 특정 값을 제거한다
animals = ["cat", "dog", "panda"]
animals.remove("panda")
print(animals)