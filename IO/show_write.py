import functools
import sys


class Write:

    @functools.singledispatch
    def __init__(self, image, file_name):
        self.__image = image
        self.__filename = file_name

    def show_img(self):
        try:
            self.__image.show()
        except IOError:
            print("Unable to show image")
            sys.exit(1)

    def write_img(self):
        try:
            self.__image.save(self.__filename)
        except IOError:
            print("Unable to show image")
            sys.exit(1)


