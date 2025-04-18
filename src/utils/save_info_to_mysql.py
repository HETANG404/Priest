from datetime import datetime
from sqlalchemy.exc import IntegrityError
from db.mysql_manager import SessionLocal
from db.models import Illustration, Tag


def save_illustration_detail_from_json(data,save_date):
    try:
        with SessionLocal() as session:
            # ✅ 插入前判断是否已存在
            existing = session.query(Illustration).filter_by(illust_id=int(data["illustId"])).first()
            if existing:
                print(f"🔁 插画 {data['illustId']} 已存在，跳过插入")
                return False

            # 👇 创建 Illustration 实例
            illust = Illustration(
                illust_id=int(data["illustId"]),
                user_id=int(data["userId"]),
                create_date=datetime.fromisoformat(data["createDate"].replace("Z", "+00:00")),
                illust_type=int(data["illustType"]),
                x_restrict=int(data["xRestrict"]),
                ai_type=int(data["aiType"]),
                width=int(data["width"]),
                height=int(data["height"]),
                image_url=data["urls"].get("original"),
                save_date=int(save_date)
            )

            session.add(illust)

            # 👇 去重处理 tags
            unique_tag_map = {}
            for tag in data["tags"]["tags"]:
                tag_name = tag["tag"]
                if tag_name not in unique_tag_map:
                    unique_tag_map[tag_name] = tag

            tag_list = list(unique_tag_map.values())

            for tag in tag_list:
                tag_name = tag["tag"]
                tag_obj = session.query(Tag).filter_by(tag_name=tag_name).first()
                if not tag_obj:
                    tag_obj = Tag(tag_name=tag_name)
                    session.add(tag_obj)
                    session.flush()

                if tag_obj not in illust.tags:
                    illust.tags.append(tag_obj)

            session.commit()
            print(f"✅ 已保存插画 {data['illustId']} 的详细信息到数据库")
            return True

    except IntegrityError as e:
        print(f"❌ 插画 {data['illustId']} 插入失败（主键冲突）：{e}")
    except Exception as e:
        print(f"❌ 插画 {data['illustId']} 插入失败（其他错误）：{e}")