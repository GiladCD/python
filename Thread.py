import threading

count = 0
lock = threading.Lock()

def thread1():
    global count
    for i in range(100000):
        with lock:
            count += 1
            

def thread2():
    global count
    for i in range(100000):
        with lock:
            count -= 1
            

thr1 = threading.Thread(target=thread1)
thr2 = threading.Thread(target=thread2)

thr1.start()
thr2.start()

thr1.join()
thr2.join()

print("Final count:", count)