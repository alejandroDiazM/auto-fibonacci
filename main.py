#from datetime import datetime

from apscheduler.schedulers.background import BlockingScheduler

def fibonacci():
    a = 0 
    b = 1
    while(True):
        yield b
        a, b = b, a + b

obj = fibonacci()

def my_job():
    print(next(obj))
    # print(f"Job called at {datetime.now()}")

scheduler = BlockingScheduler()
scheduler.add_job(func=my_job, trigger='interval', seconds=10, id='task')
scheduler.start()
