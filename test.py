import random


class M:
    def __init__(self, **kwargs) -> None:
        # 각 키를 하나하나 체크 해가지고
        self.status = kwargs


def foo(**kwargs):  # packing
    kwargs  # {'a':20,'b':10}
    return kwargs['a']+kwargs['b']


foo(b=10, a=20)

input_ = {'a': 20, 'b': 10}
foo(**input_)  # unpacking
foo(b=10, a=20)
a = M(**input_)
print(a.status)
print(input_)
input_['a'] = 30
print(a.status)
print(input_)
print(str('abc'))
