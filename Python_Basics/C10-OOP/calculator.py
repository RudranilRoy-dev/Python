class Calculator:

    @staticmethod
    def greet():
        print(" hello user!")

    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"The square of {self.n}: {self.n*self.n}")

    def cube(self):
        print(f"The cube of {self.n}: {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot of {self.n}: {self.n**1/2}")

p=Calculator(4)
p.greet()
p.square()
p.cube()
p.squareroot()

q=Calculator(8)
q.greet()
q.square()
q.cube()
q.squareroot() 