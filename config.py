import os
import logging
import logging.handlers

BASE_DIR = os.path.dirname(__file__)


def config_log():
    # 1. 获取日志器
    root = logging.getLogger()
    root.setLevel(logging.INFO)  # 自行定义

    # 2. 定义处理器
    cmd = logging.StreamHandler()
    file = logging.handlers.TimedRotatingFileHandler(BASE_DIR + os.sep + 'log/haier_log.log', when='midnight', backupCount=3, encoding='utf-8')
    # 3. 定义格式器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 4. 将格式器添加到处理器中
    cmd.setFormatter(formatter)
    file.setFormatter(formatter)
    # 5. 将处理器添加带日志器中
    root.addHandler(cmd)
    root.addHandler(file)