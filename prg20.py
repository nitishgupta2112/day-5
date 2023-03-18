#day4
class wecare:
    def __init__(self,vehicle_id, type,cost):
        self.__vehicle_id = vehicle_id
        self.__type = type
        self.__cost = cost
        
    def calculate(self):
        if self.__type =="Two Wheeler" :
            premium_amount = self.__cost*0.02
            print("the vehicle id is ",self.__vehicle_id,"and the vehicle cost is",self.__cost,
                  "the type of vehicle type", self.__type,"premium amount is ",premium_amount)
        elif self.__type=="Four Wheeler":
            premium_amount = self.__cost*0.06
            print("the vehicle id is ",self.__vehicle_id,"and the vehicle cost is",self.__cost,
                  "the type of vehicle type", self.__type,"premium amount is ",premium_amount)
    def get_premium_amount(self):
        if self.__type =="Two Wheeler" :
            return self.__cost*0.02
        elif self.__type=="Four Wheeler":
            return self.__cost*0.06


obj=wecare(124,"Four Wheeler",50000)
obj.calculate()
print(obj.get_premium_amount())
