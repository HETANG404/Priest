import os
import requests
import threading
from threading import Thread


# 添加fig文件夹到Python路径，以便能够导入setting模块
# 假设当前脚本与fig文件夹在同一目录下，如果不是，请调整路径
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from config.settings import headers
from utils.downloader import download_img,download_img_withgroup,download_img_force_check
from utils.save_info_to_mysql import save_illustration_detail_from_json
from utils.create_folder import create_users_folder


max_connections = 10  # 定义最大线程数,可根据网速修改
pool_sema = threading.BoundedSemaphore(max_connections)  # 或使用Semaphore方法

def wander_crawler_ranking(url, page, path):
    print(f"📄 正在统计 page {page+1} 的下载任务...")

    # 添加 content=illust 参数以仅获取插画作品
    url = f"{url}&content=illust"

    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        datas = res.json().get("contents", [])
    except Exception as e:
        print(f"❌ 获取排行榜数据失败：{e}")
        return

    images_list = []
    for data in datas:
        images_list.append({
            "title": data["title"],
            "user_name": data["user_name"],
            "p_id": data["illust_id"],
            "referer": f"https://www.pixiv.net/artworks/{data['illust_id']}"
        })

    thread_list = []
    download_count = 0

    for idx, image in enumerate(images_list):
        illust_id = image["p_id"]

        # 获取作品图片（包括多页）
        image_pages_url = f"https://www.pixiv.net/ajax/illust/{illust_id}/pages?lang=zh"
        try:
            image_data = requests.get(image_pages_url, headers=headers).json().get("body", [])
        except Exception as e:
            print(f"❌ 获取插画 {illust_id} 图片页失败：{e}")
            continue

        # 🔧 如果该作品有5页及以上，跳过整个作品
        if len(image_data) >= 3:
            print(f"⚠️ 插画 {illust_id} 有 {len(image_data)} 页，已跳过")
            continue

        for b in image_data:
            download_count += 1
            t = Thread(
                target=download_img_withgroup,
                args=(b['urls']['original'], image["referer"], page * 50 + idx + 1, path),
                name=str(illust_id)
            )
            thread_list.append(t)

    print(f"🧮 总共创建了 {download_count} 个下载任务")
    print("🚀 开始下载...")

    for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()

    print(f"✅ 第 {page+1} 页下载完成")