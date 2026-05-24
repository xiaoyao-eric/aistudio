# 创建应用实例
import os
import sys

from server import app
from config import APP_PORT, APP_DEBUG

# 启动Flask Web服务
if __name__ == '__main__':
    host = os.environ.get('APP_HOST', 'localhost')
    app.run(host=host, port=APP_PORT, debug=APP_DEBUG)