#!/usr/bin/python
# -*- coding: euc-kr -*-

import requests
res = requests.get("http://google.com")
res.raise_for_status() #올바른 코드가 아닐때는 error를 발생시키고 프로그램 종료, 제대로 되면 그대로 진행

#print("status code :", res.status_code) #return 200 if ok, return 403 if error

#if res.status_code == requests.codes.ok:
#    print("정상입니다.")
#else: 
#    print("문제가 생겼습니다. [에러코드:", res.status_code,"]")

print(len(res.text))

#파일로 만들기
with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)