import time
import threading
# 使用threading 模块创建线程
import queue
# 优先级队列模块

exitFlag = 0

class myThread(threading.Thread):       # 线程类
    def __init__(self,threadID,threadName,count):       # 类初始化方法 threadID、threadName、计数
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.threadName = threadName
        self.count = count

    def run(self):
        print("开始线程："+self.threadName)
        print_time(self.threadName,self.count,5)      # 执行print_time方法，线程名、延迟时间、次数
        print("退出线程："+self.threadName)

def print_time(threadName,delay,count):     # print_time方法
    while count:                # count非0执行循环
        # 这个if作用是一个开关
        if exitFlag:            # exitFlag为0不执行，非0时执行
            threadName.exit()   # 对应名称线程退出
        time.sleep(delay)       # 休息几秒
        print("%s: %s" %(threadName,time.ctime(time.time())))       # 打印线程名—线程时间
        count -=1               # count计数-1

# 创建新线程
thread1 = myThread(1,"Thread-1",1)
thread2 = myThread(2,"Thread-2",2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出主线程")