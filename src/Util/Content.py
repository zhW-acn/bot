import os
import nonebot_plugin_localstore as store
from nonebot import require

require("nonebot_plugin_localstore")

def getQQInfoJSONPath(userid :int):
    return 'C:\\Users\\22408\\AppData\\Local\\nonebot2' + os.sep + "QQInfo" + os.sep + userid.__str__() + ".json"
