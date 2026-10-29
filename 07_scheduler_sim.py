from collections import deque
jobs=[{"id":"P1","arrival":0,"burst":8,"priority":1},
      {"id":"P2","arrival":0,"burst":4,"priority":3},
      {"id":"P3","arrival":0,"burst":2,"priority":2}]
def report(order):
    t=0; waits={}; turns={}
    for p in order:
        waits[p["id"]]=t-p["arrival"]
        t+=p["burst"]; turns[p["id"]]=t-p["arrival"]
    print("orden:",[p["id"] for p in order])
    print("waiting:",waits,"prom:",sum(waits.values())/len(waits))
    print("turnaround:",turns,"prom:",sum(turns.values())/len(turns))
print("FCFS"); report(jobs)
print("\nSJF"); report(sorted(jobs,key=lambda x:x["burst"]))
print("\nPRIORITY (menor=mayor prioridad)"); report(sorted(jobs,key=lambda x:x["priority"]))
print("\nRR q=2 (timeline)")
q=2; rem={p["id"]:p["burst"] for p in jobs}; queue=deque(p["id"] for p in jobs); timeline=[]
while queue:
    pid=queue.popleft(); run=min(q,rem[pid]); timeline += [pid]*run; rem[pid]-=run
    if rem[pid]>0: queue.append(pid)
print(timeline)
