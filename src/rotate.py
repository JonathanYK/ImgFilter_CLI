from FilterAbc import FilterAbc


class rotate(FilterAbc):

    def apply_filter(*args):
        if not args[1]:
            degrees = 45
        else:
            degrees = args[1][0]

        return args[0].rotate(int(degrees))

