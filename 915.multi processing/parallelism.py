from multiprocessing import Process
import time

def task(i:int):
    print(f"working on process {i} on {time.time()} and about to go to waiting period")
    time.sleep(2) # Waiting period
    print(f'process {i}completed waiting period, Work done on {time.time()} ')
    
    

p1=Process(target=task,args=(1,))
p2=Process(target=task,args=(2,))

p1.start()
p2.start()

p1.join()
p2.join()

#Output 

"""
working on process 1 on 1767186404.3237941 and about to go to waiting period
working on process 2 on 1767186404.3245807 and about to go to waiting period
process 1completed waiting period, Work done on 1767186406.3240118 
process 2completed waiting period, Work done on 1767186406.324866 


"""