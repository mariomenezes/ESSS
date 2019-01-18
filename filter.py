
''' Class defined as abstract and all methods must be implemented by all filters inside filters' folder
@Methods:
    - __init__(Read):
        :parameter
            - Every class must receive a Read object as param, use it to retrieve the image file, then use
            super().__init__(self.__img).
            - Every attributes must be declared here and should be private. If some attribute doesn't
            have your value already, set it to None.
        :argument
            - img: Image itself
            - width: width of the image(img)
            - height: height of the image(img)
            - min_value: min value for matrix index, coord (x,y) = (0,0) - Just to avoid magic numbers
    - def execute():
        :argument
            - Eache filter must have input("") to your specifics fields, for example: Blur Filter have radius and
            weight, inside execute must have this inputs, to be executed in execution time only.
            - Inside execute() if needed to show or save multiple images(USE Write from IO.show_write) you must pass as
            parameter only one image and filename per time.

    - def get_restrictions():
        :return
            - this method must return only one restriction, as String, following this article:
            https://stackoverflow.com/questions/32192671/pil-image-mode-i-is-grayscale. (For this test, only one
            restriction per filter is supported, just to simplify the implementation).
@Imports:
    - from filter import Filter
    - from PIL import Image
    - from IO.show_write import Write
'''

import abc


class Filter(metaclass=abc.ABCMeta):

    def __init__(self, img):
        self.img = img
        self.width, self.height = img.size
        self.min_value = 0

    @abc.abstractmethod
    def execute(self):
        return

    @abc.abstractmethod
    def get_restrictions(self):
        return
