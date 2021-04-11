class employee:
    raise_amt=1.04
    def __init__(self,first,last,empid,pay):
        n=int(input("enter number of employees"))
        for i in range(0,n):
            self.first=input("first name")
            self.last=input("last name")
            self.empid=input("empid")
            self.pay=int(input("pay"))
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)
        return self.pay
    def display_details(self):
        print("name is:",self.first,self.last)
        print("Id is :",self.empid)
        print("amount:",self.pay)
class developer(employee):
    raise_amt=1.05
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)
        return self.pay
class manager(employee):
    raise_amt=1.06
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)
        return self.pay

emp1=manager("first","last","empid","pay")
emp2=developer("first","last","empid","pay")
while True:
    print("1-for manager details")
    print("2-for developer details")
    ch=int(input("enter your choice"))
    if ch==1:
        print(emp1.pay)
        emp1.apply_raise()
        print(emp1.display_details())
    elif ch==2:
        print(emp2.pay)
        emp2.apply_raise()
        print(emp2.display_details())
    else:
        print("invalid choice")
        break
        
