#example of a generator function that produces a sequence of numbers

def my_generates(n):
    
    value = 0
    
    while value < n:
        
        yield value
        
        value += 1
        
for value in my_generates(3):
    
    print(value)
    
    