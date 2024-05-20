from threading import Thread
from threading import Lock
import time

global_counter = 0

def increment_counter(x, lock):
    global global_counter
    
    lock.acquire()
    
    local_counter = global_counter
    local_counter += x
    time.sleep(0.3)
    global_counter = local_counter
    
    lock.release()
    
if __name__ == "__main__":
    lock = Lock()
    
    t1 = Thread(target=increment_counter, args=(20, lock))
    t2 = Thread(target=increment_counter, args=(70, lock))
    
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    print(global_counter)