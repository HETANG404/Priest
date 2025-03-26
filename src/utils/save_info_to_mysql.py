from datetime import datetime

from db.mysql_manager import SessionLocal
from db.models import Illustration, Tag


def save_illustration_detail_from_json(data):
    try:
        with SessionLocal() as session:
            illust = Illustration(
                illust_id=int(data["illustId"]),
                user_id=int(data["userId"]),
                create_date=datetime.fromisoformat(data["createDate"].replace("Z", "+00:00")),
                illust_type=int(data["illustType"]),
                x_restrict=int(data["xRestrict"]),
                ai_type=int(data["aiType"]),
                width=int(data["width"]),
                height=int(data["height"]),
                image_url=data["urls"]["original"] if "original" in data["urls"] else None
            )

            session.add(illust)
            
            # 用一个有序字典去重，key 是 tag["tag"]，值是整个字典
            unique_tag_map = {}
            for tag in data["tags"]["tags"]:
                tag_name = tag["tag"]
                if tag_name not in unique_tag_map:
                    unique_tag_map[tag_name] = tag  # 保留第一次出现的完整结构

            # 得到去重后的 tag_list（列表形式）
            tag_list = list(unique_tag_map.values())

            for tag in tag_list:
                tag_name = tag["tag"]
                tag_obj = session.query(Tag).filter_by(tag_name=tag_name).first()
                if not tag_obj:
                    tag_obj = Tag(tag_name=tag_name)
                    session.add(tag_obj)  # ✅ 添加新 tag 到 session
                    session.flush()  # ✅ 立即让数据库分配 ID，避免重复插入

                # ✅ 避免多对多重复插入
                if tag_obj not in illust.tags:
                    illust.tags.append(tag_obj)


            session.commit()
            print(f"✅ 已保存插画 {data['illustId']} 的详细信息到数据库")
    except Exception as e:
        print(f"❌ 保存插画 {data['illustId']} 失败：{e}")
