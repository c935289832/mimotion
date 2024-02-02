import hashlib
import random
import time
from datetime import datetime
from urllib.parse import urlencode

import requests

name = ["1111@chacuo.net", "2222@chacuo.net", "3333@chacuo.net", "4444@chacuo.net", "5555@chacuo.net", "6666@chacuo.net", "7777@chacuo.net"]
pwd = "z1234567"
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
        "token": token,
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
