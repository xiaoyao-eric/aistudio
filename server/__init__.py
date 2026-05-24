from flask import Flask
from flask_cors import CORS
import config

# 初始化web应用
app = Flask(__name__, instance_relative_config=True)

# 启用CORS
CORS(app)

# 加载控制器
from server import httpserver