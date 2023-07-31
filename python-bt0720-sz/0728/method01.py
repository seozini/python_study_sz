###매소드###

# : 특정한 개체를 통해서만 호출할 수 있는 함수를 매소드

# 문자열 매소드

 # 1. format() 매소드 : 문자열에 변수를 삽입 or 형식을 지정하는데 사용
print("Hello, {}. I am {} years old.".format("seozin",20))

 # 2. count() 매소드 : 특정 문자나 문자열이 등장하는 횟수를 세는데 사용
print("marry me, jaemin".count("m")) # 3

 # 3. find() 매소드 : 특정 문자나 문자열이 처음 등장하는 인덱스를 반환
 #                     찾고자 하는 문자나 문자열이 없는 경우 -1 반한
print("marry me, jaemin".find("e")) # 7
print("marry me, jaemin".find("k")) # -1

 # 4. index() 매소드 : 특정 문자나 문자열이 처음 등장하는 인덱스를 반환
 #                      찾고자 하는 문자나 문자열이 없는 경우 ValueError가 발생
print("marry me, jaemin".index("e")) # 7
# print("marry me, jaemin".index("k")) # Error

 # 5. 대소문자 변환 매소드
print("marry me, jaemin".upper()) # 모든 소문자를 대문자로 변환
print("MARRY ME, JAEMIN".lower()) # 모든 대문자를 소문자로 변환
print("marry me, jaemin".capitalize()) # 첫 글자만 대문자, 나머지 소문자 변환
print("marry me, jaemin".title()) # 각 단어의 첫 글자를 대문자, 나머지 소문자 변환

 # 6. join() 매소드 : 문자열 리스트를 하나로 합쳐 하나의 문자열로 변환
print(",".join(["watermelon", "tomato", "cherry"]))

 # 7. split() 매소드 : 문자열을 특정 문자를 기준으로 분리하여 리스트를 생성
print("watermelon, tomato, cherry".split(", "))

 # 8. replace() 매소드 : 특정 문자나 문자열을 다른 문자나 문자열로 교체
print("marry me, jaemin".replace("jaemin", "mark"))

 # 9. 불필요한 문자열 제거 매소드
print("   marry   ".strip()) # 문자열 양쪽 끝의 공백 및 다른 특정 문자를 제거
print("   marry   ".lstrip())
print("   marry   ".rstrip())
