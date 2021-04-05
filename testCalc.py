import myCalc 
class Calc():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print(a)
        print(b)

    def add(self,a,b):
        return myCalc.lib.add(a,b)

    def subtraction(self , a,b):
        return myCalc.lib.sub(a,b)
     
    def multiplication(self, a,b):
        return myCalc.lib.multiply(a,b)
         
    def division(self,a,b):
        return myCalc.lib.divide(a,b)

if __name__ == "__main__":
    obj = Calc(12,3)
    print("Addition is : " , obj.add(12,3))
    print("Subtraction is : ", obj.subtraction(12,3))
    print("Multiplication is : ", obj.multiplication(12,3))
    print("Division is : ", obj.division(12,3))