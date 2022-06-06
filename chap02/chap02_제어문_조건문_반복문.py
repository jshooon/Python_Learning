#!/usr/bin/env python
# coding: utf-8

# # 2022.06.06 변수와 자료형

# ### 3.1 제어문,
# ### 3.2 조건문
# ### 3.2.1 단일 조건문
# * 단일조건문 형식1 예문

# In[ ]:


var = 10                  # if 블럭에서 사용될 변수
if var >= 5:              # 조건식
    print('var = ', var)
    print('var는 5보다 크다.')
    print('조건이 참인 경우 실행')
    
print('항상 실행')


# * 단일 조건문 형식2 예문

# In[ ]:


# 100 ~ 85 : '우수', 84 ~ 70 : '보통', 69이하 : '저조'
score = int (input('점수 입력 : '))

if score >= 85 and score <=100 :
    print('우수')
else :
    if score >= 70 : 
        print('보통')
    else :
        print('저조')            # 69이하


# ### 3.2.2 중첩 조건문
# * 중첩 조건문 예

# In[ ]:


score = int (input('점수 입력 : '))
grade = ' '                      #등급

if score >= 85 and score <=100 :
    grade = '우수'
elif score >= 70 :
    grade = '보통'
else :
    grade = '저조'            # 69이하
    
print('당신의 점수는 %d이고, 등급은 %s'%(score, grade))


# ### 3.2.3 삼항 조건문
# * 삼항 조건문 예

# In[ ]:


# (1) 일반 조건문
num = 9            # 초기화
result = 0

if num >= 5 :
    result = num * 2
else : 
    result = num + 2
print('result = ', result)

# (2) 3항 연산자
# 형식) 변수 = 참 if (조건문) else 거짓
result2 = num * 2 if num >= 5 else num + 2
print('result2 = ', result2)


# ### 3.3 반복문
# ### 3.3.1 while
# * while 반복문 예

# In[ ]:


# (1) 카운터와 누적변수
cnt = tot = 0           # 변수 초기화
while cnt < 5 :         # True : loop 수행
    cnt += 1             # 카운터 변수 (cnt = cnt + 1)
    tot += cnt           # 누적변수 : tot = tot + cnt
    print(cnt , tot)


# In[1]:


# [실습] 1 ~ 100 사이 3의 배수 합과 원소 추출하기
cnt = tot = 0
dataset = []           # 빈 list

while cnt < 100 :    # 100회 반복
    cnt += 1           # 카운터
    if cnt % 3 == 0 : 
        tot += cnt     # 누적변수
        dataset.append(cnt)      # cnt 추가

print('1 ~ 100 사이 3의 배수 합 = %d ' % tot )
print('dataset = ', dataset)


# * 무한 루프(loop) 예

# In[2]:


# 무한 루프(loop)
numData = []

while True :
    num = int(input('숫자 입력 : '))
    
    if num % 10 == 0 :            # exit 조건식
        print('프로그램 종료')
        break
    else : 
        print(num)
        numData.append(num)    # list 추가


# ### 3.3.2 random 모듈
# * random 관련 함수1 예

# In[7]:


# (1) random module 추가
import random as rd
#help(rd)                  # 모듈 도움말

# (2) random모듈의 함수 도움말
#help(rd.random)

# (3) 0 ~ 1 사이 난수 실수
r = rd.random()
print('r  = ', r)


# In[59]:


# [실습] 난수 0.01 미만이면 종료 후 난수 개수 출력
cnt = 0

while True : 
    r = rd.random()
    if r < 0.01 :
        break        # loop exit
    else : 
        cnt += 1
print('난수 개수 = ', cnt)


# * random 관련 함수2 예

# In[61]:


# (1) random모듈 관련 함수 도움말
help(rd.randint)
help(rd.choices)     # 모집단에서 k 크기 목록 반환

# (2) 이름 list에 전체 이름, 특정 이름 출력
names = ['홍길동', '이순신', '유관순']
print(names)       # 전체 이름
print(names[2])    # , 특정 이름 출력

# (3) list에서 자료 유무 확인하기
if '유관순' in names :
    print('유관순 계심')
else :
    print('유관순 안계심')
    
# (4) 난수 정수로 이름 선택하기
idx = rd.randint(0, 2)
print(names[idx])


# ### 3.3.3 break, continue
# * break, continue 예

# In[62]:


i = 0
while i < 10 :
    i += 1             # 카운터
    if i == 3 :
        continue      # 다음 문장 skip
    if i == 6 :         # 탈출 조건
        break          # exit
    print(i, end = ' ')


# ### 3.3.4 for
# * for 반복문 예

# In[63]:


# (1) 문자열 열거형객체 이용
string = '홍길동'
print(len(string))       # 문자 길이 : 3
for s in string :        # 1문자 -> 변수 넘김 : 3
    print(s)
    
# (2) list 열거형객체 이용
lstset = [1,2,3,4,5] # 5개 원소를 갖는 열거형객체

for e in lstset :
    print('원소 : ', e)


# ### 3.3.5 for & range
# * range 클래스 예

# In[64]:


# (1) range 객체 생성
num1 = range(10)          # range(start)
print('num1 : ', num1)
num2 = range(1,10)        # range(start, stop)
print('num2 : ', num2)
num3 = range(1, 10, 2)    # range(start, stop, step)
print('num3 : ', num3)

# (2) range 객체 활용
for n in num1 :
    print(n, end = ' ')
print()
for n in num2 : 
    print(n, end = ' ')
print()
for n in num3 :
    print(n, end = ' ')


# ### 3.3.6 for & list
# * list 자료구조 예

# In[67]:


# (1) lsit에 자료 저장하기
lst = []      # 빈 list 만들기
for i in range(10) :           # 0 ~ 9
    r = rd.randint(1,10)       # 난수 발생
    lst.append(r)                # 난수 저장

print('lst = ', lst)               # 난수 출력

# (2) list에 자료 참조하기
for i in range(10) :            # 0 ~ 9
    print(lst[i] * 0.25)          # 난수 * 0.25


# ### 3.3.7 중첩 반복문
# * 구구단 예

# In[68]:


# 구구단 출력 : range() 함수 이용

# (1) 바같쪽 반복문
for i in range(2, 10) :
    print('--- {}단 ---'.format(i))
    
    # (2) 안쪽 반복문
    for j in range(1, 10) :
        print('%d * %d = %d '%(i, j , i*j))


# * 문장과 단어 추출 예

# In[69]:


string = '''나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 35세 입니다.'''

sents = []  # 문장 저장
words = [] # 단어 저장

# (1) 문단 -> 문장
for sen in string.split(sep = '\n') : 
    sents.append(sen)
    # (2) 문장 -> 단어
    for word in sen.split() : 
        words.append(word)
        
print('문장 : ', sents)
print('문장 수 : ', len(sents))
print('단어 : ', words)
print('단어 수 : ', len(words))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




