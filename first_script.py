#!/usr/bin/env python3
from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta
# time 함수는 어떻게 쓰는 걸까
from operator import itemgetter
import sys
import os
import glob 

print("Output #1: I'm excited to learn python.")

# 두 수를 더한다.
x = 4
y = 5
z = x + y
print("Output #2: Four plus Five equals {0:d}.".format(z))
      
a = [1,2,3,4,5]
b = ["a","b","c","d"]
c = a+b
print("Output #3: {0}, {1}, {2}".format(a,b,c))
      
x = 9
print("Output #4:{0}".format(x))
print("Output #5:{0}, {1}".format(3**4,4**4))
print("Output #6:{0}".format(int(8.3)/int(2.7)))
       
print("Output #7:{0:.3f}".format(8.3/2.7))
y = 2.5/1.75
print("Output #8:{0:.1f}".format(y))
r=8/float(3)
print(r)
print("Output #9:{0:.2f}".format(r))
print("Output #10:{0:.4f}".format(8.0/3))
      
u = 4/3
print("{0:.2f}".format(u))

print("Output #11:{0:.4f}".format(exp(3)))
print("Output #12: {0:.2f}".format(log(4)))
print("Output #13: {0:.0f}".format(sqrt(81)))
      
print("Output #14: {0:s}".format('I\'m enjoying learning python.'))
print("Output #15: {0:s}".format("This is a long string. Without the backslash\
 it would run off of the page on the right in the text editor and be very\
 difficult to read and edit. By using the backslash you can split the long\
 string into smaller strings on separate lines so that the whole string is easy\
 to view in the text editor."))
# 문장 뒤에 백슬래시를 넣으면 에디터 상에서만 줄바꿈됨

print("Output #16: {0:s}".format('''
you can use triple single quotes
for multi-line comment strings.'''))
print("Output #17: {0:s}".format("""
You can also use triple double quotes
for multi-line comment strings."""))
# 트리플 작은따옴표나 큰따옴표나 둘다 줄바꿈 있는 문장으로 나타남

string1 = "This is a "
string2 = "short string."
sentence = string1 + string2
print("Output #18: {0:s}".format(sentence))
print("Output #19: {0:s}{1:s}!{2:s}".format("she is"," very"*4," nice."))
m = len(sentence)
print("Output #20: {0:d}".format(m))
      
string1 = "My deliverable is due in May"
string1_list1 = string1.split()
string1_list2 = string1.split(" ", 2)
print("Output #21: {0}".format(string1_list1))
print("{0}".format(string1_list2))
print("{0}, {1}".format("hello, world".split(",", 1), "How do you do".split()))
print("Output #22: First piece:'{0}' Second piece:'{1}' Third piece:'{2}'"\
.format(string1_list2[0], string1_list2[1], string1_list2[2]))
# 공백 기준으로 나눈 단어들을 리스트로 만들어서 순서대로 출력함

string2 = "Your,deliverable,is,due,in,June"
string2_list = string2.split(',')
print("Output #23: {0}".format(string2_list))
print("Output #24: {0} {1} {2}".format(string2_list[0],string2_list[5],\
string2_list[-2]))
print("{0} {1} {2} {3} {4} {5}".format(string2_list[-6],string2_list[-5],\
string2_list[-4],string2_list[-3],string2_list[-2],string2_list[-1]))
# 리스트 요소를 거꾸로 카운트할 때는 -n을 사용함 (인덱싱)
      
print("Output #25: {0}".format(','.join(string2_list)))
print("{0}".format(" ".join(string1_list2)))

string3 = " Remove  unwanted characters   from this string. \t\t  \n"
print("Output #26: string3 : {0:s}".format(string3))
string3_lstrip = string3.lstrip()
print("Output #27: lstrip: {0:s}".format(string3_lstrip))
string3_rstrip = string3.rstrip()
print("Output #28: rstrip: {0:s}".format(string3_rstrip))
string3_strip = string3.strip()
print("Output #29: strip: {0:s}".format(string3_strip))
      
string4 = "$$Here's another string that has unwanted characters.__---++"
print("Output #30: {0:s}".format(string4))
string4 = "$$The unwanted characters have been removed.__---++"
string4_strip = string4.strip('$_-+')
print("Output #31: {0:s}".format(string4_strip))

string5 = "Let's replace the spaces in this sentence with other characters."
string5_replace = string5.replace(" ", "!@!")
print("Output #32: (with!@!) {0:s}".format(string5_replace))
string5_replace_replace = string5_replace.replace("!@!", " ")
print("{0:s}".format(string5_replace_replace))
string5_replace = string5.replace(" ",", ")
print("Output #33: (with commas): {0:s}".format(string5_replace))

string6 = "Here's What Happens WHEN You Use lower, UPPER, Capitalize."
print("Output #34: {0:s}".format(string6.lower()))
print("Output #35: {0:s}".format(string6.upper()))
print("Output #36: {0:s}".format(string6.capitalize()))
string6_list = string6.split()
print("Output #37: (on each word):")
for word in string6_list:
    print("{0:s}".format(word.capitalize()))    
    
# 문자열 안에 등장하는 패턴의 횟수 세기
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"The", re.I)
# re.compile 함수는 텍스트 기반의 패턴을 정규 표현식으로 컴파일함
# re.I 함수는 대소문자 구분 없이 처리함
# r은 raw string을 나타냄(\, \t, \n등을 처리하지 않음)
count = 0
for word in string_list:
    if pattern.search(word):
        count += 1 
        # += 이게 무슨 뜻이지?
        # 아 알았다 pattern 함수를 (word) 안에서 search한 값이 True일 때마다 count를 1씩 더한다는 것!
print("Output #38: {0:d}".format(count))
      
# 문자열 내에서 발견된 패턴 출력하기
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"(?P<match_word>The)", re.I) #<match_word>는 메타 문자(변수명)
print("Output #39:")
for word in string_list:
    if pattern.search(word):
        print("{:s}".format(pattern.search(word).group('match_word')))
        # {:s} 여긴 왜 번호가 없어도 되는 걸까?
        # pattern 함수를(word) 안에서 search해서 True일 때 'match_word'group에 해당하는 값을 반환한다
        
# 문자열 내 "the"를 "a"로 대체하기
string = "The quick brown fox jumps over the lazy dog."
string_to_find = r"The"
pattern = re.compile(string_to_find, re.I)
print("Output #40: {:s}".format(pattern.sub("a", string)))
      # 여기선 {0:s}랑 똑같다
        
# 오늘 날짜와 연, 월, 일 요소들 출력하기
today = date.today()
print("Output #41: today: {0!s}".format(today))
        # !s는 전달된 값이 숫자여도 문자로 표기하라는 의미
print("Output #42: {0!s}-{1!s}".format(today.year, today.month))
year = today.year
month = today.month
date = today.day
current_datetime = datetime.today()
print("{0}-{1}-{2}".format(year,month,date))
print("{0!s}".format(current_datetime))

datetime.now().time
# time은 이런 식으로 이미 추출한 값에서 시간 부분을 가져올 때 쓴다 
# 그런데 거의 쓸 일은 없을듯

# timedelta 함수를 이용하여 새로운 날짜 계산하기
one_day = timedelta(days=-1)
yesterday = today + one_day
print("Output #46: {0!s}".format(yesterday))
eight_hours = timedelta(hours=-8)
print("Output #47: {0!s} {1!s}".format(eight_hours.days, eight_hours.seconds))
someday = timedelta(weeks=2)
print(today - someday)
print(someday.days)

# 두 날짜 사이의 차이를 계산하기
date_diff = today - yesterday
print("Output #48: {0!s}".format(date_diff))
print("Output #49: {0!s}".format(str(date_diff).split(',')[0]))
      # date_diff를 문자열로 만들고 ',' 기준으로 나눈 첫 번째 값을 보여준다

# date 객체를 특정 형식의 문자열로 만들기
      # str 문자열로 바꾸는 것들
print("Output #50: {:s}".format(today.strftime('%Y/%m/%d')))
      # {0:s}, {0!s}, {:s} 다 되는 이유는 뭐람
print("Output #51: {:s}".format(today.strftime('%Y, %b-%d')))
print("Output #52: {:s}".format(today.strftime('%Y-%m-%d')))
print("Output #53: {:s}".format(today.strftime('%B %d, %Y')))
print("{:s}".format(today.strftime('%y%m%d')))

# 날짜 문자열로부터 특정 형식의 dateime 객체를 생성하기
date1 = today.strftime('%m/%d/%Y')
date2 = today.strftime('%Y, %b-%d')
date3 = today.strftime('%Y-%m-%d')
date4 = today.strftime('%B %d, %Y')
      
# 다른 date형식을 지닌 4가지 문자열에 기반한 각각 2종류의 datetime 객체들과 date 객체들
print("Output #54: {!s}".format(datetime.strptime(date1, '%m/%d/%Y')))
print("Output #55: {!s}".format(datetime.strptime(date2, '%Y, %b-%d')))
      # today는 strftime이고 datetime은 strptime이군
      
# 날짜 부분만 출력하기
print("Output #56: {!s}".format(datetime.date(datetime.strptime(date3, '%Y-%m-%d')))) 
print("Output #57: {!s}".format(datetime.date(datetime.strptime(date4, '%B %d, %Y'))))
      # 지정한 변수의 날짜 형식이 어땠든 이렇게 가공하면 기본 연-월-일로 출력됨
      
# 리스트는 대괄호 사용
# len() 함수를 통해 리스트 내 원소의 수를 센다
# max() 함수와 min()함수는 최대/최소 값을 찾는다.
# count() 함수는 리스트 내 특정 값이 등장한 횟수를 센다
a_list = [1,2,3,3,3,5,5,1,1,2,4,2]
print("{}".format(a_list.count(2)))
# 출력할 값이 하나 이상일 때는 몇 번째인지 짚어줘야 하고, 하나면 {} 비워도 됨
print("Output #58: {}".format(a_list))
print("Output #59: a_list has {} elements.".format(len(a_list)))  
      # 왜 count 함수는 변수 뒤에 붙이고 len 함수는 괄호 앞에 오는 걸까?
      # count는 조건이 필요하니까?
print("Output #60: the maximum value in a_list is {}.".format(max(a_list)))
print("Output #61: the minimum value in a_list is {}.".format(min(a_list)))
another_list = ['printer',5,['star','circle',9]]
#another_list = ['printer', 5, a_list]
      # 오 이런 리스트는 신기하다 리스트 안에 리스트가
      # 그냥 리스트 이름을 넣어도 되는구나
print("Output #62: {}".format(another_list))
print("Output #63: another_list also has {} elements.".format(len(another_list))) 
print("Output #64: 5 is in another_list {} time.".format(another_list.count(5)))
print("{}".format(another_list.count(a_list)))
     # 리스트 이름을 카운트해도 됨, 단 그 리스트 안에 있는 요소가 찾아지지는 않음
     # 그러면 리스트 안에 있는 리스트의 요소를 찾으려면 어떻게 해야 하나?
print("{0},{1}".format(another_list.count(a_list),a_list.count(9)))
     # 이건 좀 번거로운데
     
# 리스트 내 특정 원소에 접근하기 - 인덱스
# 이거 위에서 나와서 알고있지롱
print("Output #65: {}".format(a_list[0]))
print("Output #66: {}".format(a_list[10]))
print("Output #67: {}".format(a_list[-0]))
print("{}".format(a_list[-3]))
      # 인덱스는 0부터, -0은  0이랑 똑같지롱

# 리스트 분할하기
print("Output #73: {}".format(a_list[0:2]))
      # [0:2]에서 앞의 0은 시작할 위치, 2는 첫 요소부터의 갯수
      # [0:0] 하면 빈 값이 나옴
print("Output #74: {}".format(a_list[:0]))
      # 처음부터 셀 거면 굳이 0 안 써도 됨
      # 여기서도 [:0]을 쓰면 빈 값이 된다능
print("Output #75: {}".format(a_list[3:15]))
      # :뒤의 숫자는 추출할 갯수가 아니라 리스트 맨 앞부터의 순서군
      # 심지어 :뒤에 리스트 갯수보다 더 큰 숫자를 써도 에러는 안 난다
print("{}".format(a_list[5:3]))
      # 앞보다 뒤의 숫자가 작으면 당연히 아무 값도 안 나온다
print("Output #76: {}".format(another_list[1:])) 
      # : 뒤를 비우면 알아서 리스트 끝까지 ㄱㄱ
      
# [:]를 이용해 리스트 복사하기
a_new_list = a_list[:]
print("Output #77: {}".format(a_new_list))
      # 리스트 원본 하나만 수정하면 되니까 편함
      
# + 연산자로 리스트 병합하기
a_longer_list = a_list + another_list
print("Output #78: {}".format(a_longer_list))
      
# in과 not in으로 리스트 내 특정 원소의 포함 여부 확인하기
a = 2 in a_list
# 애초에 조건을 변수로 지정해주면 편하겠군
print("Output #79: {}".format(a))
      # 여기까지 출력하면 T/F값이 나옴 (부울)
if 2 in a_list:
    print("Output #80: 2 is in {}".format(a_list))
      # .format(a_list)는 a_list 원소들을 다 보여줌

b = 6 not in a_list
print("Output #81: {}".format(b))
if 3 not in a_list:
    print("Output #82: 6 not in {}".format(a_list))
else:
    print("그럴리가 in {}".format(a_list))

# append() 함수를 이용해 리스트의 마지막에 원소 추가
# remove() 함수를 이용해 리스트 내 특정 원소 제거
# pop() 함수를 이용해 리스트의 마지막 원소 제거
a_list.append(4)
a_list.append(6)
print("Output #83: {}".format(a_list))
      # 같은 숫자를 복수로 추가하고 싶다면?
a_list.remove(3)
print("Output #84: {}".format(a_list))
      # 3이 여러개 있는데 하나밖에 안 사라졌당.. 첫 번째 3이 사라진건가?
      # 나머지 3들을 동시에 치울 방법은?
      # 다 없어질때까지 반복시키면 된다 (그래서 코딩을..)
      
a_list.pop()
a_list.pop()
print("Output #85: {}".format(a_list))

# reverse() 함수로 리스트 반전하기
# 해당 리스트 내에서(인플레이스) 변경이 일어나므로 (출력값만 변하는 게 아님)
# 기존 리스트를 변경하지 않으려면 사본을 만들어 둬야 한다.
a_list.reverse()
print("Output #86: {}".format(a_list))
a_list.reverse()
print("Output #87: {}".format(a_list))     
      
# sort() 함수로 리스트 원본 안에서 순서 정렬하기
unorderd_list = [3,6,1,7,2,0,9,8,5,4]
print("Output #88: {}".format(unorderd_list))
list_copy = unorderd_list [:]
list_copy.sort()
      # 역순으로 정렬하려면? 다른 조건을 쓰려면 뭘 해야 할까?
print("Output #89: {}".format(list_copy))
print("Output #90: {}".format(unorderd_list))   
      
# sorted() 함수로 리스트들 특정 위치에 따라 정렬하기 
my_lists = [[1,2,3,4],[4,3,2,1],[2,4,1,3]]
my_lists_sorted_by_index_3 = sorted(my_lists, key=lambda index_value: index_value[3])
      # sorted 함수를 key 함수와 결합한 것
      # index_value[3]은 해당 리스트의 3번 인덱스(4번째) 값을 기준으로 정렬한다는 것
my_lists_sorted_by_index_0 = sorted(my_lists, key=lambda index_value: index_value[0])
print("Output #91: {}".format(my_lists_sorted_by_index_3))
print("{}".format(my_lists_sorted_by_index_0))      
      
# itemgetter() 함수를 이용해 2개 인덱스 위치에 따라 리스트 정렬하기
my_lists = [[123,2,2,444],[22,6,6,444],[354,4,4,678],[236,5,5,678],\
[578,1,1,290],[461,1,1,290]]
my_lists_sorted_by_index_3_and_1 = sorted(my_lists, key=itemgetter(3,1))
      # lambda에서는 index_value를 []로 지정하고, itemgetter에서는 ()로 복수 지정한닷
      # 앞의 3번 인덱스를 기준으로 정렬하고, 그 상태에서 다음 순위 1번 인덱스를 기준으로 정렬함
print("Output #92: {}".format(my_lists_sorted_by_index_3_and_1))

sorted(my_lists, key=itemgetter(2,3))  
# 변수 지정 없이 이것만 해도 에러는 안 남
# 하지만 출력할 때 귀찮지
print("{}".format(sorted(my_lists, key=itemgetter(2,3))))  

# 문자열은 어떻게 정렬하지? 특정한 기준을 지정하려면?

# 괄호를 사용해 튜플 생성하기
# 튜플은 리스트처럼 편집할 수 없다
my_tuple = ('x','y','z')
print("Output #93: {}".format(my_tuple))
print("Output #94: my tuple has {} elements.".format(len(my_tuple)))
      # 리스트처럼 원소의 수를 셀 수 있다
print("Output #95: {}".format(my_tuple[1]))
longer_tuple = my_tuple + my_tuple
print("Output #96: {}".format(longer_tuple))
# 튜플 풀기
# 할당 연산자(=) 의 왼편에 튜플 풀기
one, two, three = my_tuple
      # 오 이렇게도 되는군
      # 위에서 할당한 my_tuple의 원소들을 각각 one, two, three로 할당해 줌
print("Output #97: {2},{0},{1}".format(one, two, three))
      #  {}에 각각 순서를 바꿔도 됨, 비워두면 기본 순서대로.
var1 = 'red'
var2 = 'robin'
print("Output #98: {} {}".format(var1, var2))
# 변수 간 값 교환하기
var1, var2 = var2, var1
# 호옹이
print("Output #99: {} {}".format(var1, var2))
      
# 튜플을 리스트로, 리스트를 튜플로 변환하기
my_list = [1,2,3]
my_tuple = ('x','y','z')
print("Output #100: {}".format(tuple(my_list)))
print("Output #101: {}".format(list(my_tuple)))

list_to_tuple = tuple(my_list)
print("{}".format(list_to_tuple))

tuple_copy_to_list = list(my_tuple[:])
print("{}".format(tuple_copy_to_list))

# 딕셔너리
# 고유 식별자와 쌍을 이루는 정보로 구성된 리스트
# (고객 번호 / 시리얼 넘버 / 거래 인덱스 등)
# 리스트 = 연속적인 정수값, 암묵적으로 정렬
# 딕셔너리 = 인덱스가 숫자가 아님, 기본 정렬 방법 없음
# 정렬되어 있지 않아 값 추가 또는 검색 시 빠른 응답 가능 - 많은 데이터 처리할 때 유리

# 중괄호를 이용해 딕셔너리 생성하기
# 각 쌍의 키와 값 사이에 콜론 사용
# len()함수는 딕셔너리에 있는 키-값 쌍의 수를 센다
empty_dict = { }
a_dict = {'one':1, 'two':2, 'three':3}
print("Output #102: {}".format(a_dict))
print("Output #103: a_dict has {!s} elements".format(len(a_dict)))
      # a_dict 내 원소(쌍)의 갯수를 숫자로 나타낸다
another_dict = {'x':'printer', 'y':5, 'z':['star','circle',9]}
      # 딕셔너리 값은 일정한 형식이 아니어도 된다
print("Output #104: {}".format(another_dict))
print("Output #105: another_dict has {!s} elements".format(len(another_dict)))
test_dict = {'1':'one', 'y':2, '4':[1,2,3], '5':[]}
print(test_dict)
      # 키-값 모두 다른 형식도 가능하다(키에 리스트는 안 됨)
      # 빈 리스트도 값에 들어갈 수 있다

# 키를 사용해 딕셔너리 내 특정 값 접근하기
print("Output #106: {}".format(a_dict['two']))
      # 딕셔너리명[대괄호] 안에 키 값을 넣는다
print("{}".format(test_dict['4']))
      # '4'와 4는 다르다
      
# copy() 함수를 이용해 딕셔너리 사본 만들기
a_new_dict = a_dict.copy()
      # copy() 이 괄호는 어떤 경우에 사용될까?
print("Output #108: {}".format(a_new_dict))

# keys(), values(), items()를 사용하여 키, 값, 키-값 쌍에 접근하기
print("Output #109: {}".format(a_dict.keys()))
      # 키만 출력됨
print("Output #110: {}".format(a_dict.values()))
      # 값만 출력됨
print("Output #111: {}".format(a_dict.items()))
      # (키,값) 튜플로 구성된 리스트가 출력됨
print("Output #112: {}".format(test_dict.items()))
      
# 딕셔너리 내 모든 키와 값을 풀고 접근하는 데 for문 이용하기
if 'y' in another_dict:
    print("Output #114: y is a key in another_dict: {}."\
.format(another_dict.keys()))
      # another_dict 안에 y 키가 있다면 딕셔너리의 키 리스트를 출력한다.
if 5 not in another_dict:
    print("Output #115: 5 is not a key in another_dict: {}."\
.format(another_dict.keys()))
      # another_dict 안에 c 키가 없다면 딕셔너리의 키 리스트를 출력한다.
      # 결과가 true가 아닐 경우 아무 일도 일어나지 않는다.(else가 없으니까)
      # 값 기준으로는 찾을 수 없다. key를 기준으로 찾아야 함.
print("Output #116: {!s}".format(a_dict.get('three')))
      # a_dict에서 'three'키에 해당하는 값을 가져와 문자열로 출력한다
print("Output #117: {!s}".format(a_dict.get('four')))
      # 해당하는 키가 없을 때는 기본적으로 None을 출력한다. 
print("Output #118: {!s}".format(a_dict.get('four','Not in dict')))
      # 키가 존재하지 않을 때 출력할 내용을 인수로 넣을 수 있다.
print("{}".format(test_dict.get(4, '없')))
print("{}".format(test_dict.get('4', '없')))
      # 이것도 값을 넣어서는 찾을 수 없다. 키가 괜히 키겠냐능

# sorted() 함수를 이용해 딕셔너리 정렬하기
# 원본이 수정되므로 사본 딕셔너리를 만들어보자
print("Output #119: {}".format(a_dict))
dict_copy = a_dict.copy()
orderd_dict1 = sorted(dict_copy.items(), key=lambda item: item[0])
      # 딕셔너리 내 각 튜플(키-값 쌍)의 첫 번째([0]) 원소(키)를 기준으로 정렬한다
print("Output #120: (order by keys): {}".format(orderd_dict1))
      # 기본적으로 오름차순 정렬이다
orderd_dict2 = sorted(dict_copy.items(), key=lambda item: item[1])
      # 딕셔너리 내 각 튜플의 두 번째([1]) 원소(값) 기준으로 정렬한다     
print("Output #121: (order by values): {}".format(orderd_dict2))

test_dict_copy = test_dict.copy()
print("{}".format(sorted(test_dict_copy.items(), key=lambda item: item[0])))
      # 값의 형식이 일정하지 않을 때는(int / str 혼재) 에러가 난다
      
orderd_dict3 = sorted(dict_copy.items(), key=lambda x: x[1], reverse=True)
      # True의 T는 대문자다
      # reverse는 내림차순으로 정렬한다
      # 왜 여기서 갑자기 x가 튀어나온 것인지는 모르겠다
print("Output #122: (order by values, descending): {}".format(orderd_dict3)) 
print("Output #123: (order by values, ascending): {}".format\
(sorted(dict_copy.items(), key=lambda x: x[1], reverse=False)))
    
# 제어 흐름
# '만약 고객이 특정 양보다 더 많이 소비한다면 ㅇㅇ을 수행해라'
# '만일 판매가 ㄱ 카테고리에서 발생했다면 a 코드를, ㄴ 카테고리에서 발생했다면 b 코드를 실행해라' 등
# 프로그램에 유의미한 비즈니스 로직을 구성하는 것을 의미함
# 파이썬에서는 if-else-else 문, for문, range함수 등이 이를 제공함
# if-else는 내가 아는 그거 ㅇㅇ
# for에서 사용할 수 있는 일련의 인덱스를 생성할 때 len(리스트)함수와 range() 함수를 이용하면 편함
# while 문은 조건이 참이 될 때까지 body의 코드를 실행함(like 브레이크가 고장난 8톤 트럭...)

# if-else문 : 조건 - 예외
x = 5
if x >= 4 or x == 9:
    # or 연산자는 왼쪽이 True이면 오른쪽은 쿨스루, 왼쪽이 False일 때만 오른쪽을 평가
    print("Output #124: {}".format(x))    
else:
    print("Output #124: x is not greater than 4")      

# if-elif-else문 : 조건1 - 조건2 - 예외
if x > 6:
    print("Output #125: x is greater than six")
elif x > 4 and x == 5:
    # and 연산자는 왼쪽이 False이면 즉시 중단됨. 둘 다 True여야 진행
    print("Output #125: {}".format(x))
else:
    print("Output #125: x is not greater than 4")
          # 다음에 또 124, 125번 예제를 테스트한다면 x를 9로 바꿔보렴
    
# for 루프
y = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
z = ['annie', 'Betty', 'Claire', 'Daphne', 'ellie', 'franchesca', 'Greta', 'holly', 'Isabel', 'Jenny']

print("Output #126:")
for month in y:
    print("{!s}".format(month))

print("Output #127: (index value: name in list)")
for i in range(len(z)):
    # z 리스트 원소 갯수의 범위에서 for문을 실행한다
    print("{0!s}: {1:s}".format(i, z[i]))
    # 0!s는 0번째 원소가 숫자여도 강제로 문자열로 출력하라는 것
    # 1:s는 (강제여부x) 1번째 원소를 문자열로 출력함
    # 인덱스 번호, 리스트[인덱스]에 해당하는 원소를 가져옴

print("Output #128: (access elements in y with z's index values)")
for j in range(len(z)):
    if y[j].startswith('J'):
        # y리스트의 [j번째] 원소가 'J'로 시작하는가?
        print("{!s}".format(y[j]))       

print("\n응용하기")
for m in range(len(z)):
    if y[m].startswith('M'):
        print("{}".format(y[m]))
    
print("Output #129:")
for key, value in another_dict.items():
    # 오 for문에 두 가지 리스트를 가져올 수 있구나
    print("{0!s}, {1}".format(key, value))
    
    
# 간결한 for문 : list, set, dictionary 축약
# 리스트 축약은 대괄호[], 집합 및 딕셔너리 축약은 중괄호{} 사용 (for in 문을 감싸는 괄호)
    
# 리스트 축약을 이용해 특정 행 고르기 
my_data = [[1,2,3], [4,5,6], [7,8,9]]
rows_to_keep = [row for row in my_data if row[2] > 5]
      # my_data의 각 행(리스트 원소) 가운데, 행의 2번 인덱스 값(세 번째 값)이 5보다 큰 것만 가져옴
print("Output #130: (list comprehension): {}".format(rows_to_keep))

# 집합 축약을 이용해 튜플로 구성된 리스트에서 고유한 튜플만 선별해 집합을 추출하는 방법
my_data = [(1,2,3), (4,5,6), (7,8,9)]
set_of_tuples1 = {x for x in my_data}
print("Output #131: (set comprehension): {}".format(set_of_tuples1))
      # 출력할 때 정렬이 아무렇게나 뒤섞이는군
set_of_tuples2 = set(my_data)
      # 호라 간단데스
print("Output #132: (set funtion): {}".format(set_of_tuples2))
      # 결과는 집합 축약과 똑같지만 훨 간단하니 set함수를 쓰도록 하자
      
# '고유한' 튜플을 선별한다는 것
test_tuple = [(1,2),(1,2,3),(1,2),(1,2,3,4)]
print("{}".format(set(test_tuple)))
      # (1,2) 튜플이 중복되므로 하나만 출력됨

# 딕셔너리 축약을 이용해 특정 조건에 부합하는 키-값 쌍의 부분 집합 선별
my_dictionary = {'customer1':7, 'customer2':9, 'customer3':11}
my_results = {key : value for key, value in my_dictionary.items() if value > 10}
      # my_dictionary의 아이템 중 값을 기준으로 10이 넘는 key와 value 쌍을 가져온다
print("Output #133: (dictionary comprehnsion): {}".format(my_results)) 
      
# while 문은 보디가 실행되어야 할 횟수를 미리 알고 있을 때 유용하다.
# 모르면 되도록 for문을 쓰도록
print("Output #134:")
x = 0
while x < 11:
    print("{!s}".format(x))
    x += 1
      # x가 11보다 작을 때 True
      # while문이 True일 때 x값을 출력한다
      # x에 1을 더한다
      # while문이 False가 될 때까지 반복한다
      
# 함수를 만들 때는 맨 앞에 def라는 키워드로 시작해 함수명(): 으로 입력함
# 함수의 보디가 되는 코드는 들여쓰기를 해야 함
# 함수가 하나 이상의 값을 반환해야 한다면 return이라는 키워드를 입력함

# 숫자 시퀀스의 평균 계산하기
def getMean(numericValues):
    return sum(numericValues)/len(numericValues) if len(numericValues) > 0 \
    else float('nan')     
    # numericValues라는 변수에 포함된 원소의 수가 1 이상일 때, 평균을 계산함
    # False일 경우 'nan'을 실수 형식으로 반환함
    # 일련의 동작을 getMean으로 이름 붙인 함수로 지정함

my_list = [2,2,4,4,6,6,8,8]
print("Output #135 (Mean): {!s}".format(getMean(my_list)))
      
import numpy as np
      # 모듈 이름이 길면 as로 줄일 수 있다
print("Output #136 (mean): {!s}".format(np.mean(my_list)))
      # numpy의 mean함수를 쓰면 초간단데스
      
# 예외.
# 파이썬에 포함된 기본적인 예외들
# IOError, IndexError, KeyError, NameError, SyntaxError, TypeError, UnicodeError, ValueError 둥
# 자세한 내용은 생략한다
      
# 오류를 처리하는 방법 try-except
# if문 대신 사용해 빈 리스트를 다룰 수 있다

# try-except를 이용해 숫자 시퀀스의 평균 계산하기
def getMean(numericValues):
    return sum(numericValues)/len(numericValues)

my_list2 = [1,2,205]

# 짧은 버전
try:
    print("Output #137: {}".format(getMean(my_list2)))
except ZeroDivisionError as zero:
      # 특정 에러 유형에 대한 예외처리
      # as ~ 는 해당 예외 내용을 담은 변수임
    print("Output #137 (Error): {}".format(float('nan')))
    print("Output #137 (Error): {}".format(zero))
      # my_list2에 대해 getMean 함수를 실행한다 (참일 경우 평균값 출력)
      # 비어 있는 my_list2가 ZeroDivisionError에 해당한다
      # 예외 처리로 nan과 에러 메세지를 출력한다
    
#긴 버전
try:
    result = getMean(my_list2)
      # getMean(my_list2)의 결과를 result 변수에 할당한다
except ZeroDivisionError as detail:
    print("Output #138 (Error): {}".format(float('nan')))
    print("Output #138 (Error): {}".format(detail))
else:
    print("Output #138: {:.2f}".format(result))
      # 예외에 해당하지 않을 경우 변수 result의 값을 출력한다
finally:
    print("Output #138 (finally): the finally block is executed every time")
      # finally 블록은 예외이든 아니든 항상 실행된다

## 텍스트 파일 읽기 - sys 모듈 필요
## sys 모듈을 임포트하면 리스트 형식의 argv 변수를 사용할 수 있다
## argv 변수는 command-line 인수들로 구성된 리스트를 파이썬 스크립트로 가져온다.
## argv 리스트의 인덱스 argv[0]은 스크립트 이름, argv[1]은 커맨드 라인으로 전달된 첫 번째 인수이다.(읽을 파일명)

# 하나의 텍스트 파일 읽기
'''
print("Output #139: ")
input_file = sys.argv[1] 
      # sys.argv 함수로 읽을 파일명을 불러와 input_file 변수에 할당함
filereader = open(input_file, 'r') 
      # 파일 객체를 생성하기 위해 open함수로 input_file 내용의 각 행을 저장함
      # 'r'은 읽기 모드로 연다는 뜻
for row in filereader:
    print(row.strip()) # strip으로 각 행의 앞과 끝의 공백, 탭, 개행문자 등을 제거함
filereader.close # close 함수로 fileleader 객체를 닫는다
'''

## 터미널에서 python first_script.py file_to_read.txt 로 명령을 실행한다
## 텍스트 파일 경로가 다를 때는 python first_script.py (전체 경로)file_to_read.txt 입력

## 139번의 filereader 생성 코드는 구식이래.....
## close 함수로 닫거나 스크립트가 종료될 때까지 파일 객체가 열려있어 오류를 일으킬 수 있음
## 파이썬 2.5 이후에서는 with문으로 파일을 생성할 수 있고, with문이 끝날 때 자동으로 파일 객체를 닫는다

# with문을 활용한 파일 읽기
'''
input_file = sys.argv[1]
print("Output #140: ")
with open(input_file, 'r', newline='') as filereader:
    for row in filereader:
        print("{}".format(row.strip()))
'''
      # open 함수로 input_file을 읽기 전용으로 열고, newline 인수를 공백으로 지정한다
      # 가져온 행을 filereader 객체에 할당한다.
      # 마지막 행까지 strip()을 적용해 출력한다.

## glob 모듈은 적은 수의 코드로 다수의 입력 파일을 읽고 처리할 수 있다
## 파일이 아니라 폴더에 초점을 맞춰, 특정 패턴과 일치하는 모든 경로명을 찾는다.
## 여러 파일에서 전체 또는 부분집합의 통계치를 구할 때 유용함
## os 모듈은 유용한 경로 함수를 이용할 수 있다.
## os.path.join 함수는 하나 이상의 경로를 구성하는 요소들을 서로 합친다
## os와 glob을 결합하면 특정 폴더 내, 특정 패턴의 파일을 모두 찾을 수 있다
      
# 다수의 파일 읽기
print("Output #141:")
inputPath = sys.argv[1]
for input_file in glob.glob(os.path.join(inputPath, '*.txt')):
        # glob.glob 함수와 os.path.join 함수 함께 활용
        # 커맨드 라인에서 입력받은 변수 inputPath에 해당하는 폴더 내 '*.txt'형식의 파일을 찾는다
        # 찾은 파일들을 input_file로 할당한다
    with open(input_file, 'r', newline='') as filereader:
        for row in filereader:
            print("{}".format(row.strip()))
            
        # 터미널에서 python first_script.py "폴더 경로" 입력
        # 오예 파일이 수천개여도 다 읽어올 수 있다능
            
# 텍스트 파일 쓰기
# 는 내년에 계속....