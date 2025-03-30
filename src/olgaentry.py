import os
from utils.create_loga_folder import check_olga_wm_folder
import time
import random
import sys
from datetime import datetime

from core.olga import *



def print_menu():
    print("=" * 50)
    print(" OLGA ")
    print("=" * 50)
    print("1. 增量weekly")
    print("2. 增量monthly")
    print("3. 增量w & m")
    print("=" * 50)

def main():
    base_url = 'https://www.pixiv.net/'
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_menu()
        choice = input("请输入功能编号（1 / 2 / 3）：").strip()

        if choice == '1':
            print("\n增量 weekly")
            mode = "weekly"
            batch = int(datetime.now().strftime("%Y%m%d%H%M"))

            try:
                path, num = check_olga_wm_folder()
                print(f"\n✅ 找到了 {num} 张图！")
            except FileNotFoundError as e:
                print(f"❌ 错误：{e}")


            for i in range(10):
                print("就不做了，睡大觉")
                wait = 5 + i * 5 + random.uniform(0, 2)
                time.sleep(wait)
                url = f"{base_url}ranking.php?mode={mode}&p={i + 1}&format=json"
                crawler_ranking_withchecking(url, i, path, batch)

            print("\n✅ 增量 weekly 完成")

        elif choice == '2':
            print("\n增量 monthly")
            mode = "monthly"
            batch = int(datetime.now().strftime("%Y%m%d%H%M"))
            
            try:
                path, num = check_olga_wm_folder()
                print(f"\n✅ 找到了 {num} 张图！")
            except FileNotFoundError as e:
                print(f"❌ 错误：{e}")


            for i in range(10):
                print("就不做了，睡大觉") 
                wait = 5 + i * 5 + random.uniform(0, 2)
                time.sleep(wait)
                url = f"{base_url}ranking.php?mode={mode}&p={i + 1}&format=json"
                crawler_ranking_withchecking(url, i, path, batch)

            print("\n✅ 增量 monthly 完成")

        elif choice == '3':
            print("\n增量 w & m")
            mode = "monthly"
            batch = int(datetime.now().strftime("%Y%m%d%H%M"))
            
            try:
                path, num = check_olga_wm_folder()
                print(f"\n✅ 找到了 {num} 张图！")
            except FileNotFoundError as e:
                print(f"❌ 错误：{e}")

            mode_w = "weekly"

            for i in range(10):
                print("就不做了，睡大觉")
                wait = 5 + i * 5 + random.uniform(0, 2)
                time.sleep(wait)
                url = f"{base_url}ranking.php?mode={mode_w}&p={i + 1}&format=json"
                crawler_ranking_withchecking(url, i, path, batch)

            print("\n✅ 增量 weekly 完成\n")

            print("start: monthly")


            mode_m = "monthly"

            for i in range(10):
                print("\n就不做了，睡大觉")
                wait = 5 + i * 5 + random.uniform(0, 2)
                time.sleep(wait)
                url = f"{base_url}ranking.php?mode={mode_m}&p={i + 1}&format=json"
                crawler_ranking_withchecking(url, i, path, batch)

            print("\n✅ 增量 monthly 完成")


        else:
            print("❌ 输入错误，请输入 1, 2 或 3。")
            input("按回车键返回主菜单...")
            continue

        print("\n✅ 程序结束！")
        break

if __name__ == "__main__":
    main()
