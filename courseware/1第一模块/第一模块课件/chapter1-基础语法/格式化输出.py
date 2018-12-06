#_*_coding:utf-8_*_



name = input("Name:")
age = input("Age:")
job = input("Job:")
hometown = input("Hometown:")

info = """
----------- info of %s ----------
Name:       %s
Age:        %s
Job:        %s
Hometown:   %s
---------- end ------------------
""" % (name,name,age,job,hometown)

print(info)