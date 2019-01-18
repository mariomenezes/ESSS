import sys
from PIL import Image

img = Image.open(sys.argv[2])
width, height = img.size

img_red = Image.new('RGB', (width, height), "black")
img_green = Image.new('RGB', (width, height), "black")
img_blue = Image.new('RGB', (width, height), "black")
img_blur = Image.new('RGB', (width, height), "black")

img.show()


#def rgb_filter(img):
#    for x in range(width):
#        for y in range(height):
#            r, g, b = img.getpixel((x, y))
#
#            red = (r,0,0)
#            img_red.putpixel((x, y), red)
#
#            green = (0,g,0)
#            img_green.putpixel((x,y), green)
#
#            blue = (0,0,b)
#            img_blue.putpixel((x,y), blue)
#
#
#    img_red.show()
#    img_green.show()
#    img_blue.show()
#
#
#    img_red.save("new_red.png")
#    img_green.save("new_green.png")
#    img_blue.save("new_blue.png")


#min_value = 0


#def return_new_pixel(x,y,img, radius, weight):
#
#    radius = int(radius)
#    weight = int(weight)
#
#
#    pixel_list = []
#
#    #add center at first
#    point = [x,y]
#    pixel_list.append(point)
#
#    begin_x = x - radius
#    end_x = x + radius
#
#    begin_y = y - radius
#    end_y = y + radius
#    for x_range in range(begin_x, end_x):
#        for y_range in range(begin_y, end_y):
#            if((x_range >= min_value and x_range < width) and (y_range >= min_value and y_range < height)):
#                point = [x_range, y_range]
#                pixel_list.append(point)
#
#    #do the math for r,g,b list
#    new_value = [0,0,0]
#
#    x_weight, y_weight = pixel_list.pop(0)
#    r,g,b = img.getpixel((x_weight, y_weight))
#    r *= weight
#    g *= weight
#    b *= weight
#
#    new_value[0] += r
#    new_value[1] += g
#    new_value[2] += b
#
#    for x_,y_ in pixel_list:
#        r,g,b = img.getpixel((x_,y_))
#        new_value[0] += r
#        new_value[1] += g
#        new_value[2] += b
#
#    #size increased by weight
#    size = len(pixel_list) + weight-1
#
#    for i in range(0,len(new_value)):
#        new_value[i] = int(new_value[i]/size)
#
#    return new_value

#def do_blur(img, radius, weight):
#
#    for x in range(width):
#        for y in range(height):
#            #r, g, b = img.getpixel((x, y))
#            ret = tuple(return_new_pixel(x,y,img, radius, weight))
#            img_blur.putpixel((x,y), ret)
#
#    img_blur.show()
#    img_blur.save("test-image-blur-radius"+radius+ "-weight" + weight+".png")


if(sys.argv[1] == "-blur"):
    radius = sys.argv[3]
    weight = sys.argv[4]
    do_blur(img, radius, weight)
elif(sys.argv[1] == "-rgb"):
    rgb_filter(img)

