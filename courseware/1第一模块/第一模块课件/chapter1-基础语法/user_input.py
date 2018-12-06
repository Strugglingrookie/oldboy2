

# name = input("what's your name:")
# print("Hello " + name )
#
# username = input("username:")
# password = input("password:")
#
# print(username,password)


# msg = """my name is shanshn ,
#       i'm 22 years old
#
#       """
# print(msg)


name = input("Name:")
age  = int(  input("Age:")  )
job = input("Job:")
hometown = input("Hometown:")

print(type(name),type(age))

# print("----------info of ", name,'----')
# print("|Name:",name,"          |")
# print("Age:",age)
# print("Job:",job)
# print("----------end----")

info = """
--------- info of %s ---------
Name:       %s 
Age :       %s
Job :       %s
Hometown:   %s 
---------- end ----------------
""" % (name, name,age,job,hometown)
#s = string
#d = digit
#f = float
print(info)


