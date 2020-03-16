# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 20:55
# @Author  : davieyang
# @Email   : davieyang@qq.com
# @File    : demo_leadscloud.py
# @Project: PerformanceLocust
from locust import HttpLocust, TaskSet, task
import urllib3


class LeadsCloud(TaskSet):

    '''继承TaskSet类，用于描述用户行为'''

    urllib3.disable_warnings(InterruptedError)
    @task
    def open_leads_cloud(self):
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"}
        r = self.client.get("/#/login", headers=header, verify=False)
        print(r.status_code)
        assert r.status_code == 200

    @task  # 使用@task装饰该方法为一个事务
    def login_leads_cloud(self):
        self.client.post("https://admin-end.leadscloud.com/cuss-login/login", {
            "username": "yangdawei_10110", "password": "111111"}, verify=False)
        r = self.client.get("/#/login", verify=False)
        print(r.status_code)
        assert r.status_code == 200


class WebsiteUser(HttpLocust):
    task_set = LeadsCloud  # 指向一个定义的用户行为类
    min_wait = 3000  # 执行事务之间用户等待时间的下限
    max_wait = 6000  # 执行事务之间用户等待时间的上限


if __name__ == '__main__':
    import os
    #  启动命令，-f表示指定测试脚本文件 --host被测系统的URL
    os.system("locust -f Leadscloud.py --host=https://admin.leadscloud.com/Front-Vue")

