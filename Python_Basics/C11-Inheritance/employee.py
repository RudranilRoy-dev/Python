class employee:
    salary = 200
    increment = 10
    @property
    def afterincrement(self):
        return (self.salary + self.salary *(self.increment/100))
    
e = employee()
print(e.afterincrement)