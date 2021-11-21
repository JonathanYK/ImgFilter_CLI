from abc import ABC, abstractmethod


class FilterAbc(ABC):

    def __init__(self):
        self.img_name = None
        self.output_path = None
        self.rotate_degrees = 45

    @abstractmethod
    def params_validation(self, img_name=None, output_path=None, rotate_degrees=None) -> bool:
        pass
