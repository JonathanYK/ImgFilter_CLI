import string
from PIL import Image

from src.FilterAbc import filter_abc


class RotateFilter(filter_abc):



    def params_validation(self):
        if self.img_name is None:
            self.img_name = "input.png"
        if self.output_path is None:
            self.img_name = "rotated.png"
        if self.rotate_degrees is None:
            self.rotate_degrees = 45


    def rotate(self, img_name: string = None, output_path: string = None, rotate_degrees: int = None) -> bool:
        self.params_validation(img_name, output_path, rotate_degrees)



        main_img = Image.open(img_name)

        rotated = main_img.rotate(rotate_degrees)
        rotated.save(output_path)


    rotate("input.png", "rotated.png", 15)
