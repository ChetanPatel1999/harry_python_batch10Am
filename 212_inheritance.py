class A:
    def m1(self):
        print("m1 method of A class")


class B(A):
    def m2(self):
        print("m2 method of B class")


b1=B()
b1.m1()
b1.m2()