class A():
    def a (self):
        print('1')



class B(A):
    def a(self):
        super(B, self).a()


b = B()
b.a()
#print(b())
print(B())