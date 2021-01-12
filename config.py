import sys
import logging
from enum import Enum,unique

try:
    ENV = sys.argv[1]
except IndexError:
    ENV = 'debug'

PROTOCOL = 'http://'
@unique
class DOMAINS(Enum):
    debug = 'localhost:5000'
    pro = 'todo.winn.online:5000'


@unique
class LOG_LEVEL(Enum):
    debug = logging.INFO
    pro = logging.WARNING


logging.basicConfig(filename='AirMemo.log', level=LOG_LEVEL[ENV].value,
                    format='%(asctime)s %(levelname)s %(filename)s %(funcName)s %(message)s')

# 供调试使用
proxies = {
    'http': 'http://0.0.0.0:8888/',
    'https': 'https://0.0.0.0:8888/'
}


##### UI CONFIG #####

# 隐藏速度
SPEED = 0.001

# 公共长宽标准
# 详情编辑框大小
COM_TE_WIDTH = 320
COM_TE_HEIGHT = 250

# 通用按钮宽度
COM_BTN_WIDTH = 25
COM_BTN_HEIGHT = 25

# 小按钮长宽
COM_MICRO_BTN_WIDTH = 23
COM_MICRO_BTN_HEIGHT = 23

# 本地数据库位置
LDB_FILENAME = 'AirMemo.db'

# 等分比    窗口大小=屏幕尺寸/width
DIVIDE = {'width': 6}

# 尺寸模式 使用像素(pixel)或者等分(divide)
SIZEMODE = 'pixel'

WIDGET_FLAG = False

# 主窗口设置 main_win.py

MAIN_WELT_BTN_WIDTH = 60

MAIN_BASEWIDTH = MAIN_WELT_BTN_WIDTH + COM_TE_WIDTH

# icon
LOGIN_ICON = './icon/user.svg'

SYNC_ICON = './icon/cloud-sync.svg'

HOMO_ICON = './icon/delete.svg'

TITLE_ICON = './icon/title.svg'

WELT_ICON = './icon/double-right.svg'

SHOW_ICON = './icon/double-left.svg'

CLOSE_ICON = './icon/close.svg'

ADD_ICON = ''

UP_ICOM = './icon/up.svg'

DOWN_ICON = './icon/down.svg'

LEFT_ICON = './icon/left.svg'

RIGHT_ICON = './icon/right.svg'

# 邮箱窗口设置 email.py
RECIPIENT_TX_HEIGHT = 25

COPY_TE_HEIGHT = 25

MSG_TE_HEIGHT = 25

DETAIL_TE_HEIGHT = 70

SEND_BTN_WIDTH = 70

SEND_BTN_HEIGHT = COM_BTN_HEIGHT

EMAIL_TE_WIDTH = 300

EMAIL_LAB_WIDTH = 50

EMAIL_WIDTH = 450

EMAIL_HEIGHT = RECIPIENT_TX_HEIGHT + COPY_TE_HEIGHT + \
    MSG_TE_HEIGHT + DETAIL_TE_HEIGHT + SEND_BTN_HEIGHT + 100
