from multiprocessing import Process, Queue

def inc(i,q):
    q.put(f"data added with process {i}")

q=Queue()

p1=Process(target=inc, args=(1,q,))
p2=Process(target=inc,args=(2,q,))
p1.start()
p2.start()

p1.join()
p2.join()


print(q.get())
print(q.get())

