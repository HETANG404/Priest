from PIL import Image
import os

def images_to_pdf(image_folder, output_pdf_path):

    # ✅ 合并成 PDF
    print("🛠 正在合并图片为 PDF...")
    
    # 支持的图片扩展名
    supported_exts = ('.jpg', '.jpeg', '.png')

    # 获取并排序所有图片文件
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(supported_exts)]
    image_files.sort()  # 可按文件名排序

    if not image_files:
        print("指定文件夹中没有找到图片。")
        return

    # 打开图片并转换为RGB模式
    image_list = []
    for file in image_files:
        img_path = os.path.join(image_folder, file)
        img = Image.open(img_path).convert('RGB')
        image_list.append(img)

    # 保存为PDF（第一张图是主图，其他是附加页）
    image_list[0].save(output_pdf_path, save_all=True, append_images=image_list[1:])
    print(f"PDF已保存到：{output_pdf_path}")


