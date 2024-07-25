# -*- coding: utf-8 -*-
# settings.py - 存放项目的路径配置信息
from pathlib import Path

# 项目根目录
PROJECT_ROOT_PATH = Path(__file__).absolute().parent.parent

# 配置文件路径
LOG_FILE_PATH = PROJECT_ROOT_PATH / "logs/record_{time}.log"
IP_PORT_INFO_FILE_PATH = PROJECT_ROOT_PATH / "config/Socket_Info"
WIFI_INFO_FILE_PATH = PROJECT_ROOT_PATH / "config/WiFi_Info"

# 图标路径
WINDOWS_ICON_PATH = PROJECT_ROOT_PATH / "assets/icons/Robot_arm_log.png"