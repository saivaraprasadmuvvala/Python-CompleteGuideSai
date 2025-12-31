from multiprocessing import Process

def square(n):
    print(n * n)

if __name__ == "__main__":
    processes = []
    for i in [1, 2, 3, 4]:
        p = Process(target=square, args=(i,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
        
"""
1
4
9
16
"""
