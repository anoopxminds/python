#Find area of square,rectangle,triangle by implementing method overloading

class Area:
    def Find_area(self, a = None, b = None, c= None):
        if a != None and b != None and c == "rectangle" :
            print(f"Area of a rectangle : {a*b}")
        elif a != None and b != None and c == "triangle" :
            print(f"Area of a triangle : {a*b/2}")
        elif a != None and c == "square":
            print(f"Area of a Sqaure : {a*a}")
            
area = Area()
area.Find_area(10, 20, "rectangle")
area.Find_area(5, 15, "triangle")
area.Find_area(15, None, "square")
        
        