from multiprocessing import Process,Lock
import time

lock=Lock()

def task(i):
    with lock:
        print(f'Task is started from process {i}')
        time.sleep(1)
        print(f'Task completed by Process {i}')

p1=Process(target=task,args=(1,)) 
p2=Process(target=task,args=(2,))        
p1.start()
p2.start()

p1.join()
p2.join()


'''
Task is started from process 1
Task completed by Process 1
Task is started from process 2
Task completed by Process 2

'''


    