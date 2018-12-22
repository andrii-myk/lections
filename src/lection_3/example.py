class A():
    a = 1

class B():
    a = 2

class C(A, B):
    def l(self):
        print(self.a)

c = C()
c.l()
