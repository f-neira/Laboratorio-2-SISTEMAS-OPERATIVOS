import threading,time,random
sem=threading.Semaphore(2)
def worker(i):
    with sem:
        print("entra",i)
        time.sleep(random.uniform(.2,.8))
        print("sale",i)
threads=[threading.Thread(target=worker,args=(i,)) for i in range(6)]
for t in threads:t.start()
for t in threads:t.join()
