import threading, time
counter=0
def worker():
    global counter
    for _ in range(10000):
        tmp=counter
        time.sleep(0)
        counter=tmp+1
threads=[threading.Thread(target=worker) for _ in range(4)]
for t in threads:t.start()
for t in threads:t.join()
print("esperado:",40000,"obtenido:",counter)
