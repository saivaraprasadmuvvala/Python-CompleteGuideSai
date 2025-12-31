from multiprocessing import Process,Value
import time

bal=Value('i',200)
def task(amount):
    if bal.value>amount:
        print(f'withdrawing {amount}')
        time.sleep(1)
        bal.value-=amount
        print(f'withdraw success and balance is {bal.value}')

p1=Process(target=task,args=(100,)) 
p2=Process(target=task,args=(150,))        
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


    