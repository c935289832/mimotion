import hashlib
import random
import time
from datetime import datetime
from urllib.parse import urlencode
import pytz

import os
import time

import requests

# 获取北京时间
def get_beijing_time():
    target_timezone = pytz.timezone('Asia/Shanghai')
    # 获取当前时间
    return datetime.now().astimezone(target_timezone)

def execute():
    name = users.split('#')
    pwd = passwords
    content = ""
    
    for s in name:
        try:
            step = 20000 + int(random.random() * 10000)
            url = "http://precious.losts.top/sport.php?user="
            url += s + "&password=" + pwd + "&step=" + str(step)
            result = requests.get(url).text
            content += result
            print("content", content)
        except Exception as e:
            print("error", e)
    
    try:
        pushUrl = "https://www.pushplus.plus/send/"
        token = "f8d4de22c93341729dc08c3e9dd79636"
        title = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " 刷步数通知"
        data = {
            "token": PUSH_PLUS_TOKEN,
            "title": title,
            "content": content,
            "template": "html",
            "channel": "wechat"
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        result = requests.post(pushUrl, data=urlencode(data), headers=headers).text
        print(result)
    except Exception as e:
        print("error", e)

if __name__ == "__main__":
    # 北京时间
    time_bj = get_beijing_time()
    if os.environ.__contains__("CONFIG") is False:
        print("未配置CONFIG变量，无法执行")
        exit(1)
    else:
        # region 初始化参数
        config = dict()
        try:
            config = dict(json.loads(os.environ.get("CONFIG")))
        except:
            print("CONFIG格式不正确，请检查Secret配置，请严格按照JSON格式：使用双引号包裹字段和值，逗号不能多也不能少")
            traceback.print_exc()
            exit(1)
        PUSH_PLUS_TOKEN = config.get('PUSH_PLUS_TOKEN')
        users = config.get('USER')
        passwords = config.get('PWD')
        if users is None or passwords is None:
            print("未正确配置账号密码，无法执行")
            exit(1)
        # endregion
        execute()
