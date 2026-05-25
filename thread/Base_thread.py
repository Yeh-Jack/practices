import threading
import time

import datetime


def job(seq):
    print(f"Thread {str(seq)} is working, wait for {seq*2} seconds ...")
    time.sleep(seq * 2)


# 建立子執行緒
child1 = threading.Thread(target=job, args=(1,))
child2 = threading.Thread(target=job, args=(2,))
child3 = threading.Thread(target=job, args=(3,))

# 執行子執行緒
child1.start()
child2.start()
child3.start()

# 主執行緒繼續執行自己的工作
print("Main thread: wait for doughter threads ending ...")

# 等待子執行緒結束
child1.join()
print("Thread 1 completed.")
child2.join()
print("Thread 2 completed.")
child3.join()
print("Thread 3 completed.")

print("Done.")
