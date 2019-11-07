# encoding = utf-8
from locust import HttpLocust, TaskSet, task
import urllib3


class LeadsCloud(TaskSet):

    urllib3.disable_warnings()
    @task
    def open_leads_cloud(self):
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"}
        r = self.client.get("/#/login", headers=header, verify=False)
        print(r.status_code)
        assert r.status_code == 200

    @task
    def login_leads_cloud(self):
        self.client.post("https://cnend.leadscloud.com/cuss-login/login", {
            "username": "yangdawei_10110", "password": "111111"}, verify=False)
        r = self.client.get("/#/login", verify=False)
        print(r.status_code)
        assert r.status_code == 200


class WebsiteUser(HttpLocust):
    task_set = LeadsCloud
    min_wait = 3000
    max_wait = 6000


if __name__ == '__main__':
    import os
    os.system("locust -f D:\PythonPrograms\PerformanceLocust\LeadsCloud\Leadscloud.py --host=https://admin.leadscloud.com/Front-Vue")
