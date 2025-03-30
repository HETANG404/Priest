import utils.create_folder
from core.spider import *
from utils.create_folder import *
import datetime

from config.settings import BASE_PATH


import os
import utils.create_folder as create_folder  # 假设你是这么导入的
from core.spider import *  # 假设你封装了这几个函数
import sys

from utils.pdf_factory import images_to_pdf


def print_menu():
    print("=" * 50)
    print(" Pixiv 插画下载工具 ")
    print("=" * 50)
    print("1. 下载日周月而十八天梯，自选模式")
    print("2. 下载指定画师全部作品，需要挨滴")
    print("3. 下载关注用户最新更新, 打打牙祭")
    print("4. 下载关注用户全量更新，火力全开")
    print("=" * 50)

def main():
    base_url = 'https://www.pixiv.net/'
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_menu()
        choice = input("请输入功能编号（ 1 / 2 / 3 / 4 ）：").strip()

        if choice == '1':
            valid_modes = {"daily", "weekly", "monthly", "daily_r18", "weekly_r18", "r18g"}
            print("\n支持模式：daily / weekly / monthly / weekly_r18 / daily_r18 / r18g")
            
            mode = input("请输入下载模式：").strip()

            if mode == "r18g":
                confirm = input("❗ 该模式涉及严重 R18G 内容，确认继续请输入 yes：").strip().lower()
                if confirm != "yes":
                    print("⚠️ 已取消下载 R18G 排行榜")
                    input("按回车键返回主菜单...")
                    continue

            if mode not in valid_modes:
                print("❌ 非法模式，请重新输入。")
                input("按回车键返回主菜单...")
                continue

            method_name = f"create_{mode}_folder"
            method = getattr(create_folder, method_name, None)

            if not callable(method):
                print(f"❌ 未找到对应的文件夹创建方法: {method_name}")
                input("按回车键返回主菜单...")
                continue

            path = method()

            # 设置默认最大页数
            default_pages = {
                "daily": 10,
                "weekly": 10,
                "monthly": 10,
                "daily_r18": 2,
                "weekly_r18": 2,
                "r18g": 1
            }

            max_page = default_pages.get(mode, 1)

            # 提示用户输入页数
            print(f"💡 {mode} 模式最多支持 {max_page} 页（按回车使用默认）")
            user_page_input = input("请输入要下载的页数：").strip()

            if user_page_input == "":
                page = max_page
            else:
                if user_page_input.isdigit():
                    page = int(user_page_input)
                    if page > max_page or page <= 0:
                        print(f"❌ 页数超出范围（1 ~ {max_page}）")
                        input("按回车键返回主菜单...")
                        continue
                else:
                    print("❌ 页数必须是正整数")
                    input("按回车键返回主菜单...")
                    continue

            # 生成 PDF 文件路径，拼上页数
            date_str = datetime.datetime.now().strftime('%Y-%m-%d')
            pdf_path = os.path.join(BASE_PATH, "pdfs", f"merged_{mode}_{page}p_{date_str}.pdf")

            for i in range(page):
                url = f"{base_url}ranking.php?mode={mode}&p={i + 1}&format=json"
                crawler_ranking(url, i, path)

            images_to_pdf(path, pdf_path)
            print(f"\n📄 PDF 文件已生成：{pdf_path}")



        elif choice == '2':
            user_id = input("\n请输入画师的用户ID：").strip()
            url = f"{base_url}ajax/user/{user_id}/profile/all?lang=zh"
            crawler_users(url, user_id)

        elif choice == '3':
            try:
                page = int(input("请输入下载页数（每页60张）：").strip())
            except ValueError:
                print("❌ 输入无效，必须是整数。")
                input("按回车键返回主菜单...")
                continue

            url = f"{base_url}ajax/follow_latest/illust?lang=zh&mode=r18"
            
            path = os.path.join(BASE_PATH, "following")

            if not os.path.exists(path):
                print(f"❌ 文件夹不存在：{path}，请手动创建后再运行程序。")
                sys.exit(1)  # 🚨 直接退出程序
            
            print("开始下载...\n")
            for i in range(page):
                page_url = f"{url}&p={i + 1}"
                crawler_latest_following(page_url, path)

        elif choice == '4':


                
            print(crawler_following())


        else:
            print("❌ 输入错误，请输入 1, 2 或 3。")
            input("按回车键返回主菜单...")
            continue

        print("\n✅ 下载任务完成！")
        break

if __name__ == "__main__":
    main()