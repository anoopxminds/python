import threading 
from threading import *
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
#calc_square(arr)
#calc_cube(arr)

thread1 = threading.Thread(target=calc_square, args=(arr,))
thread2 = threading.Thread(target=calc_cube, args=(arr,))

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print('Total time taken by thread is ', time.time() - t1)      

