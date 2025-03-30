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
from utils.save_info_to_mysql import save_illustration_detail_from_json
from utils.create_folder import create_users_folder
from utils.get_with_retry import get_json_with_retry

def crawler_ranking_withchecking(url, page, path, batch):
    print(f"📄 正在统计 page {page+1} 的下载任务...")

    try:
        res = get_json_with_retry(url, headers=headers)
        datas = res.get("contents", []) if res else []
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

        # 1. 获取作品详情（用于保存入库）
        detail_url = f"https://www.pixiv.net/ajax/illust/{illust_id}?lang=zh"
        try:
            detail_res = get_json_with_retry(detail_url, headers=headers)
            detail_data = detail_res.get("body", {}) if detail_res else {}
            if isinstance(detail_data, dict):
                inserted = save_illustration_detail_from_json(detail_data, batch)
                if not inserted:
                    print(f"⏭️ 插画 {illust_id} 已存在数据库，跳过图片下载")
                    continue  # 🚫 直接跳过下面的图片处理
            else:
                print(f"⚠️ 作品 {illust_id} 的详情数据格式异常，跳过")
        except Exception as e:
            print(f"❌ 获取插画 {illust_id} 详情失败：{e}")
            continue

        # 2. 获取作品图片（包括多页）
        image_pages_url = f"https://www.pixiv.net/ajax/illust/{illust_id}/pages?lang=zh"
        try:
            image_json = get_json_with_retry(image_pages_url, headers=headers)
            image_data = image_json.get("body", []) if image_json else []
        except Exception as e:
            print(f"❌ 获取插画 {illust_id} 图片页失败：{e}")
            continue

        for b in image_data:
            download_count += 1
            t = Thread(
                target=download_img,
                args=(b['urls']['original'], image["referer"], path),
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
