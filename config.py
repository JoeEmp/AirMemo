import logging

logging.basicConfig(level=logging.WARNING, format='%(asctime)s %(levelname)s %(filename)s %(funcName)s %(message)s')

# 详情编辑框大小
TEXT_WIDTH = 320
TEXT_HEIGHT = 250

# 隐藏按钮宽度
WELT_BTN_WIDTH = 60

# 通用按钮宽度
BTN_WIDTH = 25
BTN_HEIGHT = 25

# 小按钮长宽
MICRO_BTN_WIDTH = 20
MICRO_BTN_HEIGHT = 20

BASEWIDTH = WELT_BTN_WIDTH + TEXT_WIDTH

# 本地数据库位置
LDB_FILENAME = 'AirMemo.db'

# 等分比    窗口大小=屏幕尺寸/width
DIVIDE = {'width': 6}

# 尺寸模式 使用像素(pixel)或者等分(divide)
SIZEMODE = 'pixel'

WIDGET_FLAG = False

LOGIN_ICON = './icon/user.ico'

SYNC_ICON = './icon/Sync.ico'

HOMO_ICON = './icon/recycle.svg'

TITLE_ICON = './icon/title.svg'

HIDE_ICON = './icon/hide.ico'

SHOW_ICON = './icon/show.ico'

CLOSE_ICON = './icon/close_btn.png'
