# -*- coding: utf-8 -*-
# @Time    : 2018/12/8 11:00
# @Author  : Xiao


import os


def chek_not_content(filepath,content):
    lis = os.listdir(filepath)
    for file in lis:
        new_file = os.path.join(filepath,file)
        with open(new_file,"r",encoding="utf-8") as f:
            file_content = f.read()
            f.seek(0)
            if content in file_content:
                print("\033[1;31;40m文件%s内容里有%s\033[0m"%(file,content))
                for line in f:
                    if "个人" in line:
                        print(line)

def chek_contain_content(filepath,content):
    lis = os.listdir(filepath)
    for file in lis:
        new_file = os.path.join(filepath,file)
        if file.endswith("3.html"):
            with open(new_file,"r",encoding="utf-8") as f:
                if content in f.read():
                    print("文件%s内容里有%s"%(file,content))
                else:
                    print("\033[1;31;40m文件%s内容里没有%s\033[0m"%(file,content))

# chek_not_content(r"C:\Users\lenovo\Desktop\html","个人")
# chek_contain_content(r"C:\Users\lenovo\Desktop\html","独立行使和承担本协议项下权利义务的自然人、法人或其他组织")
# chek_contain_content(r"C:\Users\lenovo\Desktop\html","3.借款人根据担保公司、友金服的不时要求如实向出借人、担保公司、友金服提供借款人情况（包括但不限于姓名/名称、身份证号/营业执照号/统一社会信用代码号、学历、联系方式、联系地址、职业信息、联系人信息、财务状况等）、借款用途以及在所有网络借贷信息中介机构未偿还借款信息等影响或可能影响出借人权益的相关信息。借款人保证其向出借人、担保公司、友金服提供的所有信息真实、准确、完整。")