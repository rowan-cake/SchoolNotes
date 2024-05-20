class Cuboid:
    # Attruibutes + Constuctor
    def __init__(self,length=1,width=1,height=1,color="White"):
        self.length = length
        self.width = width
        self.height = height
        self.color = color
    
    @classmethod
    def default(cls):
        return cls()
    
    #METHODS

    def getColor(self):
        return self.color
    def getVolume(self):
        volume = self.length*self.width*self.height
        return volume
    def getSurfaceArea(self):
        return 2*(self.length*self.width+self.length*self.height+self.width*self.height)
    def displayInfo(self):
        print("Color = ",self.color)
        print("Length: %f,Width: %f,Height: %f" % (self.length,self.width,self.height))
        print("Surface Area:",self.getSurfaceArea())
        print("Volume = ",self.getVolume())
        return ""


class BankAccount:
    # Attributes and Constuctors
    count = 0
    def __init__(self,balance = 0,annualIntrestRate=0,beneficis=None):
        self.balance = balance
        self.annualIntrestRate = annualIntrestRate
        if beneficis is None:
            self.beneficis = []
        self.setBenifiecs(self,beneficis) 
        BankAccount.count+=1
        self.id = BankAccount.count

    @classmethod
    def default(cls):
        return cls() 
    
    # Getters and Setters
    def getBalance(self):
        return self.balance
    def getInterestRate(self):
        return self.annualIntrestRate
    def getBenifieces(self):
        return self.beneficis
    
    @staticmethod
    def setBenifiecs(self,list):
        self.beneficis = list
    
    def getMonthlyIntrest(self):
        return self.annualIntrestRate/12
    
    def  getNumberOfBenefitieries(self):
        list = self.getBenifieces()
        return len(list)
    
    
    # Mehtods
    def withdraw(self,ammount):
        self.balance-=ammount
    def depoist(self,amount):
        self.balance+=amount
    def displayInfo(self):
        print("Acount ID: ",self.id)
        print("Current Balance: ", self.getBalance())
        print("Annual intrest rate: ", self.getInterestRate())
        print("Monthly intrest rate: ", self.getMonthlyIntrest())
        monthlyIntrest = self.getBalance()*(self.getMonthlyIntrest()/100)
        print("Monthly intrest: ",monthlyIntrest)
        print("%d beniifeacrs: %s " %(self.getNumberOfBenefitieries(),self.getBenifieces()))
        return ""




if __name__ == "__main__":
    cube1 = Cuboid()
    cube2 = Cuboid(8,3.5,5.9)
    print("Cube 1")
    cube1.displayInfo()
    print()
    print("Cube 2")
    cube2.displayInfo()
    print("------------- \nQ2:")

    acount = BankAccount(33000,6.7,["John","Lilli"])
    acount.withdraw(1500)
    acount.depoist(1000)
    acount.displayInfo()


