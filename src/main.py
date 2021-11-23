import sys
from PIL import Image


if __name__ == "__main__":

    input_scr = sys.argv[1]

    # for easier debug:
    # input_scr = "input.jpg-output.png gray_scale rotate overlay=python.png rotate=20 rotate overlay=python.png rotate=90"

    # extracting source and destination paths from global parameter:
    src_img = Image.open('{}'.format(input_scr.split(' ', 1)[0].split("-")[0]))
    dst_img_name = input_scr.split(' ', 1)[0].split("-")[1]

    # cutting src_img and dst_img_name from input_scr
    input_scr = input_scr.split(' ', 1)[1]


    # iterating on each filter in input_scr:
    for filter in input_scr.split(" "):

        filter_params = filter.split("=")
        module = __import__(filter_params[0])

        # executing desired filter according to filter name:
        src_img = getattr(getattr(module, filter_params.pop(0)), "apply_filter")(src_img, filter_params)

    # saving image on main project dir with dst_img_name:
    src_img.save('{}'.format(dst_img_name))

