class Value:

    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self._op = _op
        self._prev = set(_children)

    def __repr__(self):
        return f"Value(data={self.data})"

    def __add__(self, other):
        return Value(self.data + other.data, (self, other), "+")

    def __mul__(self, other):
        return Value(self.data * other.data, (self, other), "*")

a = Value(2.0)
b = Value(-3.0)
c = Value(10.0)

L = a*b + c

print(L.data)
print(L._op)
print(L._prev)