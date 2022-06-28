import abc


class A(abc.ABC):
    @abc.abstractmethod
    def must_be_implemented(self):
        return

# Another way to declare an abstract is given below:
class D:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def must_be_implemented(self):
        return


class B(A):
    def must_be_implemented(self):
        print("Hello")
        pass


class C(D):
    @abc.abstractmethod
    def must_be_implemented(self):
        return
