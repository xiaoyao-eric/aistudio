# 创建应用实例
import sys

from server import app
from config import APP_PORT, APP_DEBUG

# 启动Flask Web服务
if __name__ == '__main__':
    app.run(host='localhost', port=APP_PORT, debug=APP_DEBUG)