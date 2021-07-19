class A:
    def method_a(self):
        print("this is method a")

    def my_class(self):
        print("I am Class A!")


class B(A):
    def method_b(self):
        print("this is method b")

    def my_class(self):
        print("I am class B!")


class c(B):
    def method_c(self):
        print("this is method c")

    def my_class(self):
        print("I am class C!")

c = c()
c.method_a()
c.method_b()
c.method_c()
c.my_class()