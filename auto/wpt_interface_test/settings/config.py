import  os
import sys
import time
import  random
import  logging

env_name = 'sit01'
base_dir = os.path.dirname(os.path.dirname(__file__)).replace('/','\\')
file_path = os.path.join(base_dir,'static','img')


#邮件配置信息
receiver = [
    'liujuni@yonyou.com','lirg@yonyou.com','dengyfd@yonyou.com','weimenga@yonyou.com','zhoujlc@yonyou.com','zhengppb@yonyou.com','yangxga@yonyou.com',
    'lirhb@yonyou.com','xucwa@yonyou.com','gaojuna@yonyou.com','liuxhg@yonyou.com','linqhc@yonyou.com', 'yuanmya@yonyou.com','tangyonge@yonyou.com',
   ]
mail_info = {
    'connect':{
        'host':'mail.yonyou.com',
        'port':25
    },
    'login':{
        'username':'tangyonge',
        'passwd':''
    },
    'sender':'tangyonge@yonyou.com',
    'receiver':receiver,
    'subject':'作业平台自动化测试'
}

#日志层级
log_level_list={
    'debug':logging.DEBUG,
    'info':logging.INFO,
    'warning':logging.WARNING,
    'error':logging.ERROR,
    'critical':logging.critical
}
log_level = log_level_list['info']

#测试报告存放路径
current_time = time.strftime('%y%m%d%H%M%S')
rep = ''.join(['test_report','_',current_time,'.html'])
report_info = {
    'report_dir':os.path.join(base_dir,'report',rep),
    'report_title':'auto_test_report',
    'report_detail':'请查阅用例执行情况'
}



#接口环境配置信息
'''    內评接口配置信息    '''
inner_urls = {
    'sit01': {
        'upload_report': 'http://172.30.0.3:8080/InnerEval/api/pbcc/report/fileUpload',
        'inquiry_credit': 'http://172.30.0.3:8080/InnerEval/api/pbcc/report/apply',
        'inquiry_result': 'http://172.30.0.3:8080/InnerEval/api/credit/result/list',
         'admission':       'http://172.30.0.3:8080/InnerEval/api/apply/isAdmission',
        'qcc_company':'http://172.30.0.3:8080/InnerEval/api/company/autoSuggest',
        'soins':'http://172.30.0.3:8080/InnerEval/api/company/autoSuggest',
        'gjj':'http://172.30.0.3:8080/InnerEval/api/gjj/info',
        'insurance':'http://172.30.0.3:8080/InnerEval/api/insurance/list',
        'phone_status':'http://172.30.0.3:8080/InnerEval/api/nifa/queryInEnter',
        'naturalperson': 'http://172.30.0.3:8080/InnerEval/api/correlationcheck/blacklist/naturalperson',



    },
    'sit02': {
        'upload_report': 'http://172.30.0.21:8080/InnerEval/api/pbcc/report/fileUpload',
        'inquiry_credit': 'http://172.30.0.21:8080/InnerEval/api/pbcc/report/apply',
        'inquiry_result': 'http://172.30.0.21:8080/InnerEval/api/credit/result/list',
        'admission':'http://172.30.0.21:8080/InnerEval/api/apply/isAdmission',
        'qcc_company':'http://172.30.0.21:8080/InnerEval/api/company/autoSuggest',
        'soins':'http://172.30.0.21:8080/InnerEval/api/company/autoSuggest',
        'gjj':'http://172.30.0.21:8080/InnerEval/api/gjj/info',
        'insurance':'http://172.30.0.21:8080/InnerEval/api/insurance/list',
        'phone_status':'http://172.30.0.21:8080/InnerEval/api/nifa/queryInEnter',
        'naturalperson':'http://172.30.0.21:8080/InnerEval/api/correlationcheck/blacklist/naturalperson',
    },
    'sit03': {
        'upload_report': 'http://172.30.0.23:8080/InnerEval/api/pbcc/report/fileUpload',
        'inquiry_credit': 'http://172.30.0.23:8080/InnerEval/api/pbcc/report/apply',
        'inquiry_result': 'http://172.30.0.23:8080/InnerEval/api/credit/result/list',
        'admission':        'http://172.30.0.23:8080/InnerEval/api/apply/isAdmission',
        'naturalperson': 'http://172.30.0.23:8080/InnerEval/api/correlationcheck/blacklist/naturalperson',
        'qcc_company': 'http://172.30.0.23:8080/InnerEval/api/company/autoSuggest',
        'soins': 'http://172.30.0.23:8080/InnerEval/api/company/autoSuggest',
        'gjj': 'http://172.30.0.23:8080/InnerEval/api/gjj/info',
        'insurance': 'http://172.30.0.23:8080/InnerEval/api/insurance/list',
        'phone_status': 'http://172.30.0.23:8080/InnerEval/api/nifa/queryInEnter'
    },
    'sit04': {
        'upload_report': 'http://172.29.2.24:8080/InnerEval/api/pbcc/report/fileUpload',
        'inquiry_credit': 'http://172.29.2.24:8080/InnerEval/api/pbcc/report/apply',
        'inquiry_result': 'http://172.29.2.24:8080/InnerEval/api/credit/result/list',
        'admission':        'http://172.29.2.24:8080/InnerEval/api/apply/isAdmission',
        'qcc_company': 'http://172.29.2.24:8080/InnerEval/api/company/autoSuggest',
        'soins': 'http://172.29.2.24:8080/InnerEval/api/company/autoSuggest',
        'gjj': 'http://172.29.2.24:8080/InnerEval/api/gjj/info',
        'insurance': 'http://172.29.2.24:8080/InnerEval/api/insurance/list',
        'phone_status': 'http://172.29.2.24:8080/InnerEval/api/nifa/queryInEnter',
        'naturalperson': 'http://172.29.2.24:8080/InnerEval/api/correlationcheck/blacklist/naturalperson',


    },
    'sit05': {
        'upload_report': 'http://172.29.2.25:8080/InnerEval/api/pbcc/report/fileUpload',
        'inquiry_credit': 'http://172.29.2.25:8080/InnerEval/api/pbcc/report/apply',
        'inquiry_result': 'http://172.29.2.25:8080/InnerEval/api/credit/result/list',
        'admission':        'http://172.29.2.25:8080/InnerEval/api/apply/isAdmission',
        'qcc_company': 'http://172.29.2.25:8080/InnerEval/api/company/autoSuggest',
        'soins': 'http://172.29.2.25:8080/InnerEval/api/company/autoSuggest',
        'gjj': 'http://172.29.2.25:8080/InnerEval/api/gjj/info',
        'insurance': 'http://172.29.2.25:8080/InnerEval/api/insurance/list',
        'phone_status': 'http://172.29.2.25:8080/InnerEval/api/nifa/queryInEnter',
        'naturalperson': 'http://172.29.2.25:8080/InnerEval/api/correlationcheck/blacklist/naturalperson',
    },
    'sit06': {
        'upload_report': 'http://172.29.2.174:8080/InnerEval/api/pbcc/report/fileUpload',
        'inquiry_credit': 'http://172.29.2.174:8080/InnerEval/api/pbcc/report/apply',
        'inquiry_result': 'http://172.29.2.174:8080/InnerEval/api/credit/result/list',
        'admission':        'http://172.29.2.174:8080/InnerEval/api/apply/isAdmission',
        'qcc_company': 'http://172.29.2.174:8080/InnerEval/api/company/autoSuggest',
        'soins': 'http://172.29.2.174:8080/InnerEval/api/company/autoSuggest',
        'gjj': 'http://172.29.2.174:8080/InnerEval/api/gjj/info',
        'insurance': 'http://172.29.2.174:8080/InnerEval/api/insurance/list',
        'phone_status': 'http://172.29.2.174:8080/InnerEval/api/nifa/queryInEnter',
        'naturalperson': 'http://172.29.2.174:8080/InnerEval/api/correlationcheck/blacklist/naturalperson',

    },
    'sit07': {
        'upload_report': 'http://172.30.3.41:8080/InnerEval/api/pbcc/report/fileUpload',
        'inquiry_credit': 'http://172.30.3.41:8080/InnerEval/api/pbcc/report/apply',
        'inquiry_result': 'http://172.30.3.41:8080/InnerEval/api/credit/result/list',
        'admission':        'http://172.30.3.41:8080/InnerEval/api/apply/isAdmission',
        'qcc_company': 'http://172.30.3.41:8080/InnerEval/api/company/autoSuggest',
        'soins': 'http://172.30.3.41:8080/InnerEval/api/company/autoSuggest',
        'gjj': 'http://172.30.3.41:8080/InnerEval/api/gjj/info',
        'insurance': 'http://172.30.3.41:8080/InnerEval/api/insurance/list',
        'phone_status': 'http://172.30.3.41:8080/InnerEval/api/nifa/queryInEnter',
        'naturalperson': 'http://172.30.3.41:8080/InnerEval/api/correlationcheck/blacklist/naturalperson',
    },
    'sit08': {
        'upload_report': 'http://172.29.2.152:8080/InnerEval/api/pbcc/report/fileUpload',
        'inquiry_credit': 'http://172.29.2.152:8080/InnerEval/api/pbcc/report/apply',
        'inquiry_result': 'http://172.29.2.152:8080/InnerEval/api/credit/result/list',
        'admission':        'http://172.29.2.152:8080/InnerEval/api/apply/isAdmission',
        'qcc_company': 'http://172.29.2.152:8080/InnerEval/api/company/autoSuggest',
        'soins': 'http://172.29.2.152:8080/InnerEval/api/company/autoSuggest',
        'gjj': 'http://172.29.2.152:8080/InnerEval/api/gjj/info',
        'insurance': 'http://172.29.2.152:8080/InnerEval/api/insurance/list',
        'phone_status': 'http://172.29.2.152:8080/InnerEval/api/nifa/queryInEnter',
        'naturalperson': 'http://172.29.2.152:8080/InnerEval/api/correlationcheck/blacklist/naturalperson',
    },
}
#准入
inner_admission_default_url = inner_urls[env_name]['admission']

#查询征信
inner_inquiryCredit_default_url = inner_urls[env_name]['inquiry_credit']

#获取征信结果
inner_fetchResult_default_url = inner_urls[env_name]['inquiry_result']

#自然人检测
inner_naturalperson_default_url = inner_urls[env_name]['naturalperson']

#企查查
inner_qcc_default_url = inner_urls[env_name]['qcc_company']

#公积金
inner_gjj_default_url = inner_urls[env_name]['gjj']

#社保
inner_soins_default_url = inner_urls[env_name]['soins']

#保单
inner_insurance_default_url = inner_urls[env_name]['insurance']

#手机在网状态
inner_phone_status_default_inner = inner_urls[env_name]['phone_status']




'''    官网接口配置信息    '''

hp_urls ={
    'sit01': {
        'register': 'https://testweb3005.yylending.com',
        'real_auth': 'https://testweb3005.yylending.com/server?from=api&model=user&action=verifyUser',
    },
    'sit02': {
        'register': 'https://testweb3013.yylending.com',
        'real_auth': 'https://testweb3013.yylending.com/server?from=api&model=user&action=verifyUser',
    },
    'sit03': {
        'register': 'https://testweb3016.yylending.com',
        'real_auth': 'https://testweb3016.yylending.com/server?from=api&model=user&action=verifyUser',
    },
    'sit04': {
        'register': 'https://testweb2045.yylending.com',
        'real_auth': 'https://testweb2045.yylending.com/server?from=api&model=user&action=verifyUser',

    },
    'sit05': {
        'register': 'https://testweb3038.yylending.com',
        'real_auth': 'https://testweb3038.yylending.com/server?from=api&model=user&action=verifyUser',
    },
    'sit06': {
        'register': 'https://testweb20179.yylending.com',
        'real_auth': 'https://testweb20179.yylending.com/server?from=api&model=user&action=verifyUser',
    },
    'sit07': {
        'register': 'https://testweb30179.yylending.com',
        'real_auth': 'https://testweb30179.yylending.com/server?from=api&model=user&action=verifyUser',
    },
    'sit08': {
        'register': 'https://testweb20160.yylending.com',
        'real_auth': 'https://testweb20160.yylending.com/server?from=api&model=user&action=verifyUser',
    },
    'uat':{
        'register': 'https://testweb3058.yylending.com',
        'real_auth': 'https://testweb3058.yylending.com/server?from=api&model=user&action=verifyUser',
    }
}

#注册
hp_register_default_url = hp_urls[env_name]['register']

#实名认证
hp_real_auth_default_url = hp_urls[env_name]['real_auth']

'''    悟空接口配置信息    '''
wk_urls = {
    'sit01':{
        'login': 'http://172.30.0.9/api/user/login',
        'submit':'http://172.30.0.9/api/wpt/apply/submit',
        'detail': 'http://172.30.0.9/api/apply/get_detail',
        'schedule':'http://172.30.0.9/api/wpt/schedule/list',
        'signal':'http://172.30.0.9/api/apply/signal',
        'cancel': 'http://172.30.0.9/api/wpt/apply/cancel',
        'task_adjust':'http://172.30.0.9/api/wpt/task/adjust',
        'approval_task_adjust':'http://172.30.0.9/api/approval/adjustTask',
        'get_apply_id':'http://172.30.0.9/api/wpt/apply/get_apply_id',
        'image_export': 'http://172.30.0.9/api/wpt/image_export/list',
        'pass_apply': 'http://172.30.0.9/api/core/general/get_pass_apply_list',
        'get_send_info': 'http://172.30.0.9/api/fatp/get_info/get_send_info'
    },
    'sit02':{
        'login':'http://172.30.0.17/api/user/login',
        'submit':'http://172.30.0.17/api/wpt/apply/submit',
        'schedule': 'http://172.30.0.17/api/wpt/schedule/list',
        'detail': 'http://172.30.0.17/api/apply/get_detail',
        'signal':'http://172.30.0.17/api/apply/signal',
        'cancel': 'http://172.30.0.17/api/wpt/apply/cancel',
        'task_adjust':'http://172.30.0.17/api/wpt/task/adjust',
        'approval_task_adjust':'http://172.30.0.17/api/approval/adjustTask',
        'get_apply_id':'http://172.30.0.17/api/wpt/apply/get_apply_id',
        'image_export':'http://172.30.0.17/api/wpt/image_export/list',
        'pass_apply':'http://172.30.0.17/api/core/general/get_pass_apply_list',
        'get_send_info':'http://172.30.0.17/api/fatp/get_info/get_send_info'


    },
    'sit03':{
        'login': 'http://172.30.0.18/api/user/login',
        'submit':'http://172.30.0.18/api/wpt/apply/submit',
        'detail': 'http://172.30.0.18/api/apply/get_detail',
        'schedule': 'http://172.30.0.18/api/wpt/schedule/list',
        'signal': 'http://172.30.0.18/api/apply/signal',
        'cancel': 'http://172.30.0.18/api/wpt/apply/cancel',
        'task_adjust': 'http://172.30.0.18/api/wpt/task/adjust',
        'approval_task_adjust': 'http://172.30.0.18/api/approval/adjustTask',
        'get_apply_id':'http://172.30.0.18/api/wpt/apply/get_apply_id',
        'image_export': 'http://172.30.0.18/api/wpt/image_export/list',
        'pass_apply': 'http://172.30.0.18/api/core/general/get_pass_apply_list',
        'get_send_info': 'http://172.30.0.18/api/fatp/get_info/get_send_info'


    },
    'sit04':{
        'login': 'http://172.29.1.22/api/user/login',
        'submit':'http://172.29.1.22/api/wpt/apply/submit',
        'detail': 'http://172.29.1.22/api/apply/get_detail',
        'schedule': 'http://172.29.1.22/api/wpt/schedule/list',
        'signal': 'http://172.29.1.22/api/apply/signal',
        'cancel': 'http://172.29.1.22/api/wpt/apply/cancel',
        'task_adjust': 'http://172.29.1.22/api/wpt/task/adjust',
        'approval_task_adjust': 'http://172.29.1.22/api/approval/adjustTask',
        'get_apply_id':'http://172.29.1.22/api/wpt/apply/get_apply_id',
        'image_export': 'http://172.29.1.22/api/wpt/apply/get_apply_id',
        'pass_apply': 'http://172.29.1.22/api/wpt/apply/get_apply_id',
        'get_send_info': 'http://172.29.1.22/api/fatp/get_info/get_send_info'

    },
    'sit05':{
        'login': 'http://172.30.3.216/api/user/login',
        'submit':'http://172.30.3.216/api/wpt/apply/submit',
        'detail': 'http://172.30.3.216/api/apply/get_detail',
        'schedule': 'http://172.30.3.216/api/wpt/schedule/list',
        'signal': 'http://172.30.3.216/api/apply/signal',
        'cancel': 'http://172.30.3.216/api/wpt/apply/cancel',
        'task_adjust': 'http://172.30.3.216/api/wpt/task/adjust',
        'approval_task_adjust': 'http://172.30.3.216/api/approval/adjustTask',
        'get_apply_id': 'http://172.30.3.216/api/wpt/apply/get_apply_id',
        'image_export': 'http://172.30.3.216/api/wpt/apply/get_apply_id',
        'pass_apply': 'http://172.30.3.216/api/wpt/apply/get_apply_id',
        'get_send_info': 'http://172.30.3.216/api/fatp/get_info/get_send_info'

    },
    'sit06': {
        'login': 'http://172.29.1.156/api/user/login',
        'submit':'http://172.29.1.156/api/wpt/apply/submit',
        'detail': 'http://172.29.1.156/api/apply/get_detail',
        'schedule': 'http://172.29.1.156/api/wpt/schedule/list',
        'signal': 'http://172.29.1.156/api/apply/signal',
        'cancel': 'http://172.29.1.156/api/wpt/apply/cancel',
        'task_adjust': 'http://172.29.1.156/api/wpt/task/adjust',
        'approval_task_adjust': 'http://172.29.1.156/api/approval/adjustTask',
        'get_apply_id': 'http://172.29.1.156/api/wpt/apply/get_apply_id',
        'image_export': 'http://172.29.1.156/api/wpt/apply/get_apply_id',
        'pass_apply': 'http://172.29.1.156/api/wpt/apply/get_apply_id',
        'get_send_info': 'http://172.29.1.156/api/fatp/get_info/get_send_info'

    },
    'sit07': {
        'login': 'http://172.30.3.217/api/user/login',
        'submit':'http://172.30.3.217/api/wpt/apply/submit',
        'detail': 'http://172.30.3.217/api/apply/get_detail',
        'schedule': 'http://172.30.3.217/api/wpt/schedule/list',
        'signal': 'http://172.30.3.217/api/apply/signal',
        'cancel': 'http://172.30.3.217/api/wpt/apply/cancel',
        'task_adjust': 'http://172.30.3.217/api/wpt/task/adjust',
        'approval_task_adjust': 'http://172.30.3.217/api/approval/adjustTask',
        'get_apply_id': 'http://172.30.3.217/api/wpt/apply/get_apply_id',
        'image_export': 'http://172.30.3.217/api/wpt/apply/get_apply_id',
        'pass_apply': 'http://172.30.3.217/api/wpt/apply/get_apply_id',
        'get_send_info': 'http://172.30.3.217/api/fatp/get_info/get_send_info'
    },
    'sit08': {
        'login': 'http://172.30.3.218/api/user/login',
        'submit':'http://172.30.3.218/api/wpt/apply/submit',
        'detail': 'http://172.30.3.218/api/apply/get_detail',
        'schedule': 'http://172.30.3.218/api/wpt/schedule/list',
        'signal': 'http://172.30.3.218/api/apply/signal',
        'cancel': 'http://172.30.3.218/api/wpt/apply/cancel',
        'task_adjust': 'http://172.30.3.218/api/wpt/task/adjust',
        'approval_task_adjust': 'http://172.30.3.218/api/approval/adjustTask',
        'get_apply_id': 'http://172.30.3.218/api/wpt/apply/get_apply_id',
        'image_export': 'http://172.30.3.218/api/wpt/apply/get_apply_id',
        'pass_apply': 'http://172.30.3.218/api/wpt/apply/get_apply_id',
        'get_send_info': 'http://172.30.3.218/api/fatp/get_info/get_send_info'
    },
    'uat':{
        'login': 'http://172.30.3.219/api/user/login',
        'submit':'http://172.30.3.219/api/wpt/apply/submit',
        'detail': 'http://172.30.3.219/api/apply/get_detail',
        'schedule': 'http://172.30.3.219/api/wpt/schedule/list',
        'signal': 'http://172.30.3.219/api/apply/signal',
        'cancel': 'http://172.30.3.219/api/wpt/apply/cancel',
        'task_adjust': 'http://172.30.3.219/api/wpt/task/adjust',
        'approval_task_adjust': 'http://172.30.3.219/api/approval/adjustTask',
        'get_apply_id': 'http://172.30.3.219/api/wpt/apply/get_apply_id',
        'image_export': 'http://172.30.3.219/api/wpt/apply/get_apply_id',
        'pass_apply': 'http://172.30.3.219/api/wpt/apply/get_apply_id',
        'get_send_info': 'http://172.30.3.219/api/fatp/get_info/get_send_info'
    }
}
#'''登录'''
wk_login_default_url = wk_urls[env_name]['login']

#'''申请详情'''
wk_detail_default_url = wk_urls[env_name]['detail']

#'''改变流程状态'''
wk_signal_default_url = wk_urls[env_name]['signal']

#'''取消任务 用于面签'''
wk_cancel_default_url = wk_urls[env_name]['cancel']

#'''提交申请'''
wk_submit_default_url = wk_urls[env_name]['submit']

#'''进度查询'''
wk_schedule_default_url = wk_urls[env_name]['schedule']

#'''任务调整 作业平台调用 用户展业'''
wk_task_adjust_default_url = wk_urls[env_name]['task_adjust']

#'''任务调整 悟空系统內评审批调用'''
wk_approval_task_adjust_default_url = wk_urls[env_name]['task_adjust']

#获取空白apply_id
wk_get_apply_id_default_url = wk_urls[env_name]['get_apply_id']

#获取审批通过的apply
wk_pass_apply_default_url = wk_urls[env_name]['pass_apply']

#影像导出
wk_image_export_default_url = wk_urls[env_name]['image_export']

#批量获取发标信息
wk_send_info_default_url = wk_urls[env_name]['get_send_info']


''' 资金调度平台接口配置信息  '''
fatp_urls = {
    'sit01': {
        'organization_repair': 'https://testfatpsit01.yylending.com/fatp-lm-service/http/lm/foreign/callback/notify/getSupplementData',
        'notify': 'https://testfatpsit01.yylending.com/fatp-lm-service/http/lm/foreign/callback/defer/notify',

    },
    'sit02': {
        'organization_repair': 'https://testfatpsit02.yylending.com/fatp-lm-service/http/lm/foreign/callback/notify/getSupplementData',
        'notify':'https://testfatpsit02.yylending.com/fatp-lm-service/http/lm/foreign/callback/defer/notify',

    },
    'sit03': {
        'organization_repair': 'https://testfatpsit03.yylending.com/fatp-lm-service/http/lm/foreign/callback/notify/getSupplementData',
        'notify': 'https://testfatpsit03.yylending.com/fatp-lm-service/http/lm/foreign/callback/defer/notify',


    },
    'sit04': {
        'organization_repair': 'https://testfatpsit04.yylending.com/fatp-lm-service/http/lm/foreign/callback/notify/getSupplementData',
        'notify': 'https://testfatpsit04.yylending.com/fatp-lm-service/http/lm/foreign/callback/defer/notify',
    },
    'sit05': {
        'organization_repair': 'https://testfatpsit05.yylending.com/fatp-lm-service/http/lm/foreign/callback/notify/getSupplementData',
        'notify': 'https://testfatpsit05.yylending.com/fatp-lm-service/http/lm/foreign/callback/defer/notify',

    },
    'sit06': {
        'organization_repair': 'https://testfatpsit06.yylending.com/fatp-lm-service/http/lm/foreign/callback/notify/getSupplementData',
        'notify': 'https://testfatpsit06.yylending.com/fatp-lm-service/http/lm/foreign/callback/defer/notify',
    },
    'sit07': {
        'organization_repair': 'https://testfatpsit07.yylending.com/fatp-lm-service/http/lm/foreign/callback/notify/getSupplementData',
        'notify': 'https://testfatpsit07.yylending.com/fatp-lm-service/http/lm/foreign/callback/defer/notify',
    },
    'sit08': {
        'organization_repair': 'https://testfatpsit08.yylending.com/fatp-lm-service/http/lm/foreign/callback/notify/getSupplementData',
        'notify': 'https://testfatpsit08.yylending.com/fatp-lm-service/http/lm/foreign/callback/defer/notify',
    },
    'uat':{
        'organization_repair':'https://testfatpuat.yylending.com/fatp-lm-service/http/lm/foreign/callback/notify/getSupplementData',
        'notify': 'https://testfatpuat.yylending.com/fatp-lm-service/http/lm/foreign/callback/defer/notify',

    }
}

#''' 机构补件'''
fatp_organization_repair_default_url = fatp_urls[env_name]['organization_repair']

#通知资金平台未暂时(0);已暂缓(1) ;已终止(2)
fatp_notify_default_url =  fatp_urls[env_name]['notify']

''' 电销系统接口配置信息  '''
lcrm_urls = {
    'sit01': {
        'telemarketing': 'https://testlcrmsit01.yylending.com/lcrm-tmk-service/http/telemarketing/foreign/query/getElectricPinQuiryReqForWpt',
        'XD_type':         'https://testlcrmsit01.yylending.com:443/lcrm-tmk-service/http/lcrm/tmk/foreign/queryXDCustomerType',
        'is_lock':             'https://testlcrmsit01.yylending.com:443/lcrm-tmk-service/http/lcrm/tmk/foreign/getLockFlagByQDCertId',

    },
    'sit02': {
        'telemarketing': 'https://testlcrmsit02.yylending.com/lcrm-tmk-service/http/telemarketing/foreign/query/getElectricPinQuiryReqForWpt',
        'XD_type':'https://testlcrmsit02.yylending.com:443/lcrm-tmk-service/http/lcrm/tmk/foreign/queryXDCustomerType',
        'is_lock':'https://testlcrmsit02.yylending.com:443/lcrm-tmk-service/http/lcrm/tmk/foreign/getLockFlagByQDCertId',

    },
    'sit03': {
        'telemarketing': 'https://testlcrmsit03.yylending.com/lcrm-tmk-service/http/telemarketing/foreign/query/getElectricPinQuiryReqForWpt',
        'XD_type':         'https://testlcrmsit03.yylending.com:443/lcrm-tmk-service/http/lcrm/tmk/foreign/queryXDCustomerType',
        'is_lock':             'https://testlcrmsit03.yylending.com:443/lcrm-tmk-service/http/lcrm/tmk/foreign/getLockFlagByQDCertId',
    },
    'sit04': {
        'telemarketing': 'https://testlcrmsit04.yylending.com/lcrm-tmk-service/http/telemarketing/foreign/query/getElectricPinQuiryReqForWpt',
        'XD_type':         'https://testlcrmsit04.yylending.com:443/lcrm-tmk-service/http/lcrm/tmk/foreign/queryXDCustomerType',
        'is_lock':              'https://testlcrmsit04.yylending.com:443/lcrm-tmk-service/http/lcrm/tmk/foreign/getLockFlagByQDCertId',
    },
    'sit05': {
        'telemarketing': 'https://testlcrmsit05.yylending.com/lcrm-tmk-service/http/telemarketing/foreign/query/getElectricPinQuiryReqForWpt',
        'XD_type':         'https://testlcrmsit05.yylending.com:443/lcrm-tmk-service/http/lcrm/tmk/foreign/queryXDCustomerType',
        'is_lock':             'https://testlcrmsit05.yylending.com:443/lcrm-tmk-service/http/lcrm/tmk/foreign/getLockFlagByQDCertId',

    },
    'sit06': {
        'telemarketing': 'https://testlcrmsit06.yylending.com/lcrm-tmk-service/http/telemarketing/foreign/query/getElectricPinQuiryReqForWpt',
        'XD_type':        'https://testlcrmsit06.yylending.com:443/lcrm-tmk-service/http/lcrm/tmk/foreign/queryXDCustomerType',
        'is_lock':             'https://testlcrmsit06.yylending.com:443/lcrm-tmk-service/http/lcrm/tmk/foreign/getLockFlagByQDCertId',
    },
    'sit07': {
        'telemarketing': 'https://testlcrmsit07.yylending.com/lcrm-tmk-service/http/telemarketing/foreign/query/getElectricPinQuiryReqForWpt',
        'XD_type':        'https://testlcrmsit07.yylending.com:443/lcrm-tmk-service/http/lcrm/tmk/foreign/queryXDCustomerType',
        'is_lock':             'https://testlcrmsit07.yylending.com:443/lcrm-tmk-service/http/lcrm/tmk/foreign/getLockFlagByQDCertId',
    },
    'sit08': {
        'telemarketing': 'https://testlcrmsit08.yylending.com/lcrm-tmk-service/http/telemarketing/foreign/query/getElectricPinQuiryReqForWpt',
        'XD_type':        'https://testlcrmsit08.yylending.com:443/lcrm-tmk-service/http/lcrm/tmk/foreign/queryXDCustomerType',
        'is_lock':            'https://testlcrmsit08.yylending.com:443/lcrm-tmk-service/http/lcrm/tmk/foreign/getLockFlagByQDCertId',
    },
    'uat':{
        'telemarketing':'https://testlcrmuat.yylending.com/lcrm-tmk-service/http/telemarketing/foreign/query/getElectricPinQuiryReqForWpt',
        'XD_type':        'https://testlcrmuat.yylending.com/lcrm-tmk-service/http/lcrm/tmk/foreign/queryXDCustomerType',
        'is_lock':            'https://testlcrmuat.yylending.com/lcrm-tmk-service/http/lcrm/tmk/foreign/getLockFlagByQDCertId',
    }
}

#''' 电销查询'''
lcrm_telemarketing_default_url = lcrm_urls[env_name]['telemarketing']

#识别客户续贷类型
lcrm_XD_type_default_url = lcrm_urls[env_name]['XD_type']

#判断是否锁定
lcrm_is_lock_default_url = lcrm_urls[env_name]['is_lock']




''' 业务管理系统接口配置信息  '''
bms_urls = {
    'sit01': {
        'current_finish_signature': 'https://testbmssit01.yylending.com/bms-app-service/http/fs/deal/foreign/list',
        'video_tasks':'https://testbmssit01.yylending.com/bms-app-service/http/fs/deal/foreign/list',
        'seller_list':'https://testbmssit01.yylending.com:443/bms-sc-service/http/seller/foreign/list',
        'bind_relation': 'https://testbmssit01.yylending.com:443/bms-sm-service/http/recommender/foreign/getBindInfo',
        'channel_info':'https://testbmssit01.yylending.com:443/bms-sm-service/http/channel/foreign/listChannelManagerInfo',
        'get_seller': 'https://testbmssit01.yylending.com:443/bms-sc-service/http/seller/foreign/getSellerForApply',
        'auto_show_seller': 'https://testbmssit01.yylending.com:443/bms-sc-service/http/seller/foreign/info',
        'get_org_list': 'https://testbmssit01.yylending.com/plms-um-service/http/orginfo/foreign/getList',


    },
    'sit02': {
        'current_finish_signature': 'https://testbmssit02.yylending.com/bms-app-service/http/fs/deal/foreign/list',
        'video_tasks':'https://testbmssit02.yylending.com/bms-app-service/http/fs/deal/foreign/list',
        'seller_list':'https://testbmssit02.yylending.com:443/bms-sc-service/http/seller/foreign/list',
        'bind_relation':'https://testbmssit02.yylending.com:443/bms-sm-service/http/recommender/foreign/getBindInfo',
        'channel_info':'https://testbmssit02.yylending.com:443/bms-sm-service/http/channel/foreign/listChannelManagerInfo',
        'get_seller':'https://testbmssit02.yylending.com:443/bms-sc-service/http/seller/foreign/getSellerForApply',
        'auto_show_seller':'https://testbmssit02.yylending.com:443/bms-sc-service/http/seller/foreign/info',
        'get_org_list': 'https://testbmssit02.yylending.com/plms-um-service/http/orginfo/foreign/getList',

    },
    'sit03': {
        'current_finish_signature': 'https://testbmssit03.yylending.com/bms-app-service/http/fs/deal/foreign/list',
        'video_tasks':'https://testbmssit03.yylending.com/bms-app-service/http/fs/deal/foreign/list',
        'seller_list':'https://testbmssit03.yylending.com:443/bms-sc-service/http/seller/foreign/list',
        'bind_relation': 'https://testbmssit03.yylending.com:443/bms-sm-service/http/recommender/foreign/getBindInfo',
        'channel_info':'https://testbmssit03.yylending.com:443/bms-sm-service/http/channel/foreign/listChannelManagerInfo',
        'get_seller': 'https://testbmssit03.yylending.com:443/bms-sc-service/http/seller/foreign/getSellerForApply',
        'auto_show_seller': 'https://testbmssit03.yylending.com:443/bms-sc-service/http/seller/foreign/info',
        'get_org_list': 'https://testbmssit03.yylending.com/plms-um-service/http/orginfo/foreign/getList',

    },
    'sit04': {
        'current_finish_signature': 'https://testbmssit04.yylending.com/bms-app-service/http/fs/deal/foreign/list',
        'video_tasks':'https://testbmssit04.yylending.com/bms-app-service/http/fs/deal/foreign/list',
        'seller_list':'https://testbmssit04.yylending.com:443/bms-sc-service/http/seller/foreign/list',
        'bind_relation': 'https://testbmssit04.yylending.com:443/bms-sm-service/http/recommender/foreign/getBindInfo',
        'channel_info':'https://testbmssit04.yylending.com:443/bms-sm-service/http/channel/foreign/listChannelManagerInfo',
        'get_seller': 'https://testbmssit04.yylending.com:443/bms-sc-service/http/seller/foreign/getSellerForApply',
        'auto_show_seller': 'https://testbmssit04.yylending.com:443/bms-sc-service/http/seller/foreign/info',
        'get_org_list': 'https://testbmssit04.yylending.com/plms-um-service/http/orginfo/foreign/getList',
    },
    'sit05': {
        'current_finish_signature': 'https://testbmssit05.yylending.com/bms-app-service/http/fs/deal/foreign/list',
        'video_tasks':'https://testbmssit05.yylending.com/bms-app-service/http/fs/deal/foreign/list',
        'seller_list':'https://testbmssit05.yylending.com:443/bms-sc-service/http/seller/foreign/list',
        'bind_relation': 'https://testbmssit05.yylending.com:443/bms-sm-service/http/recommender/foreign/getBindInfo',
        'channel_info':'https://testbmssit05.yylending.com:443/bms-sm-service/http/channel/foreign/listChannelManagerInfo',
        'get_seller':'https://testbmssit05.yylending.com:443/bms-sc-service/http/seller/foreign/getSellerForApply',
        'auto_show_seller':'https://testbmssit05.yylending.com:443/bms-sc-service/http/seller/foreign/info',
        'get_org_list': 'https://testbmssit05.yylending.com/plms-um-service/http/orginfo/foreign/getList',

    },
    'sit06': {
        'current_finish_signature': 'https://testbmssit06.yylending.com/bms-app-service/http/fs/deal/foreign/list',
        'video_tasks':'https://testbmssit06.yylending.com/bms-app-service/http/fs/deal/foreign/list',
        'seller_list':'https://testbmssit06.yylending.com:443/bms-sc-service/http/seller/foreign/list',
        'bind_relation': 'https://testbmssit06.yylending.com:443/bms-sm-service/http/recommender/foreign/getBindInfo',
        'channel_info':'https://testbmssit06.yylending.com:443/bms-sm-service/http/channel/foreign/listChannelManagerInfo',
        'get_seller': 'https://testbmssit06.yylending.com:443/bms-sc-service/http/seller/foreign/getSellerForApply',
        'auto_show_seller': 'https://testbmssit06.yylending.com:443/bms-sc-service/http/seller/foreign/info',
        'get_org_list': 'https://testbmssit06.yylending.com/plms-um-service/http/orginfo/foreign/getList',
    },
    'sit07': {
        'current_finish_signature': 'https://testbmssit07.yylending.com/bms-app-service/http/fs/deal/foreign/list',
        'video_tasks':'https://testbmssit07.yylending.com/bms-app-service/http/fs/deal/foreign/list',
        'seller_list':'https://testbmssit07.yylending.com:443/bms-sc-service/http/seller/foreign/list',
        'bind_relation': 'https://testbmssit07.yylending.com:443/bms-sm-service/http/recommender/foreign/getBindInfo',
        'channel_info':'https://testbmssit07.yylending.com:443/bms-sm-service/http/channel/foreign/listChannelManagerInfo',
        'get_seller': 'https://testbmssit07.yylending.com:443/bms-sc-service/http/seller/foreign/getSellerForApply',
        'auto_show_seller': 'https://testbmssit07.yylending.com:443/bms-sc-service/http/seller/foreign/info',
        'get_org_list': 'https://testbmssit07.yylending.com/plms-um-service/http/orginfo/foreign/getList',
    },
    'sit08': {
        'current_finish_signature': 'https://testbmssit08.yylending.com/bms-app-service/http/fs/deal/foreign/list',
        'video_tasks':'https://testbmssit08.yylending.com/bms-app-service/http/fs/deal/foreign/list',
        'seller_list':'https://testbmssit08.yylending.com:443/bms-sc-service/http/seller/foreign/list',
        'bind_relation': 'https://testbmssit08.yylending.com:443/bms-sm-service/http/recommender/foreign/getBindInfo',
        'channel_info':'https://testbmssit08.yylending.com:443/bms-sm-service/http/channel/foreign/listChannelManagerInfo',
        'get_seller': 'https://testbmssit08.yylending.com:443/bms-sc-service/http/seller/foreign/getSellerForApply',
        'auto_show_seller': 'https://testbmssit08.yylending.com:443/bms-sc-service/http/seller/foreign/info',
        'get_org_list': 'https://testbmssit08.yylending.com/plms-um-service/http/orginfo/foreign/getList',

    },
    'uat':{
        'current_finish_signature':'https://testbmsuat.yylending.com/bms-app-service/http/fs/deal/foreign/list',
        'video_tasks':'https://testbmsuat.yylending.com/bms-app-service/http/fs/deal/foreign/list',
        'seller_list':'https://testbmsuat.yylending.com/bms-sc-service/http/seller/foreign/list',
        'bind_relation': 'https://testbmsuat.yylending.com/bms-sm-service/http/recommender/foreign/getBindInfo',
        'channel_info':'https://testbmsuat.yylending.com/bms-sm-service/http/channel/foreign/listChannelManagerInfo',
        'get_seller': 'https://testbmsuat.yylending.com:443/bms-sc-service/http/seller/foreign/getSellerForApply',
        'auto_show_seller': 'https://testbmsuat.yylending.com:443/bms-sc-service/http/seller/foreign/info',
        'get_org_list': 'https://testbmsuat.yylending.com/plms-um-service/http/orginfo/foreign/getList',
    }
}

#''' 当前/已完成面签列表 '''
bms_signature_default_url = bms_urls[env_name]['current_finish_signature']

#''' 视频任务列表 '''
bms_video_default_url = bms_urls[env_name]['video_tasks']

#批量查询营销人员信息
bms_seller_list_default_url = bms_urls[env_name]['seller_list']

#查询绑定关系
bms_bind_relation_default_url = bms_urls[env_name]['bind_relation']

#查询合作渠道信息
bms_channel_info_default_url =  bms_urls[env_name]['channel_info']

#查询客户经理信息
bms_get_seller_default_url = bms_urls['sit02']['get_seller']

#营销渠道选择代账渠道自动带出合作渠道绑定的客户经理
bms_auto_show_seller_default_url = bms_urls[env_name]['auto_show_seller']

#获取结构列表
bms_org_list_default_list = bms_urls[env_name]['get_org_list']


''' PLMS 贷后系统接口配置  '''
plms_urls ={
    'sit01': {
        'login': 'https://testplmssit01.yylending.com/plms-um-service/http/user/login',
        'logout': 'https://testplmssit01.yylending.com/plms-um-service/http/user/logout',
    },
    'sit02': {
        'login': 'https://testplmssit02.yylending.com/plms-um-service/http/user/login',
        'logout': 'https://testplmssit02.yylending.com/plms-um-service/http/user/logout',
    },
    'sit03': {
        'login': 'https://testplmssit03.yylending.com/plms-um-service/http/user/login',
        'logout': 'https://testplmssit03.yylending.com/plms-um-service/http/user/logout',
    },
    'sit04': {
        'login': 'https://testplmssit04.yylending.com/plms-um-service/http/user/login',
        'logout': 'https://testplmssit04.yylending.com/plms-um-service/http/user/logout',

    },
    'sit05': {
        'login': 'https://testplmssit05.yylending.com/plms-um-service/http/user/login',
        'logout': 'https://testplmssit05.yylending.com/plms-um-service/http/user/logout',
    },
    'sit06': {
        'login': 'https://testplmssit06.yylending.com/plms-um-service/http/user/login',
        'logout': 'https://testplmssit06.yylending.com/plms-um-service/http/user/logout',
    },
    'sit07': {
        'login': 'https://testplmssit07.yylending.com/plms-um-service/http/user/login',
        'logout': 'https://testplmssit07.yylending.com/plms-um-service/http/user/logout',
    },
    'sit08': {
        'login': 'https://testplmssit08.yylending.com/plms-um-service/http/user/login',
        'logout': 'https://testplmssit08.yylending.com/plms-um-service/http/user/logout',
    },
    'uat':{
        'login': 'https://testplmsuat.yylending.com/plms-um-service/http/user/login',
        'logout': 'https://testplmssuat.yylending.com/plms-um-service/http/user/logout',
    }
}

#登录
plms_login_default_url = plms_urls[env_name]['login']

#退出
plms_logout_default_url = plms_urls[env_name]['logout']


''' CMA系统接口配置  '''
cma_pwd = {
    'key':'0e80ab1f7c824152',
    'iv':'0102030405060708'
}
cme_key = cma_pwd['key']
cma_iv = cma_pwd['iv']

cma_urls ={
    'sit01': {
        'valid_recommend': 'https://testcmasit01.yylending.com/cma/entry/partner/queryChannelTypeByCertId',
    },
    'sit02': {
        'valid_recommend': 'https://testcmasit102.yylending.com:443/cma/entry/partner/queryChannelTypeByCertId',
    },
    'sit03': {
        'valid_recommend': 'https://testcmasit03.yylending.com/cma/entry/partner/queryChannelTypeByCertId',
    },
    'sit04': {
        'valid_recommend': 'https://testcmasit04.yylending.com/cma/entry/partner/queryChannelTypeByCertId',
    },
    'sit05': {
        'valid_recommend': 'https://testcmasit05.yylending.com/cma/entry/partner/queryChannelTypeByCertId',
    },
    'sit06': {
        'organization_repair': 'https://testcmasit06.yylending.com/cma/entry/partner/queryChannelTypeByCertId',
    },
    'sit07': {
        'valid_recommend': 'https://testcmasit07.yylending.com/cma/entry/partner/queryChannelTypeByCertId',
    },
    'sit08': {
        'valid_recommend': 'https://testcmasit08.yylending.com/cma/entry/partner/queryChannelTypeByCertId',
    },
    'uat':{
        'valid_recommend':'https://testcmauat.yylending.com/cma/entry/partner/queryChannelTypeByCertId'
    }
}

#根据身份证查询有效推荐人信息
cma_valid_recommend_default_url = cma_urls[env_name]['valid_recommend']

''' OMS系统接口配置  '''
oms_urls ={
    'sit01': {
        'code_detail': 'https://testomssit01.yylending.com/oms-sc-service/http/codedetail/foreign/list',
        'get_workdays': 'https://testomssit01.yylending.com/oms-hm-service/http/holiday/foreign/getWorkdays',
    },
    'sit02': {
        'code_detail': 'https://testomssit02.yylending.com/oms-sc-service/http/codedetail/foreign/list',
        'get_workdays': 'https://testomssit02.yylending.com/oms-hm-service/http/holiday/foreign/getWorkdays',
    },
    'sit03': {
        'code_detail': 'https://testomssit03.yylending.com/oms-sc-service/http/codedetail/foreign/list',
        'get_workdays': 'https://testomssit03.yylending.com/oms-hm-service/http/holiday/foreign/getWorkdays',
    },
    'sit04': {
        'code_detail': 'https://testomssit04.yylending.com/oms-sc-service/http/codedetail/foreign/list',
        'get_workdays': 'https://testomssit04.yylending.com/oms-hm-service/http/holiday/foreign/getWorkdays',
    },
    'sit05': {
        'code_detail': 'https://testomssit05.yylending.com/oms-sc-service/http/codedetail/foreign/list',
        'get_workdays': 'https://testomssit05.yylending.com/oms-hm-service/http/holiday/foreign/getWorkdays',
    },
    'sit06': {
        'code_detail': 'https://testomssit06.yylending.com/oms-sc-service/http/codedetail/foreign/list',
        'get_workdays': 'https://testomssit06.yylending.com/oms-hm-service/http/holiday/foreign/getWorkdays',
    },
    'sit07': {
        'code_detail': 'https://testomssit07.yylending.com/oms-sc-service/http/codedetail/foreign/list',
        'get_workdays': 'https://testomssit07.yylending.com/oms-hm-service/http/holiday/foreign/getWorkdays',
    },
    'sit08': {
        'code_detail': 'https://testomssit08.yylending.com/oms-sc-service/http/codedetail/foreign/list',
        'get_workdays': 'https://testomssit08.yylending.com/oms-hm-service/http/holiday/foreign/getWorkdays',
    },
    'uat':{
        'code_detail': 'https://testomsuat.yylending.com/oms-sc-service/http/codedetail/foreign/list',
        'get_workdays':'https://testomsuat.yylending.com/oms-hm-service/http/holiday/foreign/getWorkdays'
    }
}

#获取工作日
oms_workdays_default_url = oms_urls[env_name]['get_workdays']

#获取枚举值
oms_code_detail_default_url = oms_urls[env_name]['code_detail']



''' 影像系统接口配置信息  '''
image_urls = {
    'sit01':{
        'upload_image':'https://testplmssit01image.yylending.com/Image/service/imageUpload',
        'get_image':'https://testplmssit01image.yylending.com/api/apply/getImageList' },
    }
image_default_url = image_urls['sit01']['upload_image']
get_image_default_url = image_urls['sit01']['get_image']



#数据库环境配置信息
wk_mysql_conn = {
    'sit01':{
        "host": '172.29.2.144',
        "port": 3501,
        "user": 'wkapp',
        "passwd": 'WuGeiKaiFa123',
        "db": 'wkdb01',
        "charset": 'utf8'
    },
    'sit02':{
            "host": '172.29.2.144',
            "port": 3501,
            "user": 'wkapp',
            "passwd": 'WuGeiKaiFa123',
            "db": 'wkdb02',
            "charset": 'utf8'
        },
    'sit03':{
            "host": '172.29.2.144',
            "port": 3501,
            "user": 'wkapp',
            "passwd": 'WuGeiKaiFa123',
            "db": 'wkdb03',
            "charset": 'utf8'
        },
    'sit04':{
            "host": '172.29.2.144',
            "port": 3501,
            "user": 'wkapp',
            "passwd": 'WuGeiKaiFa123',
            "db": 'wkdb04',
            "charset": 'utf8'
        },
    'sit05':{
            "host": '172.29.2.144',
            "port": 3501,
            "user": 'wkapp',
            "passwd": 'WuGeiKaiFa123',
            "db": 'wkdb05',
            "charset": 'utf8'
        },
    'sit06':{
            "host": '172.29.2.144',
            "port": 3501,
            "user": 'wkapp',
            "passwd": 'WuGeiKaiFa123',
            "db": 'wkdb06',
            "charset": 'utf8'
        },
    'sit07':{
            "host": '172.29.2.144',
            "port": 3501,
            "user": 'wkapp',
            "passwd": 'WuGeiKaiFa123',
            "db": 'wkdb07',
            "charset": 'utf8'
        },
    'sit08':{
            "host": '172.29.2.144',
            "port": 3501,
            "user": 'wkapp',
            "passwd": 'WuGeiKaiFa123',
            "db": 'wkdb08',
            "charset": 'utf8'
        },
    'uat':{
            "host": '172.29.2.144',
            "port": 3509,
            "user": 'wkapp',
            "passwd": 'WuGeiKaiFa123',
            "db": 'wkdb01',
            "charset": 'utf8'
        },
}
wk_mysql_default_conn = wk_mysql_conn[env_name]


bms_mysql_conn = {
    'sit01':{
        "host": '172.29.2.143',
        "port": 3504,
        "user": 'bmsapp',
        "passwd": 'WuGeiKaiFa123',
        "db": 'bmsdb01',
        "charset": 'utf8'
    },
    'sit02':{
            "host": '172.29.2.143',
            "port": 3504,
            "user": 'bmsapp',
            "passwd": 'WuGeiKaiFa123',
            "db": 'bmsdb02',
            "charset": 'utf8'
        },
    'sit03':{
            "host": '172.29.2.143',
            "port": 3504,
            "user": 'bmsapp',
            "passwd": 'WuGeiKaiFa123',
            "db": 'bmsdb03',
            "charset": 'utf8'
        },
    'sit04':{
            "host": '172.29.2.143',
            "port": 3504,
            "user": 'bmsapp',
            "passwd": 'WuGeiKaiFa123',
            "db": 'bmsdb04',
            "charset": 'utf8'
        },
    'sit05':{
            "host": '172.29.2.143',
            "port": 3504,
            "user": 'bmsapp',
            "passwd": 'WuGeiKaiFa123',
            "db": 'bmsdb05',
            "charset": 'utf8'
        },
    'sit06':{
            "host": '172.29.2.143',
            "port": 3504,
            "user": 'bmsapp',
            "passwd": 'WuGeiKaiFa123',
            "db": 'bmsdb06',
            "charset": 'utf8'
        },
    'sit07':{
            "host": '172.29.2.143',
            "port": 3504,
            "user": 'bmsapp',
            "passwd": 'WuGeiKaiFa123',
            "db": 'bmsdb07',
            "charset": 'utf8'
        },
    'sit08':{
            "host": '172.29.2.143',
            "port": 3504,
            "user": 'bmsapp',
            "passwd": 'WuGeiKaiFa123',
            "db": 'bmsdb08',
            "charset": 'utf8'
        },
    'uat':{
            "host": '172.29.2.143',
            "port": 3504,
            "user": 'bmsapp',
            "passwd": 'WuGeiKaiFa123',
            "db": 'bmsdb09',
            "charset": 'utf8'
        },
}
bms_mysql_default_conn = bms_mysql_conn[env_name]

cma_mysql_conn = {
    'sit01':{
        "host": '172.29.2.143',
        "port": 3507,
        "user": 'cmaapp',
        "passwd": 'WuGeiKaiFa123',
        "db": 'cma01',
        "charset": 'utf8'
    },
    'sit02':{
        "host": '172.29.2.143',
        "port": 3507,
        "user": 'cmaapp',
        "passwd": 'WuGeiKaiFa123',
        "db": 'cma02',
        "charset": 'utf8'
    },
    'sit03':{
        "host": '172.29.2.143',
        "port": 3507,
        "user": 'cmaapp',
        "passwd": 'WuGeiKaiFa123',
        "db": 'cma03',
        "charset": 'utf8'
    },
    'sit04':{
        "host": '172.29.2.143',
        "port": 3507,
        "user": 'cmaapp',
        "passwd": 'WuGeiKaiFa123',
        "db": 'cma04',
        "charset": 'utf8'
    },
    'sit05':{
        "host": '172.29.2.143',
        "port": 3507,
        "user": 'cmaapp',
        "passwd": 'WuGeiKaiFa123',
        "db": 'cma05',
        "charset": 'utf8'
    },
    'sit06':{
        "host": '172.29.2.143',
        "port": 3507,
        "user": 'cmaapp',
        "passwd": 'WuGeiKaiFa123',
        "db": 'cma06',
        "charset": 'utf8'
    },
    'sit07':{
        "host": '172.29.2.143',
        "port": 3507,
        "user": 'cmaapp',
        "passwd": 'WuGeiKaiFa123',
        "db": 'cma07',
        "charset": 'utf8'
    },
    'sit08':{
        "host": '172.29.2.143',
        "port": 3507,
        "user": 'cmaapp',
        "passwd": 'WuGeiKaiFa123',
        "db": 'cma08',
        "charset": 'utf8'
    },
    'uat':{
        "host": '172.29.2.143',
        "port": 3507,
        "user": 'cmaapp',
        "passwd": 'WuGeiKaiFa123',
        "db": 'cma09',
        "charset": 'utf8'
    },
}
cma_mysql_default_conn = cma_mysql_conn[env_name]



wpt_mongo_conn = {
    'sit01': ['172.29.2.158', 27024],
    'sit02': ['172.29.2.158', 27025],
    'sit03': ['172.29.2.158', 27026],
    'sit04': ['172.29.2.7', 27018],
    'sit05': ['172.30.3.60', 27018],
    'sit06': ['172.29.2.180', 27017],
    'sit07': ['172.29.2.7', 27017],
    'sit08': ['172.29.2.162', 27018],
}
wpt_mongo_default_conn = wpt_mongo_conn[env_name]

fatp_mysql_conn = {
    'sit01':{
        "host": '172.29.2.143',
        "port": 3506,
        "user": 'fatpapp',
        "passwd": 'WuGeiKaiFa123',
        "db": 'fatpdb01',
        "charset": 'utf8'
    },
    'sit02':{
        "host": '172.29.2.143',
        "port": 3506,
        "user": 'fatpapp',
        "passwd": 'WuGeiKaiFa123',
        "db": 'fatpdb02',
        "charset": 'utf8'
    },
    'sit03':{
        "host": '172.29.2.143',
        "port": 3506,
        "user": 'fatpapp',
        "passwd": 'WuGeiKaiFa123',
        "db": 'fatpdb03',
        "charset": 'utf8'
    },
    'sit04':{
        "host": '172.29.2.143',
        "port": 3506,
        "user": 'fatpapp',
        "passwd": 'WuGeiKaiFa123',
        "db": 'fatpdb04',
        "charset": 'utf8'
    },
    'sit05':{
        "host": '172.29.2.143',
        "port": 3506,
        "user": 'fatpapp',
        "passwd": 'WuGeiKaiFa123',
        "db": 'fatpdb05',
        "charset": 'utf8'
    },
    'sit06':{
        "host": '172.29.2.143',
        "port": 3506,
        "user": 'fatpapp',
        "passwd": 'WuGeiKaiFa123',
        "db": 'fatpdb06',
        "charset": 'utf8'
    },
    'sit07':{
        "host": '172.29.2.143',
        "port": 3506,
        "user": 'fatpapp',
        "passwd": 'WuGeiKaiFa123',
        "db": 'fatpdb07',
        "charset": 'utf8'
    },
    'sit08':{
        "host": '172.29.2.143',
        "port": 3506,
        "user": 'fatpapp',
        "passwd": 'WuGeiKaiFa123',
        "db": 'fatpdb08',
        "charset": 'utf8'
    },
    'uat':{
        "host": '172.29.2.143',
        "port": 3506,
        "user": 'fatpapp',
        "passwd": 'WuGeiKaiFa123',
        "db": 'fatpdb09',
        "charset": 'utf8'
    },
}
fatp_mysql_default_conn = fatp_mysql_conn[env_name]



#业务类型
business_type = {
    'ZRB':['1100400','真融宝'],
    'SZS':['1100500','石嘴山'],
    'ZGC':['1100800','中关村'],
    'XGM':['1100900','西格玛'],
    'HXB':['1101300','华兴银行'],
    'NJB':['1101400','南京银行'],
    'XWB':['1101700','新网银行'],
    'MTB':['1101500','民泰银行'],
    'LFB':['1101600','廊坊银行'],
    'CDB':['1101200','承德银行'],
    'CCNS': ['1101800','长春农商'],
    'NBTS': ['1100700','宁波通商'],
    'ZLJR': ['1101900','招联金融'],
    'YYFAX': ['1100100','友金快贷'],
}

#营销渠道类型
sale_channel_type = [
    ('001','中介'),
    ('007','用友代理商渠道'),
    ('008', '代账公司渠道'),
    ('100', '市场推广'),
    ('004', '电销'),
    ('103', '保险业务员'),
    ('006', '居间人'),
    ('009', '荐客渠道'),
    ('101', '友金云测分享'),
    ('102', '搜索推广'),
    ('104', '云贷合作部'),
    ('108', '大查柜'),
]

#根据指定营销类型查询合作渠道信息
special_channel_type = sale_channel_type[random.randint(0,3)][0]

#根据营销渠道类型查客户经理
channel_type = sale_channel_type[random.randint(0,len(sale_channel_type))-1][0]



#客户/风控经理配置信息
operation_name_list = ['XIAOWD','ZHAOSMB']
default_operation_name = operation_name_list[0]


#深圳业务部团队二营销人员信息
sz_seller_list = [
    {
    "seller_name":"叶星就",
    "user_id":"YEXJB",
    "seller_id":"0100151",
    "belong_team":"1075501002"
    },
    {
    "seller_name":"刘城",
    "user_id":"LIUCHENGE",
    "seller_id":"75501101",
    "belong_team":"1075501001"
    },
    {
    "seller_name":"洪泽霖",
    "user_id":"HONGZL",
    "seller_id":"75501102",
    "belong_team":"1075501003"
    },
    {
    "seller_name":"陈聪",
    "user_id":"CHENCONGC",
    "seller_id":"75501109",
    "belong_team":"1075501001"
    },
    {
    "seller_name":"纪绍富",
    "user_id":"JISF",
    "seller_id":"75501111",
    "belong_team":"1075501002"
    },
    {
    "seller_name":"孙兆豪",
    "user_id":"SUNZHA",
    "seller_id":"75501113",
    "belong_team":"1075501004"
    },
    {
    "seller_name":"李梅鲜",
    "user_id":"LIMXE",
    "seller_id":"75501116",
    "belong_team":"1075501001"
    },
    {
    "seller_name":"朱小娟",
    "user_id":"ZHUXJC",
    "seller_id":"75501117",
    "belong_team":"1075501002"
    },
    {
    "seller_name":"王姝月",
    "user_id":"WANGSYAA",
    "seller_id":"75501120",
    "belong_team":"1075501003"
    },
    {
    "seller_name":"彭益",
    "user_id":"PENGYID",
    "seller_id":"75501121",
    "belong_team":"1075501002"
    },
    {
    "seller_name":"曾泰安",
    "user_id":"ZENGTAB",
    "seller_id":"75501122",
    "belong_team":"1075501001"
    },
    {
    "seller_name":"谢辉",
    "user_id":"XIEHUIA",
    "seller_id":"75501123",
    "belong_team":"1075501001"
    },
    {
    "seller_name":"洪扬",
    "user_id":"HONGYANG",
    "seller_id":"75501124",
    "belong_team":"1075501004"
    },
    {
    "seller_name":"庄焕发",
    "user_id":"ZHUANGHF",
    "seller_id":"75501125",
    "belong_team":"1075501001"
    },
    {
    "seller_name":"曾东裕",
    "user_id":"ZENGDY",
    "seller_id":"7550114",
    "belong_team":"1075501004"
    },
    {
    "seller_name":"尚金明",
    "user_id":"SHANGJM",
    "seller_id":"7550122",
    "belong_team":"1075501001"
    },
    {
    "seller_name":"吴梦娇",
    "user_id":"WUMJA",
    "seller_id":"7550123",
    "belong_team":"1075501003"
    },
    {
    "seller_name":"向超",
    "user_id":"XIANGCHAO",
    "seller_id":"7550124",
    "belong_team":"1075501002"
    },
    {
    "seller_name":"李盈",
    "user_id":"LIYINGD",
    "seller_id":"7550135",
    "belong_team":"1075501004"
    },
    {
    "seller_name":"徐进进",
    "user_id":"XUJJD",
    "seller_id":"7550137",
    "belong_team":"1075501003"
    },
    {
    "seller_name":"王美杰",
    "user_id":"WANGMJE",
    "seller_id":"7550144",
    "belong_team":"1075501002"
    },
    {
    "seller_name":"陈勇威",
    "user_id":"CHENYWB",
    "seller_id":"7550155",
    "belong_team":"1075501003"
    },
    {
    "seller_name":"邱梓耀",
    "user_id":"QIUZY",
    "seller_id":"7550156",
    "belong_team":"1075501005"
    },
    {
    "seller_name":"刘相国",
    "user_id":"LIUXGG",
    "seller_id":"7550157",
    "belong_team":"1075501002"
    },
    {
    "seller_name":"林业喜",
    "user_id":"LINYXA",
    "seller_id":"7550158",
    "belong_team":"1075501004"
    },
    {
    "seller_name":"毛珊珊",
    "user_id":"MAOSS",
    "seller_id":"7550183",
    "belong_team":"1075501004"
    },
    {
    "seller_name":"张秋菊",
    "user_id":"ZHANGQJC",
    "seller_id":"7550184",
    "belong_team":"1075501004"
    },
    {
    "seller_name":"王锦君",
    "user_id":"WANGJJU",
    "seller_id":"7550191",
    "belong_team":"1075501003"
    },
    {
    "seller_name":"黄向明",
    "user_id":"HUANGXMA",
    "seller_id":"7550194",
    "belong_team":"1075501003"
    },
    {
    "seller_name":"蔡景媚",
    "user_id":"CAIJMD",
    "seller_id":"7550196",
    "belong_team":"1075501004"
    },
    {
    "seller_name":"赵姝",
    "user_id":"ZHAOSHUB",
    "seller_id":"7550198",
    "belong_team":"1075501001"
    },
    {
    "seller_name":"许立惠",
    "user_id":"XULHB",
    "seller_id":"7550202",
    "belong_team":"1075501003"
    },
    {
    "seller_name":"赵艺",
    "user_id":"ZHAOYIB",
    "seller_id":"7550203",
    "belong_team":"1075501002"
    },
    {
    "seller_name":"高菊珍",
    "user_id":"GAOJZA",
    "seller_id":"7550207",
    "belong_team":"1075501003"
    },
    {
    "seller_name":"文怡庭",
    "user_id":"WENYT",
    "seller_id":"7550208",
    "belong_team":"1075501003"
    },
    {
    "seller_name":"胡涛",
    "user_id":"HUTAO",
    "seller_id":"7570103",
    "belong_team":"1075501002"
}
]

#营销人员id，用来根据id批量查询营销人员信息
seller_id_list  = []
for i in range(5):
    seller_id_list.append(sz_seller_list[random.randint(0,len(sz_seller_list))-1]['seller_id'])


#代账公司渠道南区团队营销人员信息
dz_seller_list = [
    {
    "seller_id":"103",
    "user_id":"MAOXXA",
    "seller_name":"毛新逊"
    },
    {
    "seller_id":"105",
    "user_id":"ZHOUTAOD",
    "seller_name":"周涛"
    },
    {
    "seller_id":"107",
    "user_id":"XUTAOF",
    "seller_name":"许涛"
    },
    {
    "seller_id":"113",
    "user_id":"JIANGWJB",
    "seller_name":"江文杰"
    },
    {
    "seller_id":"126",
    "user_id":"FENGTYA",
    "seller_name":"冯天宇"
    },
    {
    "seller_id":"154",
    "user_id":"LIAOTM",
    "seller_name":"廖铁苗"
    }
]

# 营销渠道为代账/代理渠道,带出合作渠道绑定的客户经理
dz_seller_id = dz_seller_list[random.randint(0,len(dz_seller_list))-1]['seller_id']



#风控总
wind_control = 'SIJL'


#机构配置信息
org_id_list = ['755','010']
default_org_id = org_id_list[0]


#机构门店配置信息
operate_org_id_list = ['75501']
default_operate_org_id = operate_org_id_list[0]


#枚举值
code_detail_list = [
        "Purpose",
        "Bank",
        "ApplyStatus",
        "CompanyCertType",
        "CompanyType",
        "CustomerType",
        "EducationExperience",
        "EmployeeType",
        "EnterpriseCertType",
        "WorkEnterpriseType",
        "FamilyStatus",
        "LoanType",
        "ReturnMethod",
        "Marriage",
        "OfficialLevel",
        "AgreeEnum",
        "ReturnPeriod",
        "PlaceOwnerShip",
        "PosionLevel",
        "PostAddress",
        "RelationShip",
        "SaleChannel",
        "Sex",
        "TermMonth",
        "WorkNature",
        "DocumentType",
        "OrgInfo",
        "PhaseNo",
        "BusinessType"
]
code_list = []
for i in range(5):
    code_list.append(code_detail_list[random.randint(0,len(code_detail_list))-1])


#生产银行卡号
def gen_card_num(start_with, total_num):

    result = start_with

    # 随机生成前N-1位
    while len(result) < total_num - 1:
        result += str(random.randint(0, 9))

    # 计算前N-1位的校验和
    s = 0
    card_num_length = len(result)
    for _ in range(2, card_num_length + 2):
        t = int(result[card_num_length - _ + 1])
        if _ % 2 == 0:
            t *= 2
            s += t if t < 10 else t % 10 + t // 10
        else:
            s += t

    # 最后一位当做是校验位，用来补齐到能够整除10
    t = 10 - s % 10
    result += str(0 if t == 10 else t)
    return result

#银行卡号
bank_no = {
    'share':gen_card_num('6222024',16),
    'HXB':gen_card_num('621469',16),
    'CDB':gen_card_num('622936',16),
    'LFB':gen_card_num('621340',16),
    'CCNS':gen_card_num('623181',16)
}
