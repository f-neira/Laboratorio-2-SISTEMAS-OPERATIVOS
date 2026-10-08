import threading, time
def worker(n):
    total=0
    for i in range(2_000_000):
        total += (i % 7)
    print(f"thread {n}: {total}")
threads=[threading.Thread(target=worker,args=(i,)) for i in range(4)]
for t in threads: t.start()
for t in threads: t.join()
print("fin")
