import requests,re
import datetime


def get_work():
    url = r"https://hr.yylending.com/a/oa/clock"
    heders = {
        "Content-Type":"application/x-www-form-urlencoded",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Cookie":"pageSize=20; ceis.session.id=c75d8ced72c14cac87b6b2ef6dd902d5; JSESSIONID=3935EBB3DD55352AE88558CA594E29B2; yjs_sso_token=8af10300-f7d3-4b35-8f1d-a41bdb1d2c6f; pageNo=3"
    }
    data = {"pageNo":"1","pageSize":"6000","createDateStart":"2020-01-01","createDateEnd":"2020-12-31"}

    res = requests.request("post",url,data=data,headers=heders).text
    lis = re.findall(r'<td>2020-(.*?)</td>',res)
    print(lis)
    print(len(lis))
    sum= 0
    for i in lis:
        i = '2020-'+i
        whatday = datetime.datetime.strptime(i, '%Y-%m-%d %H:%M:%S').strftime("%w")
        if int(i[11:13])>19 or whatday in ("0","6"):
            if whatday in ("0","6"):
                h = 8
            elif int(i[14:16]) >= 30:
                h = int(i[11:13]) - 18
            else:
                h = int(i[11:13]) - 19
            sum += h
            print(i,whatday,h)
    print(sum)

def get_holiday():
    apply_list = []
    url = r"https://hr.yylending.com/a/oa/leave/myApply"
    heders = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Cookie": "pageSize=20; ceis.session.id=c75d8ced72c14cac87b6b2ef6dd902d5; JSESSIONID=3935EBB3DD55352AE88558CA594E29B2; yjs_sso_token=8af10300-f7d3-4b35-8f1d-a41bdb1d2c6f; pageNo=1"
    }
    data = {"pageNo":"1","pageSize":"200","ids":"","createDateStart":"","createDateEnd":""}
    # res = requests.request("post", url, data=data, headers=heders).text
    # lis = re.findall(r'<td><a href="/a/oa/leave/detail\?id=(.*?)">', res)
    lis = ['LEAVE20200312149005', 'LEAVE20200114146442', 'LEAVE20200114146441', 'LEAVE20200102145452', 'LEAVE20191226144779', 'LEAVE20191224144555', 'LEAVE20191217144082', 'LEAVE20191216143994', 'LEAVE20191206143597', 'LEAVE20191113141460', 'LEAVE20191025139468', 'LEAVE20191011138705', 'LEAVE20190923136539', 'LEAVE20190919136366', 'LEAVE20190827134258', 'LEAVE20190812133019', 'LEAVE20190730131443', 'LEAVE20190716130067', 'LEAVE20190704129289', 'LEAVE20190620127312', 'LEAVE20190617127035', 'LEAVE20190614126935', 'LEAVE20190529124051', 'LEAVE20190514122389', 'LEAVE20190514122388', 'LEAVE20190425118826', 'LEAVE20190425118823', 'LEAVE20190425118822', 'LEAVE20190328114562', 'LEAVE20190328114560', 'LEAVE20190312112473', 'LEAVE20190225109425', 'LEAVE20190214107936', 'LEAVE20190122103638', 'LEAVE20190118101945', 'LEAVE20190118101944', 'LEAVE20190107100967', 'LEAVE20181221096350', 'LEAVE20181221096348', 'LEAVE20181210095382', 'LEAVE20181203093666', 'LEAVE20181126091502', 'LEAVE20180929083512', 'LEAVE20180817075481', 'LEAVE20180808074492', 'LEAVE20180727071353', 'LEAVE20180723070284', 'LEAVE20180529060331', 'LEAVE20180526059551']
    url2 = "https://hr.yylending.com/a/oa/leave/detail?id="
    for id in lis:
        url_new = url2+id
        res2 = requests.request("get", url_new, headers=heders).text
        text = r'''<div class="control-group" id="showLeaveTime">
			<label class="control-label">请假时长：</label>
			<div class="controls">
				(.*?)
			</div>'''
        if re.findall(text, res2):
            day = re.findall(text, res2)[0]
            apply_list.append((id,day))
    return apply_list

print(get_holiday())
