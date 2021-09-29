class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str = ""
        index = 0
        for i in self.vec:
            str += f"{i}a{index} + "
            index += 1
        return str[:-2]

    def __add__(self, vec2):
        newList = []
        if (len(v1) == len(v2)):
            for i in range(len(self.vec)):
                newList.append(self.vec[i] + vec2.vec[i])
        else:
            print("Lengths are not equal, hence addition is not possible...")
        return Vector(newList)

    def __mul__(self, vec2):
        sum = 0
        if (len(v1) == len(v2)):
            for i in range(len(self.vec)):
                sum += self.vec[i] * vec2.vec[i]
        else:
            print("Lengths are not equal, hence multiplication is not possible...")
        return sum

    def __len__(self):
        return len(self.vec)


v1 = Vector([1, 4, 8])
v2 = Vector([1, 9, 0])
print(len(v1))
print(len(v2))
print(v1+v2)
print(v1*v2)
