class Value:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Value(data={self.data})"

    def __add__(self, other):
        return self.data + other.data

test_1 = Value(2.0)
test_2 = Value(3.0)
print(test_1 + test_2)
