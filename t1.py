from PIL import Image


im = Image.new("RGB", (512, 512))
pix = im.load()
for x in range(512):
    for y in range(512):
        pix[x,y] = (256-x,256-y,x+y)

im.save("test.jpg", "JPEG")