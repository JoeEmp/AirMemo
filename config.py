import logging

# pro
'''
logging.basicConfig(level=logging.WARNING, filename='log.txt', filemode='a',
                    format='%(asctime)s %(levelname)s %(filename)s %(funcName)s %(message)s')
'''
# dev
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(filename)s %(funcName)s %(message)s')

#隐藏速度
SPEED = 0.001


# 公共长宽标准
# 详情编辑框大小
COM_TE_WIDTH = 320
COM_TE_HEIGHT = 250

# 通用按钮宽度
COM_BTN_WIDTH = 25
COM_BTN_HEIGHT = 25

# 小按钮长宽
COM_MICRO_BTN_WIDTH = 20
COM_MICRO_BTN_HEIGHT = 20

# 本地数据库位置
LDB_FILENAME = 'AirMemo.db'

# 等分比    窗口大小=屏幕尺寸/width
DIVIDE = {'width': 6}

# 尺寸模式 使用像素(pixel)或者等分(divide)
SIZEMODE = 'pixel'

WIDGET_FLAG = False

# 主窗口设置 main.py

MAIN_WELT_BTN_WIDTH = 60

MAIN_BASEWIDTH = MAIN_WELT_BTN_WIDTH + COM_TE_WIDTH

# icon
LOGIN_ICON = './icon/user.ico'

SYNC_ICON = './icon/Sync.ico'

HOMO_ICON = './icon/recycle.svg'

TITLE_ICON = './icon/title.svg'

HIDE_ICON = './icon/hide.ico'

SHOW_ICON = './icon/show.ico'

CLOSE_ICON = './icon/close_btn.png'

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

EMAIL_HEIGHT = RECIPIENT_TX_HEIGHT + COPY_TE_HEIGHT + MSG_TE_HEIGHT + DETAIL_TE_HEIGHT + SEND_BTN_HEIGHT + 100
