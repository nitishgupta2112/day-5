# class shoe:
#     def __init__(self,price,material):
#         self.price=price
#         self.material=material
# s1 = shoe(10000,"canvas")
# s2 = shoe(10001,"canvas")
# print("the unique ",id(s1))
# print("the unique ",id(s2))
# class shoe:
#     def __init__(self,price,material):
#         self.price=price
#         self.material=material
#     def __str__(self):
#         return "shoes with price:" + str(self.price) + " and material:" + str(self.material)
# s1= shoe(1000,"canvas")
# print(s1)    
# class mobile:
#     def __init__(self):
#         print(id(self))
#     def display(self):
#         print("Displaying details  ")
#     def purchase(self):
#         self.display()
#         print("calculating price")


# s1 = mobile()#100
# print(s1)
# s2 = mobile()#200
# s1 = s2 #s1 =200
# print(s1)
# s1.purchase()
# class mobile:
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price
#         self.total_price = None
#     def purchase(self):
#         if self.brand == "Apple":
#             discount = 10
#         else:
#             discount = 5
#         self.total_price = self.price - self.price*(discount/100)
#         print("Total price of ", self.brand,"mobile is ",self.total_price)
#     def amount_returned(self):
#         return (self .price-self.total_price)
    
# mob1 = mobile("Apple", 20000)
# mob2 = mobile("Samsung", 10000)
# mob1.purchase()
# mob2.purchase()
# print(mob1.amount_returned())
# print(mob2.amount_returned())
# class Customer:
#     def __init__(self, cust_id, name, age, wallet_balance):
#         self.cust_id = cust_id
#         self.name =name 
#         self.age= age 
#         self.__wallet_balance = wallet_balance

#     def set_balance (self, amount): 
#         if amount < 500000 and amount > 0:
#             self.__wallet_balance += amount
#     def get_wallet_balance(self):
#             return  self.__wallet_balance
# c1=Customer (100, "G", 24, 10000)
# print(c1.get_wallet_balance())
# c1.set_balance (50000)
# print(c1.get_wallet_balance())
# class Dam:

#     def __init__(self, name, length):
#         self.name=name
#         self.__length=length
#     def get_length(self):
#         return self.__length
# dam1=Dam("ABC dam", 3.5)
# print("Dam name:", dam1.name)
# print("Dam Length", dam1.get_length())
# class Table:
#     def __init__(self):
#         self.no_of_legs=4
#         self._glass_top=None 
#         self._wooden_top=None
#     def assign_data(self, glass_top, wooden_top):
#         self._glass_top=glass_top
#         self._wooden_top=wooden_top 
#     def identify_rate (self, glass_top, wooden_top):# 
#         self.assign_data(glass_top, wooden_top)
#         if(self._glass_top==True):
#              rate=20000 
#         elif (self._wooden_top==True):
#              rate=30000
#         else:
#             rate=0
#         return rate
# dining_table = Table()
# rate=dining_table.identify_rate(False, True)
# print(rate)
class Table:
    def __init__(self): 
        self.no_of_legs=4
        self.glass_top=None
        self.wooden_top=None

dining_table=Table() 
back_table=Table() #
front_table=back_table
back_table=dining_table

print(id(dining_table), id(back_table), id(front_table))