import os
import sys
from filter import Filter
from filters import rgb
from filters import blur
from IO.read import Read


def import_class(class_string):

    """Returns class object specified by a string.

    Args:
        class_string: The string representing a class.

    Raises:
        ValueError if module part of the class is not specified.
    """

    module_name, _, class_name = class_string.rpartition('./filters')
    if module_name == '':
        raise ValueError('Class name must contain module part.')
    return getattr(
        __import__(module_name, globals(), locals(), [class_name], -1),
        class_name)


def get_class( kls ):

    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = __import__( module )
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m


def concat(str1, str2):
    return str(str1)+str2


def str_to_class(str_temp):
    return getattr(sys.modules[__name__], str_temp)


def instantiate_filters(path_to_filters_folder):
    files = os.listdir(path_to_filters_folder)
    class_list = []
    for file in files:
        if(".py" in file):
            class_list.append(file)

    ret = [file[:-3] for file in class_list ]
    # return filters name
    return (ret)


def call_func(func, dispatcher):
    try:
        return dispatcher[func].execute()
    except RuntimeError:
        print("Error in method - check implementation")


def main():

    print("This is an Image App\n")
    print("Available Filters:")

    _read = Read(sys.argv)

    # create list of filters based on classes that extend from Filter class
    keys = [str(n+1) for n in range(0, len(Filter.__subclasses__()))]
    values = [str.lower(cls.__name__) for cls in Filter.__subclasses__()]
    dispatcher = dict(zip(keys, values))

    # .copy() is needed because without it when "dicpatcher" change, "disp" changes too
    disp = dispatcher.copy()

    # Reading all filters, creating instances dynamically and checking the restrictions
    for key, value in disp.items():
        module_name = disp[key]
        _module = str_to_class(disp[key])
        class_name = str.capitalize(module_name)
        # if one filter has restrictions with input image, it will be dropped from dict(dispatcher var)
        if(getattr(_module, class_name)(_read).get_restrictions() is _read.get_img_mode()):
            try:
                dispatcher.pop(key)
            except KeyError:
                print("Key not found")

    # printing the available filters after remove the filters with restrictions with image.mode
    for key, value in dispatcher.items():
        print(key, ". ", value)

    # read from input and setting the filter num
    filter_num = input("Type the selected filter number:")
    _read.set_func(filter_num)

    # creating the instance selected and execute the filter, everything dynamically
    try:
        module_name = dispatcher[_read.get_func()]
        _module = str_to_class(dispatcher[_read.get_func()])
        class_name = str.capitalize(module_name)
        getattr(_module, class_name)(_read).execute()
        #new_imgs = temp_obj.execute()
        #temp_obj.save_img()
        print("\nImage file processed successfully!")
    except KeyError:
        print("\nInvalid Option!")


if __name__ == '__main__':
    main()




