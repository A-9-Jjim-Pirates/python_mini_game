class M:
    def __init__(self, a) -> None:
        self.a = a


a = M(10)
print(a.__class__.__name__)
