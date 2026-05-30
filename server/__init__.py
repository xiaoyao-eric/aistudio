import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import pymysql

# 初始化web应用
app = Flask(__name__, instance_relative_config=True)

# 启用CORS
CORS(app)

# 数据库连接 — 敏感信息从环境变量读取，避免硬编码
DB_USER = os.environ.get('DB_USER', 'root')
DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_NAME = os.environ.get('DB_NAME', 'omnieye')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}'.format(
    DB_USER, DB_PASSWORD, DB_HOST, DB_NAME
)

# 因MySQLDB不支持Python3，使用pymysql扩展库代替MySQLDB库
pymysql.install_as_MySQLdb()

# 初始化DB操作对象
db = SQLAlchemy(app)

# 导入模型（必须在 db 之后）
from server.models import Region  # noqa

# 加载控制器
from server import httpserver  # noqa

# 启动时自动建表并初始化数据
with app.app_context():
    db.create_all()
    from server.seed_data import init_data  # noqa
    init_data()
