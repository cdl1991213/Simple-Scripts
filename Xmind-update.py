# 以管理员身份运行文件，实现xmind破解

import shutil

# 复制并覆盖hosts文件
shutil.copy2('D:/Study/XMind/hosts', 'C:/Windows/System32/drivers/etc/hosts')

# 复制并覆盖account.json文件
shutil.copy2('D:/Study/XMind/account.json', 'C:/Users/ChenDlung/AppData/Roaming/XMind/Electron v3/vana/state/account.json')
