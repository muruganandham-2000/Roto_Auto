class MS:
    def hehe(self,A,B):
        C=A+B
        return C
    

sum=MS()
print(sum.hehe(10,20))

class Jolly:
    def __init__(self,A,B):
        self.A,self.B=A,B

    def sum(self):
        C=self.A+self.B
        return C

result=Jolly(10,20)
print(result.sum())

        