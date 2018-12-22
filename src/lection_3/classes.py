class Simple():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"Class Simple has values: {self.a}, {self.b}"

    def __repr__(self):
        return f"Representation of the class Simple"

s = Simple(10, 20)
print("Stasdas {}".format(s))