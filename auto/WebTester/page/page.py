from lib.pyse import Pyse


class BasePage(object):
    def __init__(self):
        self.d = Pyse('chrome')

    def url(self):
        self.d.open('http://zbox.imdsx.cn')

    def quit(self):
        self.d.quit()
class LoginPage(BasePage):
    def username(self):
        self.d.type("id=>account", "admin")

    def password(self):
        self.d.type("name=>password", "houyafan123")

    def login_button(self):
        self.d.click("id=>submit")

    def keep_login(self):
        self.d.js("document.getElementById('keepLoginon').setAttribute('checked','checked')")

    def login_check(self, name):
        return self.d.wait_and_save_exception('css=>a[href="/user-logout.html1"]', name)


class BugPage(LoginPage):
    def tag_bug(self):
        self.d.click("css=>a[href='/bug/']")

    def create_bug(self):
        self.d.click("css=>a[href^='/bug-create']")

    def module(self):
        self.d.click("css=>#module_chosen>a")
        self.d.click("css=>#module_chosen>div>ul>li[data-option-array-index='1']")

    def module_select(self):
        self.d.js("document.getElementById('module').style.display='';")
        self.d.select_by_value('css=>#module','2')


    def system(self):
        self.d.select_by_value("css=>#os", "win8")

    def browser(self):
        self.d.select_by_value("css=>#browser", "all")

    def build(self):
        self.d.click("css=>#openedBuild_chosen")
        self.d.click("css=>#openedBuild_chosen>div>ul>li[data-option-array-index='1']")

    def assign(self):
        self.d.click("css=>#assignedTo_chosen")
        self.d.click("css=>#assignedTo_chosen>div>ul>li[data-option-array-index='1']")

    def end_date(self):
        self.d.type("css=>#deadline", '2018-01-25')

    def bug_title(self):
        self.d.type('css=>#title', 'UI自动化创建BUG')

    def steps(self):
        self.d.js("document.getElementById('steps').innerText = '1、启动浏览器 2、运行driver 3、运行测试case'")

    def save(self):
        self.d.js("window.scrollTo(0,800);")
        self.d.click('css=>#submit')

    def create_bug_check(self, name):
        return self.d.wait_and_save_exception("css=>a[href^='/bug-create']", name)

    def clear_date(self):
        """
        洗数据
        :return:
        """
        sql = "DELETE FROM zt_bug WHERE title LIKE 'UI%';"
        self.m.execute_sql(sql)


class Page(BugPage):
    pass
