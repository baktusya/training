import sys
import inspect
from pprint import pprint
import time

def introspection_info(obj):
    info = {}

    star_time = time.time()
    info['type'] = type(obj).__name__
    time.sleep(0.2)
    info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    time.sleep(0.2)
    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    time.sleep(0.2)
    info['module'] = inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else None
    time.sleep(0.2)
    info['size'] = sys.getsizeof(obj)
    time.sleep(0.2)
    end_time = time.time()
    info['time introspection'] = end_time - star_time

    return info

class Example:
    def __init__(self):
        self.attr1 = 10
        self.attr2 = 20

    def method1(self):
        pass

    def method2(self):
        pass

example_obj = Example()
info = introspection_info(example_obj)
pprint(info)

number_info = introspection_info(42)
pprint(number_info)

