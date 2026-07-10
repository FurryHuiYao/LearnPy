from PIL import Image
from PIL import ImageFilter
import numpy as np
import matplotlib.pyplot as plt
from time import sleep

def main():
    #显示图片基本信息
    im = Image.open("test.png")
    print(im.format)
    print(im.size)
    print(im.mode)
    im.rotate(45).show()
    sleep(3)

    #加上浮雕效果
    omg = im.filter(ImageFilter.EMBOSS)
    omg.save("test_emboss.png")
    omg.show()
    sleep(3)

    #压缩图片
    im.thumbnail((128,128))
    im.save("test_zipped.png")
    im.show()
    sleep(3)

    #数学绘图
    x = np.linspace(0, 10, 1000)
    y = np.sin(x)
    plt.figure(figsize=(8,4))
    plt.title("sin(x)")
    plt.plot(x, y, label="sin(x)", color="red", linewidth=2)
    plt.ylim(-1.5, 1.5)
    plt.xlim(0, 10)
    plt.legend()
    plt.show()
    sleep(3)

    #黑白图像
    img = np.array(Image.open("test.png").convert("L"))
    rows, cols = img.shape
    for i in range(rows):
        for j in range(cols):
            if img[i, j] >= 128:
                img[i, j] = 1
            else:
                img[i, j] = 0
    plt.figure("test")
    plt.imshow(img, cmap="gray")
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    main()