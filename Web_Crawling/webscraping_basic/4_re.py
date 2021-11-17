#!/usr/bin/python
# -*- coding: euc-kr -*-

#���Խ� ����

import re #���Խ� ���̺귯��
p = re.compile("ca.e") 
# . : �ϳ��� ����(ca.e -> case, cave ��) 
# ^ : ���ڿ��� ����(^de -> de�� �����ϴ� �͵� matching. desk, deny, destination ��) 
# $ : ���ڿ��� ��(se$ -> se�� ������ �͵� matching. case, base ��)

def print_match(m):
    if m: 
        print("m.group(): ", m.group()) # group: ��ġ�ϴ� ���ڿ� ��ȯ. match���� ������ ���� �߻�
        print("m.string: ", m.string) # string: �Է¹��� ���ڿ� ��ȯ
        print("m.start(): ", m.start()) #��ġ�ϴ� ���ڿ��� ���� index
        print("m.end():", m.end()) # ��ġ�ϴ� ���ڿ��� �� index
        print("m.span(): ", m.span()) #��ġ�ϴ� ���ڿ��� ���� / �� index
    else:
        print("��Ī���� �ʾҽ��ϴ�")
        

m = p.match("careless") # good care�� error. careless�� care�� ��Ī�ȴٰ� care ��µ�. b/c match�� �־��� ���ڿ��� ó������ ��ġ�ϴ��� Ȯ��
print_match(m)

s = p.search("good care") # search: �־��� ���ڿ� �߿� ��ġ�ϴ°� �ִ��� Ȯ��
print_match(s)

f = p.findall("careless case exists in our life") # ��ġ�ϴ� ��� ���� ����Ʈ ���·� ��ȯ
print(f)


#1. re.compile("���ϴ� ����") �� ���Խ� ���� ����
#2. �� = p.match()/search()/findall() ���� ���� Ȱ�� ����

# ���ϴ� ���� : . ^ $ �� �̿��ؼ� ǥ�� ����