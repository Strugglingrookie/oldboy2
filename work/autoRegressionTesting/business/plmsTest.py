# coding=utf-8
import os, sys
import unittest
import requests

BASEPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASEPATH)

from config import Config
from tools.plms_tools import oracle_sql, mysql_sql


class PLMSTest(unittest.TestCase):
    configPath = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.yml")
    config = Config(configPath)
    curEnv = config.getCfgValue("curEnv")
    url = config.getCfgValue(curEnv, "PLMS", "url")

    @classmethod
    def setUpClass(cls):  # 在所有用例执行之前运行的
        pass

    @classmethod
    def tearDownClass(cls):  # 在所有用例都执行完之后运行的
        pass

    def setUp(self):  # 每个用例运行之前运行的
        pass

    def tearDown(self):  # 每个用例运行之后运行的
        pass

    def get_coreDB_info(self):
        db_info = self.config.getCfgValue(self.curEnv, "CORE", "MYDB")
        return db_info

    def get_plmsDB_info(self):
        db_info = self.config.getCfgValue(self.curEnv, "PLMS", "DB")
        print(db_info)
        return db_info

    def get_PLMS_header(self):
        header = self.config.getCfgValue(self.curEnv, "PLMS", "header")
        return header

    def login(self):    # 登陆
        path = '/plms-um-service/http/user/login'
        data = {"password": "96qyVNn/porDY", "userId": "sijl"}
        header = self.get_PLMS_header()
        res = requests.post(self.url + path, json=data, headers=header).json()
        token = res.get('data').get('accToken') if res.get('data') else None
        self.assertTrue(token)
        return token


    # 一次性费用还款
    def getLoanNo(self, token):  # 一次性费用还款  ------->  一次性费用借据列表
        path = '/plms-repay-service/http/repay/oncefee/getOnceFeeList'
        data = {"pageNo": 1, "pageSize": 10}
        header = self.get_PLMS_header()
        header["acctoken"] = token
        res = requests.post(self.url + path, json=data, headers=header).json()
        loanNo = None
        if res.get('data') and res.get('data').get('list'):
            for var in res.get('data').get('list'):
                responseMsg = var.get("responseMsg")
                if not responseMsg:
                    loanNo = var.get("loanNo")
                    break
        self.assertTrue(loanNo)
        return loanNo

    def getOnceFeeDetail(self, token, loanNo):# 一次性费用还款  ------->  一次性费用借据详情
        path = '/plms-repay-service/http/repay/oncefee/getOnceFeeDetail'
        data = {"loanNo": loanNo}
        header = self.get_PLMS_header()
        header["acctoken"] = token
        res = requests.post(self.url + path, json=data, headers=header).json()
        paySum = res.get('data').get('paySum') if res.get('data') else None
        self.assertTrue(paySum)
        return paySum

    def onceFeeDeduct(self, token, loanNo, paySum):  # 一次性费用还款  ------->  一次性费用还款
        path = '/plms-repay-service/http/repay/oncefee/onceFeeDeduct'
        data = {"actualPaySum": paySum, "loanNo": loanNo}
        header = self.get_PLMS_header()
        header["acctoken"] = token
        res = requests.post(self.url + path, json=data, headers=header).json()
        retCode = res.get('retCode')
        return retCode


    # 预还款
    def getOverDueRepayDetail(self, token):  # 预还款  ------->  逾期管理费还款费用详情
        db_info = self.get_plmsDB_info()
        sql = "SELECT * FROM plms_case_distribute WHERE attribute_queue=300001 AND sterm+20<total_sterm LIMIT 1"
        loanNo = mysql_sql(sql,**db_info)[0][1]
        path = '/plms-repay-service/http/repay/overdue/getOverDueRepayDetail'
        data = {"loanNo": loanNo}
        header = self.get_PLMS_header()
        header["acctoken"] = token
        res = requests.post(self.url + path, json=data, headers=header).json()
        allPayBalance = res.get('data').get('allPayBalance') if res.get('data') else None
        unPayOneTimeFee = res.get('data').get('unPayOneTimeFee') if res.get('data') else 0
        self.assertTrue(allPayBalance)
        return loanNo,allPayBalance,unPayOneTimeFee

    def getOverDueRepayCommit(self,token, loanNo, allPayBalance, unPayOneTimeFee):  # 预还款  ------->  逾期管理费还款
        path = '/plms-repay-service/http/repay/overdue/getOverDueRepayCommit'
        data = {"loanNo": loanNo, "unPayOneTimeFee": unPayOneTimeFee, "payAmount": allPayBalance, "allPayBalance": allPayBalance}
        header = self.get_PLMS_header()
        header["acctoken"] = token
        res = requests.post(self.url + path, json=data, headers=header).json()
        retCode = res.get('retCode')
        self.assertEqual(retCode, '000000')

    def getPrerepayLoanPlan(self, token, loanNo):  # 预还款  ------->  预还款期次费用信息
        path = '/plms-repay-service/http/repay/prerepay/getPrerepayLoanPlan'
        data = {"loanNo": loanNo}
        header = self.get_PLMS_header()
        header["acctoken"] = token
        res = requests.post(self.url + path, json=data, headers=header).json()
        payAmount = res.get('data').get('payAmount') if res.get('data') else None
        sterm = res.get('data').get('sterm') if res.get('data') else None
        self.assertTrue(payAmount)
        self.assertTrue(sterm)
        print(payAmount,sterm)
        return payAmount,sterm

    def aheadDeductCommit(self, token, loanNo, payAmount, sterm):  # 预还款  ------->  预还款期次费用信息
        path = '/plms-repay-service/http/repay/prerepay/aheadDeductCommit'
        data = {"loanNo": loanNo, "amount": 10, "term": sterm}  # payAmount 可以小于应还金额
        header = self.get_PLMS_header()
        header["acctoken"] = token
        res = requests.post(self.url + path, json=data, headers=header).json()
        retCode = res.get('retCode')
        return retCode


    # 代偿手续费还款
    def getCompensatoryFeeInfoList(self, token):  # 代偿手续费还款  ------->  代偿手续费还款列表
        path = '/plms-repay-service/http/repay/compensatoryFee/getCompensatoryFeeInfoList'
        data = {"loanNo": "", "customerName": "", "orgName": "", "pageNo": 1, "pageSize": 10}
        header = self.get_PLMS_header()
        header["acctoken"] = token
        res = requests.post(self.url + path, json=data, headers=header).json()
        loanNo = None
        paySum = None
        if res.get('data') and res.get('data').get('list'):
            for var in res.get('data').get('list'):
                responseMsg = var.get("responseMsg")
                if not responseMsg:
                    loanNo = var.get("loanNo")
                    paySum = var.get("paySum")
                    break
        self.assertTrue(loanNo)
        self.assertTrue(paySum)
        return loanNo, paySum

    def payPguaFee(self, token, loanNo, paySum):  # 代偿手续费还款  ------->  代偿手续费还款
        path = '/plms-repay-service/http/repay/compensatoryFee/payPguaFee'
        data = {"payAmount": paySum, "loanNo": loanNo}
        header = self.get_PLMS_header()
        header["acctoken"] = token
        res = requests.post(self.url + path, json=data, headers=header).json()
        retCode = res.get('retCode')
        return retCode

    # 追偿逾期还款
    def guaranteePayCommit(self, token):  # 追偿逾期还款  ------->  追偿逾期还款
        db_info = self.get_coreDB_info()
        get_loanNo_sql = "SELECT * from (select LOAN_NO from ph_disposal_loanplan GROUP BY LOAN_NO ORDER BY LOAN_NO DESC) WHERE ROWNUM=1"
        loanNo = oracle_sql(db_info,get_loanNo_sql)[0][0]
        get_guaranteePay_sql = "select * from ph_disposal_repayrecord where loan_no = '%s'" % loanNo
        actual_org = oracle_sql(db_info, get_guaranteePay_sql)[0]
        org_money = actual_org[6]+actual_org[8]+actual_org[10]+actual_org[12]+actual_org[14]
        path = '/plms-repay-service/http/repay/guaranteePay/guaranteePayCommit'
        data = {"loanNo": loanNo, "repayAmount": "10"}
        header = self.get_PLMS_header()
        header["acctoken"] = token
        res = requests.post(self.url + path, json=data, headers=header).json()
        retCode = res.get('retCode')
        return retCode, loanNo, org_money

    def xg_test_PLMS_001_一次性费用还款(self):
        # 测试步骤
        token = self.login()
        loanNo = self.getLoanNo(token)
        paySum = self.getOnceFeeDetail(token, loanNo)
        retCode = self.onceFeeDeduct(token, loanNo, paySum)
        # 接口返回结果判断
        self.assertEqual(retCode, '000000')
        # 数据库结果判断  PAY_OFF_FLAG 结清标志为1
        db_info = self.get_coreDB_info()
        sql = "SELECT * from (select PAY_OFF_FLAG from PH_LOANOUT_FEE_REPAY_RECORD f where f.LOAN_NO='%s' ORDER BY UPDATE_TIME DESC) WHERE ROWNUM<2" % loanNo
        res = oracle_sql(db_info, sql)
        flag = 0 if not res else res[0][0]
        self.assertEqual(flag, '1')
        print("一次性费用还款成功", loanNo, paySum)

    def xg_test_PLMS_002_逾期管理费还款_预还款(self):
        token = self.login()
        loanNo, allPayBalance, unPayOneTimeFee = self.getOverDueRepayDetail(token)
        self.getOverDueRepayCommit(token, loanNo, allPayBalance, unPayOneTimeFee)
        payAmount, sterm = self.getPrerepayLoanPlan(token, loanNo)
        retCode = self.aheadDeductCommit(token, loanNo, payAmount, sterm)
        # 接口返回结果判断
        self.assertEqual(retCode, '000000')
        # 数据库结果判断  status为S
        db_info = self.get_coreDB_info()
        sql = "select * from ph_prerepayrecord where loanapplyserialno ='%s' and sterm=%s" %(loanNo,sterm)
        res = oracle_sql(db_info, sql)
        money = 0 if not res else res[0][5]
        status = 0 if not res else res[0][6]
        self.assertEqual(money, 10)
        self.assertEqual(status, 'S')
        print("预还款成功",loanNo, sterm, 10)

    def xg_test_PLMS_003_代偿手续费还款(self):
        token = self.login()
        loanNo, paySum = self.getCompensatoryFeeInfoList(token)
        retCode = self.payPguaFee(token, loanNo, paySum)
        # 接口返回结果判断
        self.assertEqual(retCode, '000000')
        # 数据库结果判断  status为S
        db_info = self.get_coreDB_info()
        sql = "select * from PH_LOANOUT_FEE_REPAY_RECORD ee where ee.loan_no='%s'" %loanNo
        res = oracle_sql(db_info, sql)
        flag = 0 if not res else res[0][-3]
        actual_pay = 0 if not res else res[0][-5]
        self.assertEqual(flag, "1")
        self.assertEqual(str(actual_pay), paySum)
        print("代偿手续费还款成功",loanNo, paySum)

    def xg_test_PLMS_004_追偿逾期还款(self):
        token = self.login()
        retCode, loanNo, org_money = self.guaranteePayCommit(token)
        # 接口返回结果判断
        self.assertEqual(retCode, '000000')
        # 数据库结果判断  status为S
        db_info = self.get_coreDB_info()
        get_guaranteePay_sql = "select * from ph_disposal_repayrecord where loan_no = '%s'" % loanNo
        actual_new = oracle_sql(db_info, get_guaranteePay_sql)[0]
        new_money = actual_new[6] + actual_new[8] + actual_new[10] +  actual_new[12] + actual_new[14]
        money = new_money - org_money
        self.assertEqual(money, 10)
        print("追偿逾期还款成功",loanNo, 10)


if __name__ == '__main__':
    unittest.main()
