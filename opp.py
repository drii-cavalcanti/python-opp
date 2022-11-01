# Process Abstraction
# we use sorted function without knowing what is behind

# Data Abstraction
# string, float, int, user data type

# collection of attributes
from unicodedata import name


class Class:

    # shared state
    _shared_state = []

    @classmethod
    def _classmethod(cls, obj):
        cls._shared_state.append(obj)
        print(cls._shared_state)
    
    @staticmethod
    def _staticmethod():
        print('nothing to do with the class')
    
    # initial method
    def __init__(self) -> None:
        # initial object state
        self._initial_state = []
    
    # object/instance method
    def _method(self, obj):
        self._initial_state.append(obj)
        print(self._initial_state)


class Client:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname
        # obj = Client(John Carl)
        # if obj.name = 10, full name = 'John Carl'
        self.name = f'{name} {surname}'

    def get_full_name(self):
        # obj = Client(John Carl)
        # if obj.name = 10, full name = '10 Carl'
        # But get_full_name = 10, get_full_name = 10
        return f'{self.name} {self.surname}'
    
class Rectangule:
    def __init__(self, height, width) -> None:
        self.h = height
        self.w = width

    @property
    def area(self):
        return self.h * self.w
