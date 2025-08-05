from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def __add__(cls, *args, **kwargs):
        pass