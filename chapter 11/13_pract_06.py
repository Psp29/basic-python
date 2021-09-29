class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[0]}j + {self.vec[0]}k"


v1 = Vector([1, 4, 9])
v2 = Vector([1, 9, 6])
print(v1)
