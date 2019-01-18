from filter import Filter
from PIL import Image
from IO.show_write import Write


class Rgb(Filter):

    def __init__(self, _read):
        self.__img = _read.get_image()
        super().__init__(self.__img)
        self.__img_red = Image.new('RGB', (self.width, self.height), "black")
        self.__img_green = Image.new('RGB', (self.width, self.height), "black")
        self.__img_blue = Image.new('RGB', (self.width, self.height), "black")

    def execute(self):

        for x in range(self.width):
            for y in range(self.height):
                r, g, b = self.img.getpixel((x, y))

                red = (r, 0, 0)
                self.__img_red.putpixel((x, y), red)

                green = (0, g, 0)
                self.__img_green.putpixel((x, y), green)

                blue = (0, 0, b)
                self.__img_blue.putpixel((x, y), blue)

        image_list = []
        file_name_list = []
        image_list.append(self.__img_red)
        file_name_list.append("new_red.png")
        image_list.append(self.__img_green)
        file_name_list.append("new_green.png")
        image_list.append(self.__img_blue)
        file_name_list.append("new_blue.png")


        for index in range(0, len(image_list)):
            _write = Write(image_list[index], file_name_list[index])
            _write.show_img()
            _write.write_img()


    def get_restrictions(self):
        # using test-image.png, if you want to test this restriction, change return to "RGB"
        return "L"
