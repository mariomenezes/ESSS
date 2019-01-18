from PIL import Image


class Read(object):

    class __Read:

        def __init__(self, argv):
            self.__img = Image.open(argv[1])
            self.__width, height = self.__img.size
            self.__func = None

        def get_image(self):
            return self.__img

        def get_width(self):
            return self.__width

        def get_func(self):
            return self.__func

        def set_func(self, filter_num):
            self.__func = filter_num

        def get_img_mode(self):
            return self.__img.mode

    instance = None

    # Singleton Pattern to avoid new instances of read class
    def __new__(cls, argv): # __new__ always a classmethod
        if not Read.instance:
            Read.instance = Read.__Read(argv)
        return Read.instance



