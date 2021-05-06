import multiprocessing as mp
import time


# 멀티프로세싱 모듈
def worker():
    proc = mp.current_process()
    print(proc.name)
    print(proc.pid)
    time.sleep(5)
    print("SubProcess End")

if __name__=="__main__":
    # main process
    proc = mp.current_process()
    print(proc.name)
    print(proc.pid)

    # process spawning
    p = mp.Process(name="SubProcess", target=worker)
    p.start()

    print("MainProcess End")