import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import pymysql

# 初始化web应用
app = Flask(__name__, instance_relative_config=True)

# 启用CORS
CORS(app)

# 数据库连接 — 优先使用 DATABASE_URL 环境变量，默认 SQLite
DB_URI = os.environ.get('DATABASE_URL')
if DB_URI is None:
    DB_URI = 'sqlite:///' + os.path.join(os.path.dirname(os.path.dirname(__file__)), 'app.db')

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

# 如果配置了 MySQL，使用 pymysql 驱动
if DB_URI and DB_URI.startswith('mysql'):
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
