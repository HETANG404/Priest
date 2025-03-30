import requests
import time
import random

def get_json_with_retry(url, headers, max_retries=15, name="请求"):
    for attempt in range(max_retries):
        try:
            res = requests.get(url, headers=headers)
            if res.status_code == 200:
                return res.json()
            elif res.status_code == 429:
                wait = 10 + attempt * 6 + random.uniform(0, 2)
                print(f"⚠️ [{name}] 请求太频繁（429），等待 {wait:.1f}s 后重试：{url}")
                time.sleep(wait)
                continue
            else:
                print(f"⚠️ [{name}] 状态码 {res.status_code}：{url}")
                time.sleep(wait)
                continue
        except Exception as e:
            print(f"❌ [{name}] 请求异常：{e} -> {url}")
            time.sleep(2 + attempt)
    print(f"❌ [{name}] 多次重试失败：{url}")
    return None


def get_image_with_retry(url, headers, max_retries=15, name="图片请求"):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, timeout=(5, 15), stream=True)

            if response.status_code == 200:
                return response

            elif response.status_code == 429:
                wait = 8 + attempt * 3 + random.uniform(0, 2)
                print(f"⚠️ [{name}] 请求太频繁（429），等待 {wait:.1f}s 后重试：{url}")
                time.sleep(wait)
                continue

            else:
                print(f"⚠️ [{name}] 状态码 {response.status_code}：{url}")
                time.sleep(2 + attempt)
                continue

        except requests.exceptions.RequestException as e:
            print(f"❌ [{name}] 网络异常：{e} -> {url}")
            time.sleep(2 + attempt)

    print(f"❌ [{name}] 多次重试失败：{url}")
    return None