import os
import datetime
import sys

# 添加fig文件夹到Python路径，以便能够导入setting模块
# 假设当前脚本与fig文件夹在同一目录下，如果不是，请调整路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# 从config.settings导入BASE_PATH
from config.settings import BASE_PATH

# totaly: daily / daily_r18 / weekly / weekly_r18 / monthly




def create_daily_folder():
    """
    根据当前日期在BASE_PATH/ranking/daily目录下创建文件夹
    如果文件夹已存在则不会重复创建
    """
    # 获取当前日期
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # 构建基础路径
    base_path = os.path.join(BASE_PATH, "ranking", "daily")
    
    # 构建新文件夹的完整路径
    folder_path = os.path.join(base_path, current_date)
    
    # 检查文件夹是否已存在
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"✅ 成功创建文件夹: {folder_path}\n")
    else:
        # 清空该目录下所有图片文件
        print(f"🔌 文件夹已存在: {folder_path},正在清空...\n")
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                try:
                    os.remove(os.path.join(folder_path, filename))
                except Exception as e:
                    print(f"⚠️ 无法删除 {filename}：{e}")
    
    return folder_path


def create_daily_r18_folder():
    """
    根据当前日期在BASE_PATH/ranking/daily_r18目录下创建文件夹
    如果文件夹已存在则不会重复创建
    """
    # 获取当前日期
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # 构建基础路径
    base_path = os.path.join(BASE_PATH, "ranking", "daily_r18")
    
    # 构建新文件夹的完整路径
    folder_path = os.path.join(base_path, current_date)
    
    # 检查文件夹是否已存在
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"✅ 成功创建文件夹: {folder_path}\n")
    else:
        # 清空该目录下所有图片文件
        print(f"🔌 文件夹已存在: {folder_path},正在清空...\n")
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                try:
                    os.remove(os.path.join(folder_path, filename))
                except Exception as e:
                    print(f"⚠️ 无法删除 {filename}：{e}")
        
    return folder_path


def create_weekly_folder():
    """
    根据当前日期在BASE_PATH/ranking/weekly目录下创建文件夹
    如果文件夹已存在则不会重复创建
    """
    # 获取当前日期
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # 构建基础路径
    base_path = os.path.join(BASE_PATH, "ranking", "weekly")
    
    # 构建新文件夹的完整路径
    folder_path = os.path.join(base_path, current_date)
    
    # 检查文件夹是否已存在
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"✅ 成功创建文件夹: {folder_path}\n")
    else:
        # 清空该目录下所有图片文件
        print(f"🔌 文件夹已存在: {folder_path},正在清空...\n")
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                try:
                    os.remove(os.path.join(folder_path, filename))
                except Exception as e:
                    print(f"⚠️ 无法删除 {filename}：{e}")
    
    return folder_path


def create_weekly_r18_folder():
    """
    根据当前日期在BASE_PATH/ranking/weekly_r18目录下创建文件夹
    如果文件夹已存在则不会重复创建
    """
    # 获取当前日期
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # 构建基础路径
    base_path = os.path.join(BASE_PATH, "ranking", "weekly_r18")
    
    # 构建新文件夹的完整路径
    folder_path = os.path.join(base_path, current_date)
    
    # 检查文件夹是否已存在
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"✅ 成功创建文件夹: {folder_path}\n")
    else:
        # 清空该目录下所有图片文件
        print(f"🔌 文件夹已存在: {folder_path},正在清空...\n")
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                try:
                    os.remove(os.path.join(folder_path, filename))
                except Exception as e:
                    print(f"⚠️ 无法删除 {filename}：{e}")
    return folder_path


def create_monthly_folder():
    """
    根据当前日期在BASE_PATH/ranking/monthly目录下创建文件夹
    如果文件夹已存在则不会重复创建
    """
    # 获取当前日期
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # 构建基础路径
    base_path = os.path.join(BASE_PATH, "ranking", "monthly")
    
    # 构建新文件夹的完整路径
    folder_path = os.path.join(base_path, current_date)
    
    # 检查文件夹是否已存在
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"✅ 成功创建文件夹: {folder_path}\n")
    else:
        # 清空该目录下所有图片文件
        print(f"🔌 文件夹已存在: {folder_path},正在清空...\n")
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                try:
                    os.remove(os.path.join(folder_path, filename))
                except Exception as e:
                    print(f"⚠️ 无法删除 {filename}：{e}")
    return folder_path


def create_r18g_folder():
    """
    根据当前日期在BASE_PATH/ranking/r18g目录下创建文件夹
    如果文件夹已存在则不会重复创建
    """
    # 获取当前日期
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # 构建基础路径
    base_path = os.path.join(BASE_PATH, "ranking", "r18g")
    
    # 构建新文件夹的完整路径
    folder_path = os.path.join(base_path, current_date)
    
    # 检查文件夹是否已存在
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"✅ 成功创建文件夹: {folder_path}\n")
    else:
        # 清空该目录下所有图片文件
        print(f"🔌 文件夹已存在: {folder_path},正在清空...\n")
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                try:
                    os.remove(os.path.join(folder_path, filename))
                except Exception as e:
                    print(f"⚠️ 无法删除 {filename}：{e}")
    return folder_path


def create_users_folder(nameAndnum):
    """
    根据当前日期在BASE_PATH/users目录下创建文件夹
    如果文件夹已存在则不会重复创建
    """
    
    # 构建基础路径
    base_path = os.path.join(BASE_PATH, "users", )
    
    # 构建新文件夹的完整路径
    folder_path = os.path.join(base_path, nameAndnum)
    
    # 检查文件夹是否已存在
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"✅ 成功创建文件夹: {folder_path}\n")
    else:
        print(f"🔌 文件夹已存在: {folder_path}\n")
        
    return folder_path