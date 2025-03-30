# models.py
from sqlalchemy import Column, Integer, String, DateTime, Text, Table, ForeignKey, BigInteger
from sqlalchemy import SmallInteger
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# 多对多关联表
illustration_tag = Table(
    'illustration_tag', Base.metadata,
    Column('illust_id', Integer, ForeignKey('illustrations.illust_id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.tag_id'), primary_key=True)
)

class Illustration(Base):
    __tablename__ = 'illustrations'

    illust_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    create_date = Column(DateTime, nullable=False)
    illust_type = Column(SmallInteger, nullable=False)
    x_restrict = Column(SmallInteger, nullable=False)
    ai_type = Column(SmallInteger, nullable=False)
    width = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    image_url = Column(Text, nullable=False)

    save_date = Column(BigInteger, nullable=False)


    tags = relationship('Tag', secondary=illustration_tag, back_populates='illustrations')

class Tag(Base):
    __tablename__ = 'tags'

    tag_id = Column(Integer, primary_key=True, autoincrement=True)
    tag_name = Column(String(255), unique=True, nullable=False)

    illustrations = relationship('Illustration', secondary=illustration_tag, back_populates='tags')
