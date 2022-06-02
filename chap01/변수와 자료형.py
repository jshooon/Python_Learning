#!/usr/bin/env python
# coding: utf-8

# # 2022.06.02 변수와 자료형

# ### 2.1.1 변수 
# * 변수와 메모리 주소(address) 예

# In[1]:


var1 = "Hello python"
print(var1)
print( id(var1) )


# In[2]:


var1 = 100
print(var1)
print( id(var1) )


# In[3]:


var2 = 150.25
print(var2)
print(id(var2))


# In[4]:


var3 = True
print(var3)
print(id(var3))


# ### 파이썬 예약어 확인 예

# In[6]:


# 예약어 확인
import keyword # 모듈 임포트
python_keyword = keyword.kwlist
print(python_keyword)


# In[7]:


print(type(python_keyword))
print(len(python_keyword))


# ### 2.1.2 자료형
# * 변수와 자료형 예

# In[8]:


var1 = "Hello python"
print(var1)
print(type(var1))


# In[9]:


var1 = 100
print(var1)
print(type(var1))


# In[10]:


var2 = 150.25
print(var2)
print(type(var2))


# In[11]:


var3 = True
print(var3)
print(type(var3))


# * 자료형 변환 예

# In[12]:


# 실수 -> 정수
a = int(10.5)
b = int(20.42)
add = a + b
print('add = ', add)


# In[13]:


# 정수 -> 실수
a = float(10)
b = float(20)
add2 = a + b
print('add2 = ', add2)


# In[14]:


# 논리형 -> 정수
print(int(True))     # 1
print(int(False))    # 0


# In[15]:


# 문자형 -> 정수
st = '10'
print(int(st) ** 2)   # 제곱 연산


# ### 2.2 연산자(Operator)

# ### 2.2.1 산술연산자
# * 산술연산자 예

# In[3]:


num1 = 100 # 피연산자1
num2 = 20  # 피연산자2


# In[5]:


add = num1 + num2     # 덧셈
print('add = ', add)
sub = num1 - num2     # 뺄셈
print('sub = ', sub)
mul = num1 * num2     # 곱셈
print('mul = ', mul)
div = num1 / num2     # 나눗셈
print('div = ', div)
div2 = num1 % num2    # 나머지 계산
print('div2 = ', div2)
square = num1**2      # 제곱 계산
print('square = ', square)


# ### 2.2.2 관계연산자
# * 관계연산자 예

# In[7]:


# (1)  동등비교
bool_result = num1 == num2 # 두 변수의 값이 같은지 비교
print(bool_result)
bool_result = num1 != num2 # 두 변수의 값이 다른지 비교
print(bool_result)


# In[8]:


# (2) 크기비교
bool_result = num1 > num2 # num1값이 큰지 비교
print(bool_result)
bool_result = num1 >= num2 # num1값이 크거나 같은지 비교
print(bool_result)
bool_result = num1 < num2 # num2값이 큰지 비교
print(bool_result)
bool_result = num1 <= num2 # num2값이 크거나 같은지 비교
print(bool_result)


# ### 2.2.3 논리연산자
# * 논리연산자 예

# In[9]:


# 두 관계식이 같은지 판단
log_result = num1 >= 50 and num2 <= 10
print(log_result)


# In[11]:


# 두 관계식 중 하나라도 같은지 판단
log_result = num1 >= 40 or num2 <=10
print(log_result)

log_result = num1 >=50 # 관계식 판단
print(log_result)


# In[12]:


# 괄호 안의 관계식 판단 결과에 대한 부정
log_result = not(num1 >= 50)
print(log_result)


# ### 2.2.4 대입연산자
# * 대입연산자 예

# In[14]:


# (1) 변수에 값 할당(=)
i = tot = 10 # i = 10; toto = 10
i += 1       # i = i + 1
tot += i     # tot = tot + i
print(i, tot)
# 같은 줄에 중복 출력
print('출력1', end =' , ')  # end = '구분자'
print('출력2')


# In[15]:


# (2) 변수 교체
v1, v2 = 100,200
v2, v1 = v1, v2
print(v1, v2)    # 200 100


# In[18]:


# (3) 패킹(packing) 할당
lst = [1,2,3,4,5]
v1, *v2 = lst
print(v1, v2)
*v1, v2 = lst
print(v1, v2)


# ### 2.3 표준입출력장치

# ### 2.3.1 표준입력장치
# * 표준입력장치 예

# In[22]:


# (1) 문자형 숫자 입력
num = input('숫자 입력 : ')
print('num type : ', type(num)) # str타입
print('num = ', num)
print('num = ', num*2)


# In[23]:


# (2) 문자형 숫자를 정수형으로 변환
num1 = int( input('숫자 입력 : ' ) ) # str -> int(형변환)
print('num1 = ', num1*2)


# In[24]:


# (3) 문자형 숫자를 실수형으로 변환
num2 = float( input('숫자 입력 : ') ) # str -> float(형변환)
result = num1 + num2 # 실수 = 정수 + 실수
print('result = ', result)


# ### 2.3.2 표준출력장치
# * 표준출력장치 예

# In[26]:


# (1) value 인수
print("value = ", 10 + 20 + 30 + 40 + 50)


# In[27]:


# (2) sep 인수 : 값과 값을 특수문자로 구분
print("010", "1234", "5678", sep="-")


# In[28]:


# (3) end 인수
print("value = ", 10, end = " , ")
print("vlaue = ", 20)


# ### 2.3.3 format과 양식문자
# * format과 양식문자 예

# In[29]:


# (4) format() 함수 임수 : format(value, "format")
print("원주율 = ", format(3.14159, "8.3f"))
print("금액 = ", format(10000, "10d"))
print("금액 = ", format(125000, "3,d"))


# In[32]:


# (5) 양식문자 인수 : print("%양식문자" %(값))
name = "홍길동"
age = 35
price = 125.456
print("이름 : %s, 나이 : %d, data = %.2f" %(name, age, price))


# ### 2.3.4 외부상수 출력
# * 외부상수 출력 예

# In[33]:


# (6) 외부 상수 인수
print("이름 : {}, 나이 : {}, data = {}".format(name,age,price))
print("이름 : {1}, 나이 : {0}, data = {2}".format(age,name,price))


# In[35]:


# (7) format 축약형(SQL문 작성)
uid = input("id input : ")
query = f"SELECT * FROM member WHERE uid = {uid}"
print(query) # member 테이블에서 uid가 hong인 레코드 검색


# ### 2.4 문자열(String)
# * 문자열 유형 예

# In[36]:


# 문자열 유형
oneLine = "this is one line string"
print(oneLine)

multiLine = """this is
multi line
string"""
print(multiLine)

multiLine2 = "this is \nmulti line\nstring"
print(multiLine2)


# ### 2.4.1 문자열 특징
# * 문자열 색인과 연산 예

# In[38]:


# (1) 문자열 색인
string = "PYTHON"
print(string[0])
print(string[5])
print(string[-1])
print(string[-6])


# In[42]:


# (1) 문자열 연산
print("python" + " program") # 결합연산자
# print("python-" + 3.7 + ".exe") # error
print("python-" + str(3.7) + ".exe") # python-3.7.exe

print("-"*30) # 반복연산자


# ### 2.4.2 슬라이싱(slicing)
# * 슬라이싱 예

# In[43]:


# (1) 왼쪽 기준
print(oneLine)
print("문자열 길이 : ", len(oneLine))
print(oneLine[0:4])
print(oneLine[:4])
print(oneLine[:])   # 전체 원소
print(oneLine[::2]) # 2의 배수 index


# In[44]:


# (2) 오른쪽 기준
print(oneLine)
print(oneLine[0:-1:2])
print(oneLine[-6:-1])
print(oneLine[-6:])


# In[46]:


# (3) 부분 문자열 생성
print(oneLine)
subString = oneLine[-11:]
print(subString)


# ### 2.4.3 문자열 처리 함수
# * 문자열 처리 함수 예

# In[47]:


# (1) 특정 글자 수 반환
oneLine = "this is one line string"
print('t 글자 수 : ', oneLine.count('t'))


# In[48]:


# (2) 접두어 문자 비교 판단
print(oneLine.startswith('this'))
print(oneLine.startswith('that'))


# In[49]:


# (3) 문자열 교체
print(oneLine.replace('this', 'that'))


# In[50]:


# (4) 문자열 분리(split : 문단 -> 문장
multiLine = """this is
multi line
string"""
sent = multiLine.split('\n')
print('문장 : ', sent)


# In[51]:


# (5) 문자열 분리(split)2 : 문장 -> 단어
words = oneLine.split(' ') # split(sep = ' ') : default
print(words)


# In[52]:


# (6) 문자열 결합(join) : eksdj -> answkd
sent2 = ','.join(words) # '구분자'.join(string)
print(sent2)


# ### 2.4.4 이스케이프 문자 (escape character)
# * 이스케이프 문자 기능 차단 예

# In[53]:


# (1) escape 문자 적용
print('escape 문자 차단')
print('\n출력 이스케이프 문자') # \n : 줄 바꿈 기능


# In[54]:


# (2) escape 문자 기능 차단
print('\\n출력 이스케이프 기능 차단1')
print(r'\n출력 이스케이프 기능 차단2')


# In[55]:


# (3) 경로 표현 : C:\Python\test
print('path = ', 'C:\Python\test')
print('path = ', 'C:\\Python\\test')
print('path = ', r'C:\Python\test')

