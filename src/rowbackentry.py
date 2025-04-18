
from utils.delete_illustration_by_save_date import *  # 替换为你的实际模块路径
import sys

def main():


    print("🗓️ 请输入要删除的插画 save_date（格式如 202503301443）：")
    try:
        user_input = input(">>> ").strip()
        save_date = int(user_input)
    except ValueError:
        print("❌ 输入格式错误，必须是纯数字！")
        sys.exit(1)



    result = delete_illustration_by_save_date(save_date)
    if result:
        print("🎉 删除成功")
    else:
        print("⚠️ 删除失败或没有匹配的数据")

if __name__ == "__main__":
    main()
