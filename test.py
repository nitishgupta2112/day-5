class Mobile: 
    def init_(self, brand, price): #
        self.brand= brand
        self.price =price 
        self.total_price =None
    def purchase(self):
        if self.brand =="Apple":
            discount = 10
        else:
            discount =5
        self.total_price = self.price- self.price*(discount/ 100)
        print("Total price of", self.brand, "mobile is",self.total_price)
mob1 = Mobile("Apple",20000) 
mob1.purchase()