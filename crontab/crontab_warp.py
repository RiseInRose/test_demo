# coding:utf-8
# author caturbhuja
# date   2019/8/9 10:12 AM 
# wechat chending2012 
"""
直接使用python调度程序

"""

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import os

scheduler = BlockingScheduler()

# cron
task_list = """
*/10 * * * * cd /data/monitor/admin && sh ./start_service.sh log
*/30 * * * * cd /data/monitor/admin && sh ./start_service.sh redis
0 4 * * * cd /data/monitor/admin && sh ./start_service.sh table   
"""

task_list2 = """
* * * * * cd /Users/caturbhuja/datagrand/cmb_all/cmb/shouye8.0/code/monitor/src && sh test.sh
"""


def action_cmd(cmd):
    os.system(cmd)


def add_task(task_lists):
    for task in task_lists.split('\n'):
        if task.strip():
            tmp = task.strip().split(' ')
            cmd_tmp = ' '.join(tmp[5:])
            cron_time = ' '.join(tmp[:5])
            scheduler.add_job(action_cmd, CronTrigger.from_crontab(cron_time), args=(cmd_tmp, ))


add_task(task_list2)
scheduler.start()

# 还可以把这个放到多进程中处理。
