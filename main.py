import hashlib
import random
import time
from datetime import datetime
from urllib.parse import urlencode
import os

import requests

name = os.environ.get("user").split('#')
pwd = os.environ.get("pwd")
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
        "token": os.environ.get("token"),
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
