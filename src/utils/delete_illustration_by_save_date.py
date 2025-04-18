from sqlalchemy.orm import Session
from sqlalchemy import select, delete
from db.mysql_manager import SessionLocal
from db.models import Illustration, Tag  # 假设 Illustration 与 Tag 是通过 secondary 表关联的

def delete_illustration_by_save_date(save_date: int):
    try:
        with SessionLocal() as session:
            # 查询要删除的插画列表
            illustrations = session.query(Illustration).filter_by(save_date=save_date).all()

            if not illustrations:
                print(f"ℹ️ 没有找到 save_date 为 {save_date} 的插画记录")
                return False

            illust_ids = [i.illust_id  for i in illustrations]

            # 打印要删除的 ID
            print(f"🗑️ 准备删除以下插画ID: {illust_ids}")

            # 删除中间表中的关联标签关系
            for illust in illustrations:
                illust.tags.clear()

            # 删除插画记录
            for illust in illustrations:
                session.delete(illust)

            session.commit()
            print(f"✅ 成功删除 save_date = {save_date} 的插画及标签关系")
            return True

    except Exception as e:
        print(f"❌ 删除失败：{e}")
        return False
