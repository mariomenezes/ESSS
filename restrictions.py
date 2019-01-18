# https://stackoverflow.com/questions/32192671/pil-image-mode-i-is-grayscale

# Adicionar

class Restrictions:

    def configure_restrictions(self):
        self.__dict_restrictions = {'RGB': "P"}

    def get_restrictions(self):
        return self.__dict_restrictions
