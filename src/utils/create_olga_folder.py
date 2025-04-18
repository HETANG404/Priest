import os
import datetime
import sys

# 添加fig文件夹到Python路径，以便能够导入setting模块
# 假设当前脚本与fig文件夹在同一目录下，如果不是，请调整路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# 从config.settings导入BASE_PATH
from config.settings import BASE_PATH

# totaly: daily / daily_r18 / weekly / weekly_r18 / monthly




def check_olga_wm_folder():
    """
    根据当前日期在BASE_PATH/olga查看受否文件存在
    检测文件内容数量
    """
    
    # 构建完整路径
    path = os.path.join(BASE_PATH, "olga", "olga_wm")
    

    # 检查文件夹是否已存在
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"✅ 成功创建文件夹: {path}\n")
    # 检查文件夹是否已存在
    else:
        print(f"🔌 文件夹已存在: {path}\n")

        
    # 统计文件夹中图片数量（假设为 .jpg / .png / .webp 等）
    image_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.bmp', '.gif')
    num = len([
        f for f in os.listdir(path)
        if os.path.isfile(os.path.join(path, f)) and f.lower().endswith(image_extensions)
    ])

    print(f"📦 文件数量: {num} 个\n")
    return path, num
