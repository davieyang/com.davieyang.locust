# encoding = utf-8
'''
@Time    : 2018/9/14 10:42
@Author  : 
@Email   : davieyang@qq.com
@File    : AccessPaaSWebSite.py
@Software: PyCharm
@Description:
'''
from locust import HttpLocust, TaskSet, task

class PaaSWebSite(TaskSet):
    ''' 浏览PaaS平台'''
    @task
    def open_paas(self):
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"}
        r = self.client.get("/", headers = header, verify= False)
        print(r.status_code)
        assert r.status_code == 200

class WebsiteUser(HttpLocust):
    task_set = PaaSWebSite
    min_wait = 3000
    max_wait = 6000


if __name__=='__main__':
    import os
    os.system("locust -f AccessPaaSWebSite.py --host=http://paasweb.tpaas.youedata.com")