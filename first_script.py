#!/usr/bin/env python3
from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta
# time 함수는 어떻게 쓰는 걸까
from operator import itemgetter

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
# time은 이런 식으로 가져올 때 쓴다 


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
print("{}".format(tuple_copy))

# 72p부터 이어서

