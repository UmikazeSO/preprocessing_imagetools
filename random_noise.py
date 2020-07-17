import os
from progress.bar import ShadyBar
from progress.bar import Bar
import PIL
from PIL import Image  # 生成图片
from PIL import ImageDraw  # 控制图片内容
import random


def random_color():
    return random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)


# draw有很多功能
# draw.text() 往里面添加文本
# draw.line() 往里面添加线
# draw.point() 往里添加噪点
# PIL.ImageDraw.Draw.ellipse(xy, fill=None, outline=None) 往里面添加椭圆
# PIL.ImageDraw.Draw.polygon(xy, fill=None, outline=None) 往里面添加多边形


def random_paint(src, dst):
    # 生成一个0-255的三位元组 用以控制背景颜色
    background_color = (0, 0, 0, 0)
    # 生成一个图片(模式，图片尺寸，颜色（用之前调好的随机颜色就好）
    image = Image.new('RGBA', (600, 500), background_color)
    # 生成一个编辑对象 可以对image对象添加各种属性 实际是对刚才生成的image对象做编辑
    draw = ImageDraw.Draw(image)

    # 随机多边形 9 15 5
    width = 800
    height = 600
    for j in range(5):
        x = random.randint(0, width)
        x1 = random.randint(x, x + 20)
        x2 = random.randint(x, x + 35)
        x3 = random.randint(x, x + 40)
        x4 = random.randint(x, x + 55)
        y = random.randint(0, height)
        y1 = random.randint(y, y + 20)
        y2 = random.randint(y, y + 35)
        y3 = random.randint(y, y + 40)
        y4 = random.randint(y, y + 55)
        # 往里面添加多边形
        draw.polygon([(x, y), (x1, y1), (x2, y2), (x3, y3), (x4, y4)], fill=random_color(), outline=random_color())

    # 随机空心椭圆 20 10
    for i in range(10):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(x1, x1 + 50)
        y2 = random.randint(y1, y1 + 50)
        draw.ellipse([(x1, y1), (x2, y2)], fill=random_color(), outline=random_color())
        draw.ellipse([(x1+1, y1+1), (x2-1, y2-1)], fill=background_color, outline=random_color())
    # 随机椭圆 20 10
    for i in range(10):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(x1, x1 + 50)
        y2 = random.randint(y1, y1 + 50)
        draw.ellipse([(x1, y1), (x2, y2)], fill=random_color(), outline=random_color())
    # 随机杂点 20 10
    for k in range(10):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=random_color())  # 画点(([点坐标]),颜色)
        x = random.randint(0, width)
        y = random.randint(0, height)
        rad = random.randint(0, 180)

    image.save("./here.png", "png")  # 图片对象保存（地址，格式）
    background = Image.open(src)
    foreground = Image.open("here.png")
    background.paste(foreground, (380, 100), foreground)
    #  background.show()
    background.save(dst, "png")


if __name__ == '__main__':
    path = r"../empty_bg"
    out_path = r"../dirty_bg"
    filelist = os.listdir(path)
    i = 40000
    bar = Bar('Processing', max=len(filelist))
    for files in filelist:
        src = path + "/" + files
        dst = out_path + "/" + "dirty_bg_" + str(i) + ".jpg"
        xml = out_path + "/" + "dirty_bg_" + str(i) + ".xml"
        open(os.path.join(xml), "w")
        random_paint(src, dst)
        i += 1
        bar.next()
    bar.finish()



