import time
import pytesseract
from PIL import Image, ImageEnhance
from my_pyse import Pyse


# pyse = Pyse("chrome")
# url = "https://testyyfax8446.yylending.com/web/register.html"
# pyse.open(url)

# pyse.type('css=>[name="phone"]','13436589654')
# pyse.type('css=>[name="password"]','a123456')
# pyse.type('css=>[name="verifyImageCode"]','123456')
# pyse.type('css=>[name="verifyCode"]','123456')
# pyse.click('css=>#regBtn')
file_path = "imgcode.png"
# pyse.get_window_img(file_path)
ran = Image.open(file_path)  # 打开截图，获取验证码位置，截取保存验证码
box = (1430, 305, 1516, 340)  # 获取验证码位置,自动定位不是很明白，就使用了手动定位，代表（左，上，右，下）
ran.crop(box).save("code.png")  # 把获取的验证码保存
# 获取验证码图片，读取验证码
imageCode = Image.open("code.png")  # 打开保存的验证码图片
# imageCode.load()
# # 图像增强，二值化
sharp_img = ImageEnhance.Contrast(imageCode).enhance(2.0)
sharp_img.save("code2.png")  # 保存图像增强，二值化之后的验证码图片
sharp_img.load()  # 对比度增强
time.sleep(2)
print(sharp_img)  # 打印图片的信息
code = pytesseract.image_to_string(sharp_img).strip()  # 读取验证码
# # 5、收到验证码，进行输入验证
print(code)  # 输出验证码
# name.send_keys('60037')  # 给定位账号的输入框中输入值
# password.send_keys('123456')  # 给定位密码的输入框中输入值
# code1.send_keys(code)  # 给定位验证码的输入框中输入读取到的验证码
# click = driver.find_element_by_name("yt0").click()  # 点击登录
# time.sleep(2)
# # 关闭浏览器
# driver.quit()
