from multiprocessing import Process, Value

def inc(x):
    x.value+=1

x=Value('i', 0)

p1=Process(target=inc, args=(x,))
p2=Process(target=inc,args=(x,))
p1.start()
p2.start()

p1.join()
p2.join()


print(x.value)
