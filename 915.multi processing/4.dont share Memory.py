from multiprocessing import Process
import time


lst=[0]
def task(i:int,j:int):
    
    lst.append(j)
    print(f"Process {i} appended {j} in to lst and lst :{lst}")
    
    
    

p1=Process(target=task,args=(1,100))
p2=Process(target=task,args=(2,200))

p1.start()
p2.start()

p1.join()
p2.join()
print(lst)
#Output 

"""
Process 1 appended 100 in to lst and lst :[0, 100]
Process 2 appended 200 in to lst and lst :[0, 200]
[0]


"""