#Understanding Condition Variables in Python for Thread Synchronization
import threading

shared_resorces = []

condition = threading.Condition()

def consumer():
    with condition:
        while not shared_resorces:
            print('Waiting for shared resourses')
            condition.wait(0.3)
            item = shared_resorces.pop(0)
            print('Consumer consumed item :', item)
            
def producer():
    with condition:
        item = 'New Item'
        shared_resorces.append(item)
        print('Producer produced item :', item)
        condition.notify()

t1 = threading.Thread(target=consumer)
t2 = threading.Thread(target=producer)

t1.start()
t2.start()            
