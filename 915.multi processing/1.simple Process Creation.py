from multiprocessing import Process

def task(i:int):
    print(f"working on process {i}")
    

p1=Process(target=task,args=(1,))
p2=Process(target=task,args=(2,))

p1.start()
p2.start()

p1.join()
p2.join()


#output
```
working on process 1
working on process 2
```