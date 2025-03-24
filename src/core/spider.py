import os
import requests
import threading
from threading import Thread


# 添加fig文件夹到Python路径，以便能够导入setting模块
# 假设当前脚本与fig文件夹在同一目录下，如果不是，请调整路径
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from config.settings import headers
from utils.downloader import download_img,download_img_withgroup


max_connections = 10  # 定义最大线程数,可根据网速修改
pool_sema = threading.BoundedSemaphore(max_connections)  # 或使用Semaphore方法


def crawler_ranking(url, page, path):  # https://www.pixiv.net/ranking.php?mode=monthly_r18&p=1&format=json   # https://www.pixiv.net/bookmark_new_illust
    res = requests.get(url, headers=headers)
    datas = res.json()["contents"]  # print(datas)
    images_list = []
    
    print(f"正在统计page:{page+1}下载任务数量...")

    for data in datas:
        image = {
            "title": data["title"],
            "user_name": data["user_name"],
            "p_id": data["illust_id"],
            "referer": f"https://www.pixiv.net/artworks/{data['illust_id']}"
        }
        images_list.append(image)  # print(images_list)

    thread_list = []
    download_count = 0  # 添加下载任务计数器

    for i in range(len(images_list)):
        image_1 = images_list[i]
        image_url = f"https://www.pixiv.net/ajax/illust/{image_1['p_id']}/pages?lang=zh"  # 通过以下链接，请求图片详情
        
        # print({image_1['p_id']})

        image_data = requests.get(image_url, headers=headers).json()["body"]  # 数据保存在body字段        print(image_data)
        
        for b in image_data:  # thumb_mini/small/regular/original
            download_count += 1 # 每创建一个下载任务就计数加1
            t = Thread(target=download_img_withgroup, args=(b['urls']['original'], image_1["referer"], page * 50 + i + 1, path),
                       name=image_1['p_id'])
            thread_list.append(t)

    print(f"总共有 {download_count} 个下载任务")  # 输出总任务数
    print("开始下载...")

    for t in thread_list:
        t.start()  # 调用start()方法，开始执行

    for t in thread_list:
        t.join()  # 子线程调用join()方法，使主线程等待子线程运行完毕之后才退出
    print(f"page:{page+1} 下载完成")

def crawler_users(url, path):  # https://www.pixiv.net/ajax/user/23945843/profile/all?lang=zh
    res = requests.get(url, headers=headers)
    datas = res.json()["body"]  # print(datas["illusts"])

    images_list = list(datas["illusts"].keys())  # print(images_list)

    for i in range(len(images_list)):
        image_1 = images_list[i]
        Referer_ = f"https://www.pixiv.net/artworks/{image_1}"
        image_url = f"https://www.pixiv.net/ajax/illust/{image_1}/pages?lang=zh"  # 通过以下链接，请求图片详情
        image_data = requests.get(image_url, headers=headers).json()["body"]  # 数据保存在body字段        print(image_data)
        for b in image_data:  # thumb_mini/small/regular/original
            t = Thread(target=download_img, args=(b['urls']['original'], Referer_, path),
                       name=image_1)
            thread_list.append(t)

    for t in thread_list:
        t.start()  # 调用start()方法，开始执行

    for t in thread_list:
        t.join()  # 子线程调用join()方法，使主线程等待子线程运行完毕之后才退出

def crawler_latest(url, page, path):#  https://www.pixiv.net/ajax/follow_latest/illust?p=1&mode=r18&lang=zh
    res = requests.get(url, headers=headers)
    datas = res.json()["body"]  # print(datas["illusts"])
    images_list = datas["page"]["ids"]  # print(images_list, len(images_list))

    for i in range(len(images_list)):
        image_1 = images_list[i]
        Referer_ = f"https://www.pixiv.net/artworks/{image_1}"
        image_url = f"https://www.pixiv.net/ajax/illust/{image_1}/pages?lang=zh"  # 通过以下链接，请求图片详情
        image_data = requests.get(image_url, headers=headers).json()["body"]  # 数据保存在body字段        print(image_data)
        for b in image_data:  # thumb_mini/small/regular/original
            t = Thread(target=download_img, args=(b['urls']['original'], Referer_,  path),
                       name=image_1)
            thread_list.append(t)

    for t in thread_list:
        t.start()  # 调用start()方法，开始执行

    for t in thread_list:
        t.join()  # 子线程调用join()方法，使主线程等待子线程运行完毕之后才退出