import os
import datetime
import sys

# 添加fig文件夹到Python路径，以便能够导入setting模块
# 假设当前脚本与fig文件夹在同一目录下，如果不是，请调整路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 从fig文件夹的setting.py导入BASE_PATH
from config.settings import BASE_PATH

def create_daily_folder():
    """
    根据当前日期在BASE_PATH/images/ranking/daily目录下创建文件夹
    如果文件夹已存在则不会重复创建
    """
    # 获取当前日期
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # 构建基础路径
    base_path = os.path.join(BASE_PATH, "ranking", "daily")
    
    # 确保基础路径存在
    if not os.path.exists(base_path):
        os.makedirs(base_path)
        print(f"创建基础路径: {base_path}")
    
    # 构建新文件夹的完整路径
    folder_path = os.path.join(base_path, current_date)
    
    # 检查文件夹是否已存在
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"成功创建文件夹: {folder_path}")
    else:
        print(f"文件夹已存在: {folder_path}")

if __name__ == "__main__":
    create_daily_folder()