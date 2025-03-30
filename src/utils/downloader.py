import os
import time
import random
import requests


from utils.get_with_retry import get_json_with_retry,get_image_with_retry
'''

只是下载的方法，
    withgroup是当出现连击的时候通过‘i’合并成小组命名
    download_img是普通的把id作为文件名字

'''


# download with group

def download_img_withgroup(url, referer, i, path):  # 获取到图片url后定义个函数用于下载
    headers_download = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        "referer": str(referer)
    }
    name = str(i) + '_' + url.split("/")[-1]  # 将图片链接以斜杠分割后取最后面的信息作为名字，因为爬取的图片有jeg也有png
    
    file_path = os.path.join(path, name)

    # naming in without group way
    # name = url.split("/")[-1]  # 分割url最后一段作为image文件名，因为有jeg和png
    
    if os.path.exists(f"{path}/{name}"):
        print(f'🔌 {name}已存在')
        return

    for attempt in range(20):
        try:
            response = requests.get(url=url, headers=headers_download)

            # ✅ 正常成功返回
            if response.status_code == 200:
                with open(file_path, "wb") as file:
                    file.write(response.content)
                print(f"✅ {name} 下载成功")
                return True


            # ✅ 处理 429 错误：请求太频繁
            elif response.status_code == 429:
                wait = 5 + attempt * 3 + random.uniform(0, 2)
                print(f"⚠️ 请求太频繁（429），等待 {wait:.1f} 秒后重试... ({name})")
                time.sleep(wait)
                continue


            
            # ❌ 其他异常状态码
            else:
                print(f"⚠️ 下载 {name} 时返回状态码 {response.status_code}")
                time.sleep(2 + attempt)


        except requests.exceptions.RequestException as e:
            print(f"⚠️ 发生网络错误,应该是反爬，小睡一下: {e}，尝试重新连接... ({name})")
            time.sleep(2 + attempt)

    print(f"{name} 最终下载失败")
    return False




def download_img(url, referer, path):  # 获取到图片url后 注入referer到header中 下载到path文件中
    
    headers_download = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        "referer": str(referer)
    }

    name = url.split("/")[-1]  # 分割url最后一段作为image文件名，因为有jeg和png

    file_path = os.path.join(path, name)
    
    if os.path.exists(f"{path}/{name}"):    #insure that image(name) is not in 'path'folder
        print(f'🔌 {name}存在')
        return

    for attempt in range(20):
        try:
            response = requests.get(url=url, headers=headers_download)

            # ✅ 正常成功返回
            if response.status_code == 200:
                with open(file_path, "wb") as file:
                    file.write(response.content)
                print(f"✅ {name} 下载成功")
                return True


            # ✅ 处理 429 错误：请求太频繁
            elif response.status_code == 429:
                wait = 5 + attempt * 3 + random.uniform(0, 2)
                print(f"⚠️ 请求太频繁（429），等待 {wait:.1f} 秒后重试... ({name})")
                time.sleep(wait)
                continue
            
            # ❌ 其他异常状态码
            else:
                print(f"⚠️ 下载 {name} 时返回状态码 {response.status_code}")
                time.sleep(2 + attempt)

        except requests.exceptions.RequestException as e:
            print(f"⚠️ 发生网络错误,应该是反爬，小睡一下: {e}，尝试重新连接... ({name})")
            time.sleep(2 + attempt)

    print(f"❌ {name} 最终下载失败")
    return False


def download_img_force_check(url, referer, path):  # 获取到图片url后 注入referer到header中 下载到path文件中
    
    headers_download = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        "referer": str(referer)
    }

    name = url.split("/")[-1]  # 分割url最后一段作为image文件名，因为有jeg和png

    file_path = os.path.join(path, name)
    
    if os.path.exists(f"{path}/{name}"):    #insure that image(name) is not in 'path'folder
        print(f'🔌 {name}存在')
        return

    for attempt in range(20):
        try:
            response = get_image_with_retry(url=url, headers=headers_download)

            # ✅ 正常成功返回
            if response.status_code == 200:
                with open(file_path, "wb") as file:
                    file.write(response.content)
                print(f"✅ {name} 下载成功")
                return True


            # ✅ 处理 429 错误：请求太频繁
            elif response.status_code == 429:
                wait = 5 + attempt * 3 + random.uniform(0, 2)
                print(f"⚠️ 请求太频繁（429），等待 {wait:.1f} 秒后重试... ({name})")
                time.sleep(wait)
                continue
            
            # ❌ 其他异常状态码
            else:
                print(f"⚠️ 下载 {name} 时返回状态码 {response.status_code}")
                time.sleep(2 + attempt)

        except requests.exceptions.RequestException as e:
            print(f"⚠️ 发生网络错误,应该是反爬，小睡一下: {e}，尝试重新连接... ({name})")
            time.sleep(2 + attempt)

    print(f"❌ {name} 最终下载失败")
    return False