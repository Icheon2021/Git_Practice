#!/usr/bin/python
# -*- coding: euc-kr -*-

#정규식 예시

import re #정규식 라이브러리
p = re.compile("ca.e") 
# . : 하나의 문자(ca.e -> case, cave 등) 
# ^ : 문자열의 시작(^de -> de로 시작하는 것들 matching. desk, deny, destination 등) 
# $ : 문자열의 끝(se$ -> se로 끝나는 것들 matching. case, base 등)

def print_match(m):
    if m: 
        print("m.group(): ", m.group()) # group: 일치하는 문자열 반환. match되지 않으면 에러 발생
        print("m.string: ", m.string) # string: 입력받은 문자열 반환
        print("m.start(): ", m.start()) #일치하는 문자열의 시작 index
        print("m.end():", m.end()) # 일치하는 문자열의 끝 index
        print("m.span(): ", m.span()) #일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않았습니다")
        

m = p.match("careless") # good care는 error. careless는 care가 매칭된다고 care 출력됨. b/c match는 주어진 문자열의 처음부터 일치하는지 확인
print_match(m)

s = p.search("good care") # search: 주어진 문자열 중에 일치하는게 있는지 확인
print_match(s)

f = p.findall("careless case exists in our life") # 일치하는 모든 것을 리스트 형태로 반환
print(f)


#1. re.compile("원하는 형태") 로 정규식 형태 규정
#2. ㅡ = p.match()/search()/findall() 등을 통해 활용 가능

# 원하는 형태 : . ^ $ 를 이용해서 표현 가능