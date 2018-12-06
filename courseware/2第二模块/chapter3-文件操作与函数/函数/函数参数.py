#_*_coding:utf-8_*_
#
# def stu_register(name, age,country, course ):
#     print("----ע��ѧ����Ϣ------")
#     print("����:", name)
#     print("age:", age)
#     print("����:", country)
#     print("�γ�:", course)
#
#
# stu_register("��ɽ��", 22, "CN", "python_devops")
# stu_register("�Žд�", 21, "CN", "linux")
# stu_register("���ϸ�", 25, "CN", "linux")


#
# def stu_register(name, age, course='PY' ,country='CN'):
#     print("----ע��ѧ����Ϣ------")
#     print("����:", name)
#     print("age:", age)
#     print("����:", country)
#     print("�γ�:", course)
#     if age > 22:
#         return False
#     else:
#         return True
#
# registriation_status = stu_register("��ɽ��",22,course="PYȫջ����",country='JP')
#
# if registriation_status:
#     print("ע��ɹ�")
#
# else:
#     print("too old to be a student.")



def func(name,*args,**kwargs):
    print(name,args,kwargs)



func('Alex',22,'tesla','500w',addr='ɽ��',num=12442323)

d = {'degree':'primary school'}
func('Peiqi',**d)





