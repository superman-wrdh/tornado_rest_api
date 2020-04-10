import sqlalchemy
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.sql.expression import text
from sqlalchemy.types import Date
from sqlalchemy.types import TIMESTAMP

from lib.mysql_base_model import BaseModel


class UserInfoModel(BaseModel):
    __tablename__ = 'user_info'
    __table_args__ = {'mysql_charset': 'utf8mb4', 'mysql_engine': 'InnoDB'}

    # 用户ID
    id = Column(BIGINT(20, unsigned=True), primary_key=True, comment='用户ID')
    # 登录名
    login_name = Column(String(64), unique=True, nullable=False, comment='登录名', index=True)
    # 密码哈希
    password_hash = Column(String(255), nullable=False, server_default="", comment='密码哈希')
    # 用户国家
    user_nation = Column(String(255), comment='用户国家')
    # 用户省份
    user_province = Column(String(255), comment='用户省份')
    # 用户城市
    user_city = Column(String(255), comment='用户城市')
    # 用户地区
    user_zone = Column(String(255), comment='用户地区')
    # 用户地址
    user_address = Column(String(255), comment='用户地址')
    # 用户学校
    user_school = Column(String(255), nullable=False, default="", comment='用户学校')
    # 用户微博
    user_weibo = Column(String(255), comment='用户微博')
    # 用户邮箱
    user_mail = Column(String(255), comment='用户邮箱', index=True)
    # 用户QQ
    user_qq = Column(String(255), comment='用户QQ')
    # 用户微信
    user_wechat = Column(String(255), comment='用户微信')
    # 用户头像
    user_avatar = Column(String(255), comment='用户头像')
    # 用户性别
    user_gender = Column((TINYINT(2)), comment='用户性别 1 男 ,2 女,3 未知')
    # 用户生日
    user_birthday = Column(Date, comment='用户生日')
    # 用户签名
    user_statement = Column(String(255), comment='用户签名')
    # 用户背景URL
    user_background_url = Column(String(255), nullable=False, default="", comment='用户背景URL')
    # 创建时间
    create_time = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP()'), comment='创建时间')
    # 更新时间
    update_time = Column(TIMESTAMP, nullable=False,
                         server_default=text('CURRENT_TIMESTAMP() on update  CURRENT_TIMESTAMP()'), comment='更新时间')



engine = sqlalchemy.create_engine("mysql+pymysql://root:root@127.0.0.1:3306/app", encoding="utf8",
                                  echo=False)
DBSessinon = sqlalchemy.orm.sessionmaker(bind=engine)
db_session = DBSessinon()


def find_user_by_login_name(login_name):
    if not login_name:
        return False
    query = db_session.query(UserInfoModel)
    query = query.filter(UserInfoModel.login_name == login_name)
    query = query.first()
    if query:
        return query.to_dict()
    return None
