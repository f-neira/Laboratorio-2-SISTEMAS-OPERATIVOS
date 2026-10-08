import threading,time
a=threading.Lock(); b=threading.Lock()
def uno():
    with a:
        time.sleep(.5)
        with b: print("uno")
def dos():
    with b:
        time.sleep(.5)
        with a: print("dos")
t1=threading.Thread(target=uno); t2=threading.Thread(target=dos)
t1.start(); t2.start(); t1.join(); t2.join()
