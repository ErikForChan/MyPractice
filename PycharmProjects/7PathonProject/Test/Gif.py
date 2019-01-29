from PIL import Image

im = Image.open("D:/img/1.jpg")
images = []
images.append(Image.open('D:/img/2.jpg'))
images.append(Image.open('D:/img/1.png'))

im.save('D:/gif.gif', save_all=True, append_images=images, loop=3, duration=1, comment=b"aaabb")