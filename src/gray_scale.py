from FilterAbc import FilterAbc


class gray_scale(FilterAbc):

    def apply_filter(*args):
        gray_scale_img = args[0].convert('L')
        return gray_scale_img
