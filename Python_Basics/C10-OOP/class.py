class programmer:
    company="Microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin

p = programmer("Nilu",10000,"z52")
print(p.name,p.salary,p.company,p.pin)