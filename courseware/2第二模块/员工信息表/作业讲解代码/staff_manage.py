# _*_coding:utf-8_*_
# created by Alex Li on 10/22/17
from tabulate import tabulate
import os

DB_FILE = "staff.db"
COLUMNS = ['id','name','age','phone','dept','enrolled_date']



def print_log(msg,log_type="info"):
    if log_type == 'info':
        print("\033[32;1m%s\033[0m"%msg)
    elif log_type == 'error':
        print("\033[31;1m%s\033[0m"%msg)


def load_db(db_file):
    """
    加载员工信息表，并转成指定的格式
    :param db_file: 
    :return: 
    """
    data = {}
    for i in COLUMNS:
        data[i] = []

    f = open(db_file,"r")
    for line in f:
        staff_id,name,age,phone,dept,enrolled_date  = line.split(",")
        data['id'].append(staff_id)
        data['name'].append(name)
        data['age'].append(age)
        data['phone'].append(phone)
        data['dept'].append(dept)
        data['enrolled_date'].append(enrolled_date)
    #print_log(data)
    return data

def save_db():
    """把内存数据存回硬盘"""
    f = open("%s.new"%DB_FILE,"w",encoding="utf-8")
    for index,staff_id in enumerate(STAFF_DATA['id']):
        row = []
        for col in COLUMNS:
            row.append( STAFF_DATA[col][index] )
        f.write( ",".join(row) )
    f.close()

    os.rename("%s.new"%DB_FILE,DB_FILE)


STAFF_DATA = load_db(DB_FILE) #程序一启动就执行

def op_gt(column,condtion_val):
    """
    
    :param column: eg.age
    :param condtion_val: eg.22
    :return: [[id,name,age,phone],...]
    """
    matched_records = []
    for index,val in enumerate(STAFF_DATA[column]): #"age": [22,445,2,5,2]
        if float(val) > float(condtion_val):#匹配上了
            #print("match",val)
            # matched_records.append(STAFF_DATA['id'][index])
            # matched_records.append(STAFF_DATA['name'][index])
            # matched_records.append(STAFF_DATA['age'][index])
            record = []
            for col in COLUMNS:
                record.append(STAFF_DATA[col][index])
            matched_records.append(record)
    #print("matched records",matched_records)
    return matched_records

def op_lt(column,condtion_val):

    matched_records = []
    for index,val in enumerate(STAFF_DATA[column]): #"age": [22,445,2,5,2]
        if float(val) < float(condtion_val):#匹配上了
            record = []
            for col in COLUMNS:
                record.append(STAFF_DATA[col][index])
            matched_records.append(record)

    return matched_records

def op_eq(column,condtion_val):

    matched_records = []
    for index,val in enumerate(STAFF_DATA[column]): #"age": [22,445,2,5,2]
        if val == condtion_val:#匹配上了
            record = []
            for col in COLUMNS:
                record.append(STAFF_DATA[col][index])
            matched_records.append(record)
    return matched_records

def op_like(column,condtion_val):

    matched_records = []
    for index,val in enumerate(STAFF_DATA[column]): #"age": [22,445,2,5,2]
        if  condtion_val in val :#匹配上了

            record = []
            for col in COLUMNS:
                record.append(STAFF_DATA[col][index])
            matched_records.append(record)
    return matched_records

def syntax_where(clause):
    """
    解析where条件，并过滤数据
    :param clause: eg. age>22
    :return: 
    """
    operators =  {
        '>':op_gt,
        '<':op_lt,
        '=':op_eq,
        'like':op_like,
    }

    for op_key,op_func in operators.items():
        if op_key in clause:
            column,val = clause.split(op_key)
            matched_data =op_func(column.strip(),val.strip()) #真正的查询数据去啦
            #print_log(matched_data)
            return matched_data

    else: #只有在for执行完成 ，且没有中间被 break的情况 下，才执行
        #没匹配上任何的条件公式
        print_log("语法错误:where条件只能支持[>,<,=,like]",'error')

def syntax_find(data_set,query_clause):
    """
    解析查询语句并从data_set中打印指定的列
    :param data_set: eg.[['1', 'Alex Li', '22', '13651054608', 'IT', '2013-04-01\n'], ['3', 'Rain Wang', '21', '13451054608', 'IT', '2017-04-01\n'], ['5', 'Rachel Chen', '23', '13351024606', 'IT', '2013-03-16\n'], ['9', 'Shit Wen', '20', '13351024602', 'IT', '2017-07-03\n']]
    :param query_clause: eg. find name,age from staff_table
    :return: 
    """
    filter_cols_tmp = query_clause.split("from")[0][4:].split(',')
    filter_cols = [i.strip() for i in filter_cols_tmp] #干净的columns
    if '*' in filter_cols[0]:
        print(tabulate(data_set, headers=COLUMNS, tablefmt="grid"))
    else:
        reformat_data_set = []
        for row in data_set:
            filtered_vals = [] #把要打印的字段放在这个列表里
            for col in filter_cols:
                col_index = COLUMNS.index(col) #拿到列的索引，依此取出每条纪录里对应索引的值
                filtered_vals.append( row[col_index] )
            reformat_data_set.append(filtered_vals)
        print(tabulate(reformat_data_set, headers=filter_cols,tablefmt="grid"))

    print_log("匹配到%s条数据!" % len(data_set))


def syntax_delete(data_set,query_clause):
    pass

def syntax_update(data_set,query_clause):
    """
    
    :param data_set: eg. [['1', 'Alex Li', '22', '13651054608', 'IT', '2013-04-01\n'],...]
    :param query_clause: eg. update staff_table set age=25
    :return: 
    """
    formula_raw = query_clause.split('set')
    if len(formula_raw) > 1: #有set关键字
        col_name,new_val = formula_raw[1].strip().split('=') #age=25
        #col_index = COLUMNS.index(col_name)
        #循环data_set,取到每条纪录的id,拿着这个id到STAFF_DATA['id'] 里找对应的id的索引，
        # 再拿这个索引，去STAFF_DATA['age']列表里，改对应索引的值
        for matched_row in data_set:
            staff_id = matched_row[0]
            staff_id_index = STAFF_DATA['id'].index(staff_id)
            STAFF_DATA[col_name][staff_id_index] = new_val
        print(STAFF_DATA)

        save_db() #把修改后的数据刷到硬盘上
        print_log("成功修改了%s条数据!"% len(data_set))
    else:
        print_log("语法错误:未检测到set关键字!",'error')


def syntax_add(data_set,query_clause):
    pass

def syntax_parser(cmd):
    """
    解析语句，并执行
    1.  
    :param cmd: 
    :return: 
    """

    syntax_list = {
        'find': syntax_find,
        'del': syntax_delete,
        'update': syntax_update,
        'add': syntax_add,
    }

    #find name,age from staff_table where age > 22
    if cmd.split()[0] in ('find','add','del','update'):
        if 'where' in cmd:
            query_clause,where_clause = cmd.split("where")
            matched_records = syntax_where(where_clause)
        else:
            matched_records = []
            for index,staff_id in enumerate(STAFF_DATA['id']):
                record = []
                for col in COLUMNS:
                    record.append(STAFF_DATA[col][index])
                matched_records.append(record)
            query_clause = cmd
        cmd_action = cmd.split()[0]
        if cmd_action in syntax_list:
            syntax_list[cmd_action](matched_records,query_clause)

    else:
        print_log("语法错误:\n[find\\add\del\\update] [column1,..] from [staff_table] [where] [column][>,..][condtion]\n",'error')





def main():
    """
    让用户数据语句，并执行
    :return: 
    """
    while True:
        cmd = input("[staff_db]:").strip()
        #print('cmd',cmd)
        if not cmd: continue

        syntax_parser(cmd.strip())






main() #start program