#스케쥴러
#pip install apscheduler
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
#실행함수
def exec_interval():
    print('interval')
    print(datetime.datetime.now())



def exec_cron():
    print('cron')
    print(datetime.datetime.now())
sched = BlockingScheduler()
#interval 잡 등록
sched.add_job(exec_interval, 'interval', seconds=10)
#cron job 등록
sched.add_job(exec_cron, 'cron', hour=10, minute=40)
# 시작
sched.start()
