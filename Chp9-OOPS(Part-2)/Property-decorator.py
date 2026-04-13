class student:
    def __init__(self,chem,eng,phy):
        self.chem = chem
        self.eng = eng
        self.phy = phy


    @property
    def percentage(self):
        return str((self.chem + self.eng + self.phy)/3) + "%"


std1 = student(87,90,67)
print(std1.percentage)

std1.phy = 60
std1.chem = 89
print(std1.percentage)
