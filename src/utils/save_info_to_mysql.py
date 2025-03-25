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

            tag_list = data["tags"]["tags"]
            for tag in tag_list:
                tag_name = tag["tag"]
                tag_obj = session.query(Tag).filter_by(tag_name=tag_name).first()
                if not tag_obj:
                    tag_obj = Tag(tag_name=tag_name)
                illust.tags.append(tag_obj)

            session.add(illust)
            session.commit()
            print(f"✅ 已保存插画 {data['illustId']} 的详细信息到数据库")
    except Exception as e:
        print(f"❌ 保存插画 {data['illustId']} 失败：{e}")
