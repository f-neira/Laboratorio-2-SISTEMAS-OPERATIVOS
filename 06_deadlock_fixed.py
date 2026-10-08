import threading,time
a=threading.Lock(); b=threading.Lock()
def worker(name):
    with a:
        time.sleep(.2)
        with b: print(name,"completo")
ts=[threading.Thread(target=worker,args=(x,)) for x in ("uno","dos")]
for t in ts:t.start()
for t in ts:t.join()
