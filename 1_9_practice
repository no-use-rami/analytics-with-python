#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 연습문제 1.
'''새로운 파이썬 스크립트를 만들고, 세 가지 다른 리스트를 만들고, 각 리스트를 합쳐보자.
그다음 for문과 각 리스트를 반복할 위치(즉 range(len()))을 이용하여 화면에 리스트의 인덱스와
해당하는 값을 출력해보자.'''

list1 = [1,2,3,4,5,6,7]
list2 = ['a','b','star',('@','#','$')]
list3 = [10,100,1000,10000,100000]

list4 = list1+list2+list3
print(list4)
print("\n")

print ("A1. ")
for index in range(len(list4)):
    print("{0:d}: {1!s}".format(index, list4[index]))

print("\n")
    

# 연습문제 2.
'''새로운 파이썬 스크립트를 만들고, 동일한 길이를 가진 리스트 두 개를 만든다.
이 중 하나의 리스트에는 서로 고유한 문자열을 넣고, 빈 딕셔너리를 하나 추가로 만든다.
그다음 for문과 위치 인덱스, 그리고 고유한 문자열을 지닌 리스트의 각 값들이 이미 딕셔너리에 있는 키인지
확인하는 if문을 작성한다. 만약 딕셔너리에 없는 문자열이라면, 딕셔너리에 키를 저장하고,
동일한 위치에 있는 다른 리스트의 값을 해당 키와 연관된 값으로 추가한다.
마지막으로 화면에 딕셔너리의 키와 각 연관된 값을 출력한다.'''

print("A2. ")

list1 = [1,2,3,4,5]
list2 = ['1','2','3','4','5']

dict1 = {}
    
for index in range(len(list1)):
    if list1[index] not in dict1:
        dict1[list1[index]] = [list2[index]]

for key, value in dict1.items():
    print("the key is {}, the value is {}".format(key, value))

print("\n")
    
# 연습문제 3.
'''새로운 파이썬 스크립트를 만들고, 동일한 길이의 리스트들로 구성된 리스트를 하나 만든다.
이 리스트로 된 리스트를 반복 처리하기 위해, 1.7.2절에서 작성한 코드를 수정해보자.
그다음 각 리스트에 있는 값을 쉼표로 구분하되 마지막 값 뒤에는 개행문자를 붙여 화면에 출력해보자.'''

list1 = [['hi','hello'],['my','name'],['is','rami']] 
comment = ''

for full_list in list1:
    max_index = len(full_list)
    for index in range(len(full_list)):
        if index < (max_index - 1):
            comment += str(full_list[index])+', '
        else:
            comment += str(full_list[index])+'\n'
            
print("A3.\n{}".format(comment))

# 그냥 궁금해서
words = comment.split(', ')
for index in range(len(words)):
    print(words[index])