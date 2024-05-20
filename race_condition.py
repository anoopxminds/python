from threading import Thread
import time

global_counter = 0

def increment_counter(x):
    global global_counter
    
    local_counter = global_counter
    local_counter += x
    time.sleep(0.3)
    global_counter = local_counter
    
if __name__ == "__main__":
    
    t1 = Thread(target=increment_counter, args=(20,))
    t2 = Thread(target=increment_counter, args=(70,))
    
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    print(global_counter)

    
    
    