from PIL import Image

from FilterAbc import FilterAbc


class overlay(FilterAbc):

    def apply_filter(*args):
        over_img = args[1][0]

        if not over_img:
            return False

        with Image.open('{}'.format(over_img)) as over_img:
            args[0].paste(over_img.convert("RGBA"), (0, 0))

        return args[0]