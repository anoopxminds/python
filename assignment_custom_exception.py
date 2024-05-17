#Create a custom exception class OutofStock which will be raised in the case of stock unavailability
#Create order class with method placeOrder.If the quantity ordered is greater than available stock raise the error
#Product class will have the properties id,name,stockAvailable

class OutofStock(Exception):
    
    def __init__(self, message):
        self.message = message;
        super().__init__(self.message)
        
    def __str__(self):
        return f"{self.message}"
    
class Order(OutofStock):
    
    def __init__(self, message):
        super().__init__(message)
    
    def placeOrder():
        total_quantity = 10
        request_quatity = int(input("Enter quantity : "))
        try:
            
            if (total_quantity >= request_quatity):
                print(f"Stock is available.")
            else:
                raise OutofStock("Out of stock..!")
        except OutofStock as e :
            
            print(f" Error is : {e}")
    
class Product(Order):
    def __init__(self, id, name, stockAvailable):
        self.id = id
        self.name = name
        self.stockAvailable = stockAvailable
        
        
order = Order        
order.placeOrder()
    
