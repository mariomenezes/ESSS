from filter import Filter
from PIL import Image
from IO.show_write import Write


class Blur(Filter):

    def __init__(self, _read):
        self.__img = _read.get_image()
        super().__init__(self.__img)
        self.img_blur = Image.new('RGB', (self.width, self.height), "black")
        self.__radius = None
        self.__weight = None

    def return_new_pixel(self, coord_x, coord_y, radius, weight):

        radius = int(radius)
        weight = int(weight)

        pixel_list = []

        # add center at first
        point = [coord_x, coord_y]
        pixel_list.append(point)

        begin_x = coord_x - radius
        end_x = coord_x + radius

        begin_y = coord_y - radius
        end_y = coord_y + radius
        for x_range in range(begin_x, end_x):
            for y_range in range(begin_y, end_y):
                if((x_range >= self.min_value and x_range < self.width) and (y_range >= self.min_value and y_range < self.height)):
                    point = [x_range, y_range]
                    pixel_list.append(point)

        # do the math for r,g,b list
        new_value = [0, 0, 0]

        x_weight, y_weight = pixel_list.pop(0)
        r, g, b = self.img.getpixel((x_weight, y_weight))
        r *= weight
        g *= weight
        b *= weight

        new_value[0] += r
        new_value[1] += g
        new_value[2] += b

        for x_,y_ in pixel_list:
            r,g,b = self.img.getpixel((x_, y_))
            new_value[0] += r
            new_value[1] += g
            new_value[2] += b

        # size increased by weight
        size = len(pixel_list) + weight-1

        for i in range(0,len(new_value)):
            new_value[i] = int(new_value[i]/size)

        return new_value

    def execute(self):

        self.__radius = input("Type the Blur radius: ")
        self.__weight = input("Type the Blur weight: ")

        for x in range(self.width):
            for y in range(self.height):
                ret = tuple(self.return_new_pixel(x, y, self.__radius, self.__weight))
                self.img_blur.putpixel((x, y), ret)

        _write = Write(self.img_blur, "test-image-blur-radius"+self.__radius+"-weight" + self.__weight+".png")
        _write.show_img()
        _write.write_img()

    def get_restrictions(self):
        return False



