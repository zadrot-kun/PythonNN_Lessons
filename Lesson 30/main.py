
class F():
    attr3 = 2000

class C():
    attr1 = 400
    attr3 = 1000


class E(C):
    pass

class D():
    attr2 = 950

class B(E):
    attr2 = 150

class A(D, B):
    attr1 = 100

obj1 = A()
obj2 = A()
obj3 = A()


obj1.attr1 = 200
obj3.attr2 = 250
A.attr1 = 500

print('obj1.attr1 = ', obj1.attr1)
print('obj2.attr1 = ', obj2.attr1)
print('obj3.attr1 = ', obj3.attr1)
print('B.attr1 = ', B.attr1)
print('-'*100)
print('obj1.attr2 = ', obj1.attr2)
print('obj2.attr2 = ', obj2.attr2)
print('obj3.attr2 = ', obj3.attr2)
print('A.attr2 = ', A.attr2)
print('B.attr2 = ', B.attr2)
print('-'*100)
print('obj1.attr3 = ', obj1.attr3)
print('obj2.attr3 = ', obj2.attr3)
print('obj3.attr3 = ', obj3.attr3)