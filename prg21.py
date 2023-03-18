class student:
    def __init__(self,student_id,age,marks):
        self.__student_id=student_id
        self.__age=age
        self.__marks=marks
    
    def validate_marks(self):
        if self.__marks<=100 and self.__marks>=0:
            return True
        else:
            return False
    def validate_age(self):
        if self.__age>20:
            return True
        else:
            return False
    def check_qualification(self):
        if (self.validate_marks() == True) and (self.validate_age() == True):
            if(self.__marks >= 65):
                self.fees()
            else:
                return False
    def fees(self):
        dic={"Course 1001":25575.0,"Course 1002":15500.0}
        
        if self.get_marks()>=85:
            c= input()
            fee=0
            if(c=="Course 1001"):
                fee=dic["Course 1001"]*0.25
                print("The fees need to pay is :",fee)
                print("  You are allowed to join")
        else:
            print(" You are not allowed to join")
        
    def set_marks(self,marks):
        self.__marks=marks
    
    def get_marks(self):
        return self.__marks
        
    def set_age(self,age):
        self.__age=age
        
    def get_age(self):
        return self.__age
        
        
s1=student(12,28,89)
print(s1.check_qualification())
