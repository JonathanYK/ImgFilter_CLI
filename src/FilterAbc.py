from abc import ABC, abstractmethod


class FilterAbc(ABC):

    @abstractmethod
    def apply_filter(*args):
        """Applying the desired filter"""
        pass

