import os
import requests
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
    
    # naming in without group way
    # name = url.split("/")[-1]  # 分割url最后一段作为image文件名，因为有jeg和png
    
    if os.path.exists(f"{path}/{name}"):
        print(f'{name}已存在')
        return

    for _ in range(20):
        try:
            response = requests.get(url=url, headers=headers_download)  # print(url)
            if response.status_code == 200:
                with open(f"{path}/{name}", "wb") as file:
                    file.write(response.content)
                    # print(f'{name} 下载成功')
                    return True
        except requests.exceptions.RequestException:
            print("发生错误:重新连接")

    print(f"{name} 最终下载失败", end='  ')
    return False


# pure download

def download_img(url, referer, path):  # 获取到图片url后 注入referer到header中 下载到path文件中
    
    headers_download = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        "referer": str(referer)
    }

    name = url.split("/")[-1]  # 分割url最后一段作为image文件名，因为有jeg和png
    
    if os.path.exists(f"{path}/{name}"):    #insure that image(name) is not in 'path'folder
        print(f'{name}存在', end='  ')
        return

    for _ in range(20):
        try:
            response = requests.get(url=url, headers=headers_download)  # print(url)
            if response.status_code == 200:
                with open(f"{path}/{name}", "wb") as file:
                    file.write(response.content)
                    # print(f'{name} 下载成功')
                    return True
        except requests.exceptions.RequestException:
            print("发生错误:重新连接")

    print(f"{name} 最终下载失败", end='  ')
    return False
