import thread
import time

def calc_square(num):
    print('Calculate the square root of the given number :')
    for n in num:
        time.sleep(0.3)
        print('Print square :', n*n)
    
def calc_cube(num):
    print('Calculate the cube of  the given number :')
    for n in num:
        time.sleep(0.3)
        print('Print cube :', n*n*n)
        
arr = [4,5,6,2]

t1 = time.time()
calc_square(arr)
calc_cube(arr)

print('Total time taken by thread is ', time.time() - t1)        