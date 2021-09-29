class C2dVec:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return(f"{self.icap}i + {self.jcap}j")


class C3dVec(C2dVec):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return(f"{self.icap}i + {self.jcap}j + {self.kcap}k")


print("***** 2D Vector *****")
v2d = C2dVec(int(input("Please, enter values of i: ")),
             int(input("Please, enter values of j: ")))
print(f"The 2D vector is: {v2d}")

print("***** 3D Vector *****")
v3d = C3dVec(int(input("Please, enter values of i: ")),
             int(input("Please, enter values of j: ")),
             int(input("Please, enter values of k: ")))
print(f"The 3D vector is: {v3d}")
