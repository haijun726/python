#!/usr/bin/python
# -*- coding: gb2312-*-
import os
import pickle
#�ж�ͨѶ¼�Ƿ���ڣ��������򴴽���ͨѶ¼
if os.path.exists(r'E:\work\python\Person.data')==False:
    f=open('E:\work\python\Person.data','wb')
    temp={'total' : 0}
    pickle.dump(temp,f)
    f.close()
else:
    pass
#�����ϵ��
def add():
    f=open('E:\work\python\Person.data','rb')
    a=pickle.load(f)
    f.close()
    b=0
    name = input('��������Ҫ�����ϵ�˵�����:')
    for key in a.keys():
        b+=1
        if key==name and b <= a['total']+1:
            print("��ϵ���Ѵ��ڣ����ʧ�ܣ�")
            break
        if b==a['total']+1 and key != name:        
            number = input('���������:')
            information={name : number}
            a['total']+=1
            a.update(information)
            f=open('E:\work\python\Person.data','wb')
            pickle.dump(a,f)
            f.close()
            print('��ӳɹ�!')
            break
#��ʾ������ϵ��
def showall():
    f=open('E:\work\python\Person.data','rb')
    a=pickle.load(f)
    print("һ����{}����ϵ��.".format(a['total']))
    for key in a.keys():
        if key != 'total':
            print("{""}:{""}".format(key,a[key]))
    f.close()
#�˳�ͨѶ¼
def exit():
    exec("quit()")
#����
def search(name):
    f=open('E:\work\python\Person.data','rb')
    a=pickle.load(f)
    b=0
    for key in a.keys():
        b+=1
        if key==name and b<=a['total']+1:
            print("{}�ĺ�����: {}".format(name,a[key]))
            break
        if b==a['total']+1 and key != name:
            print("��ϵ�˲�����!")
            break
    f.close()
#ɾ��
def deleate(name):
    f=open('E:\work\python\Person.data','rb')
    a=pickle.load(f)
    f.close()
    b=0
    for key in a.keys():
        b+=1
        if key==name and b<=a['total']+1:
            a.pop(name)
            a['total']-=1
            f=open('E:\work\python\Person.data','wb')
            pickle.dump(a,f)
            f.close()
            print("ɾ���ɹ�!")
            break
        if b==a['total']+1 and key != name:
            print("��ϵ�˲����ڣ��޷�ɾ����")
            break
#�޸�
def change ():
    x=input("��������Ҫ�޸���ϵ������:")
    f=open('E:\work\python\Person.data','rb')
    a=pickle.load(f)
    f.close()
    b=0
    for key in a.keys():
        b+=1
        if key==x and b<=a['total']+1:
            y=input("�������޺�ĺ���:")
            a[key]=y
            f=open('E:\work\python\Person.data','wb')
            pickle.dump(a,f)
            f.close()
            print("�޸ĳɹ�!")
            break
        if b==a['total']+1 and key != name:
            print("��ϵ�˲����ڣ�")
            break
#����
def point ():
    print("*******************************")
    print("��ʾ��ʾ��Ϣ:*")
    print("��ʾ������ϵ��:0")
    print("������ϵ��:1")
    print("�����ϵ��:2")
    print("ɾ����ϵ��:3")
    print("������ϵ������:4")
    print("�˳�ͨѶ¼:5")
    print("*******************************")
#������
print("��ӭ�������޵�˽��ͨѶ¼!")
point()
while True:
    x=input("����������ѡ��:")
    if x == '2':
        add()
        continue
    if x== '0':
        showall()
        continue
    if x=='5':
        exit()
        continue
    if x=='1':
        name=input("��������Ҫ������ϵ�˵�����:")
        search(name)
        continue
    if x=='3':
        name=input("��������Ҫɾ����ϵ�˵�����:")
        deleate(name)
        continue
    if x== '4':
        change()
        continue
    if x=='*':
        point()
    else:
        print("����ѡ����ڣ����������룡")
        continue