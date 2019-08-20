from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import random, string

def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def get_valid_img(request):
    # 方式一 直接读取一张图片
    # with open(r'%s\avatars\lufei.jg'%settings.MEDIA_ROOT, 'rb') as f:
    #     data = f.read()


    # 方式二 生成一张随机颜色的图片用 pillow 模块   pip install pillow
    # import random
    # from PIL import Image
    # random_color = get_random_color()
    # img = Image.new('RGB', (270,40), color=random_color)
    # with open('valid_image.png', 'wb') as f:
    #     img.save(f, 'png')
    # with open('valid_image.png', 'rb') as f:
    #     data = f.read()


    # 方式三  方式二是在通过磁盘存取，存在一定的io时间，性能较差，改为内存存取
    # import random
    # from PIL import Image
    # from io import BytesIO
    # random_color = get_random_color()
    # img = Image.new('RGB', (270, 40), color=random_color)
    # f = BytesIO()
    # img.save(f, 'png')
    # data = f.getvalue()


    # 方式四 上面的只是加了背景图，还没有加校验码
    # from PIL import Image, ImageDraw, ImageFont
    # from io import BytesIO
    # import random, string
    #
    # img = Image.new('RGB', (270,40), color=get_random_color())
    # draw = ImageDraw.Draw(img)
    # kumo_font = ImageFont.truetype('statics/font/kumo.ttf', size=32)
    # str_pool = string.ascii_letters + string.digits # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    # valid_code_str = random.sample(str_pool, 5)
    #
    # for i in range(5):
    #     draw.text((i*50+22,5),valid_code_str[i],get_random_color(),font=kumo_font)
    #
    # f = BytesIO()
    # img.save(f, 'png')
    # data = f.getvalue()


    # 方式五 加上噪点和噪线
    str_pool = string.ascii_letters + string.digits  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    valid_code_str = random.sample(str_pool, 5)
    request.session['valid_code_str'] = valid_code_str  # 存session，给视图函数用来校验验证码是否正确

    img = Image.new('RGB', (270, 40), color=get_random_color())
    draw = ImageDraw.Draw(img)
    kumo_font = ImageFont.truetype('statics/font/kumo.ttf', size=32)

    for i in range(5):
        draw.text((i * 50 + 22, 5), valid_code_str[i], get_random_color(), font=kumo_font)

    width=270
    height=40
    for i in range(8):
        x1=random.randint(0,width)
        x2=random.randint(0,width)
        y1=random.randint(0,height)
        y2=random.randint(0,height)
        draw.line((x1,y1,x2,y2),fill=get_random_color())

    for i in range(80):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=get_random_color())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=get_random_color())

    f = BytesIO()
    img.save(f, 'png')
    data = f.getvalue()

    return data