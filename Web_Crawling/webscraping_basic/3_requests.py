#!/usr/bin/python
# -*- coding: euc-kr -*-

import requests
res = requests.get("http://google.com")
res.raise_for_status() #�ùٸ� �ڵ尡 �ƴҶ��� error�� �߻���Ű�� ���α׷� ����, ����� �Ǹ� �״�� ����

#print("status code :", res.status_code) #return 200 if ok, return 403 if error

#if res.status_code == requests.codes.ok:
#    print("�����Դϴ�.")
#else: 
#    print("������ ������ϴ�. [�����ڵ�:", res.status_code,"]")

print(len(res.text))

#���Ϸ� �����
with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)