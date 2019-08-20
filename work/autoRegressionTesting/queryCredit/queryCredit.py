import pymongo
import requests
import time
import os
import string
from random import choice,randint

files = {
    'multiple1': ['A-01', open(os.path.join(os.path.dirname(__file__),'A-01-个人借款及担保申请表.jpg'), 'rb') ],
    'multiple2': ['A-06', open(os.path.join(os.path.dirname(__file__),'A-06-征信查询授权书.jpg'), 'rb') ],
    'multiple3': ['A-08', open(os.path.join(os.path.dirname(__file__),'A-08-第二代身份证.jpg'), 'rb') ],
}

address_info = {
    'workAddress': [('广东省'), ( '深圳市'), ('南山区')],
    'familyAddress': [('广东省'), ( '深圳市'), ('南山区')]
}

final_data_dict = {}

def format_timestamp(timeNum,format='%Y-%m-%d %H:%M:%S'):
    if len(str(timeNum))>10:
        timeStamp = float(timeNum / 1000)
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime(format, timeArray)
    else:
        timeArray = time.localtime(timeNum)
        otherStyleTime = time.strftime(format, timeArray)
    return otherStyleTime



def change_timestamp(specify_time,format='%Y-%m-%d %H:%M:%S'):
    timestamp =  time.mktime(time.strptime(specify_time,format))
    timestamp = timestamp * 1000
    return timestamp


def upload_img(plms_uploadImg_url):
    response = requests.post(
        url=plms_uploadImg_url,
        files=files,
        data={
            'source': '05'
        },
        verify=False
    )
    return response.json()['content']


def fetch_result(inne_urls,name,cert_no):
    start_time = time.time()
    while True:
        response = requests.post(
            url = inne_urls['query_result'],
            json={
                'certId':cert_no,
                'orgId':'75501',
                'pageNo':1,
                'pageSize':30
            },
            headers={
                'source':'WPT'
            },
            verify=False
        )
        if response.json()['data']['list']:
            return  response.json()

        elif time.time() - start_time > 35:
            raise Exception('【%s】征信报告解析失败!'%name)
        time.sleep(2)


def format_data(query_result):
    dict_result = query_result['data']['list'][0]
    final_data_dict.update(dict_result)

    user_tags = dict(dict_result['userTags'].items())
    final_data_dict.update(user_tags)
    del final_data_dict['userTags']

    final_data_dict.update({'serialNo': dict_result['applyId']})
    del final_data_dict['applyId']

    final_data_dict.update({'certNo': dict_result['certId']})
    del final_data_dict['certId']

    final_data_dict.update({'bankInfo': dict_result['helpLoanResults']})
    del final_data_dict['helpLoanResults']

    # #转换成13位时间戳
    final_data_dict.update({'reportTime': change_timestamp(dict_result['reportTime'])})

    final_data_dict.update({'timestamp': change_timestamp(dict_result['queryDate'])})
    del final_data_dict['queryDate']

    del final_data_dict['triggerEvent']
    del final_data_dict['rejectCodes']

    final_data_dict.update({'familyAddress': address_info['familyAddress']})
    final_data_dict.update({'workAddress': address_info['workAddress']})

    return final_data_dict

def save_to_mongoDB(mongo_conn,query_result):
    client = pymongo.MongoClient(host=mongo_conn[0], port=mongo_conn[1])
    conn = client.wpt
    cursor = conn.wpt_credit

    format_data(query_result)
    try:
        final_data_dict.update({"_id":"".join([choice(string.hexdigits) for _ in range(24)])})
        cursor.insert_one(final_data_dict)
    except Exception:
        raise Exception('作业平台数据库连接超时,请检查!')
    finally:
        client.close()


def query_credit(inne_urls,imgs,name,cert_no,company,platform='LEAGUER'):
    wpt_no = 'I00002'
    current_time = time.localtime()
    year = (current_time[0])
    year = str(year)[2:4]

    month = (current_time[1])
    if month < 10:
        month = ''.join(['0', str(month)])
    else:
        month = str((current_time[1]))

    day = (current_time[2])
    if day < 10:
        day = ''.join(['0', str(day)])
    else:
        day = str((current_time[2]))

    final_time = ''.join([year, month, day])

    num = ''
    for i in range(10):
        num1 = randint(1, 9)
        num += str(num1)

    serialNo = ''.join([wpt_no, final_time, num])

    credit_data = {
        'customerName': name,
        'certNo': cert_no,
        'serialNo': serialNo,
        'customerType': '001',
        'certType': 'Ind01',
        'outlet': '75501',
        'searcher': 'XIAOWD',
        'platform': platform,
        'saleChannel': '004',
        'triggerEvent': 'WPT',
        'authority': '南山公安局',
        'address': '广东省深圳市南山区',
        'employeeType': '010',
        'phone': '',
        'customerMgr': '152',
        'listImage':[
            {'imageSource': '06', 'imageNo': imgs[0], 'imageType': '00'},
            {'imageSource': '06', 'imageNo': imgs[1], 'imageType': '00'},
            {'imageSource': '06', 'imageNo': imgs[2], 'imageType': '00'},
        ],
        'companyName': company,

        'workAddress': {'province': '广东省', 'city': '深圳市', 'district': '南山区'},
        'familyAddress':{'province': '广东省', 'city': '深圳市', 'district': '南山区'}
    }
    final_data_dict.update(credit_data)

    response = requests.post(
        url=inne_urls['query_credit'],
        json=credit_data,
        headers={
            'source': 'WPT',
        },
        verify=False
    )
    return  response.json()

def run(inne_urls,mongo_conn,name,cert_no,company='北京小桔科技有限公司'):
    imgs = upload_img("https://testplmssit01image.yylending.com/Image/service/imageUpload")
    query_credit(inne_urls,imgs,name,cert_no,company)
    query_result = fetch_result(inne_urls,name,cert_no)
    save_to_mongoDB(mongo_conn,query_result)











