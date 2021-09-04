class Calc:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def result(self):
        return self.num1*self.num2

a=Calc(2,5)
final=a.result()
print("the final value of the product",final)