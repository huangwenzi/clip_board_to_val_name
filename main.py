import win32clipboard as w
import win32con
from pynput import keyboard
import json


# 获取剪切板
def get_text():
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d.decode('GBK')

# 设置剪切板
def set_text(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()

# 键盘事件
def on_press(key):
    if print_key:
        print(key)
        
    # 是否是快捷键
    if key != keyboard.Key[replace_key]:
        return
    
    # 检查长度
    text:str = get_text()
    if len(text) > replace_len:
        return
    
    # 检查类型
    status = False
    new_text = ""
    if replace_type == 1:
        text_list:list = text.split("_")
        if len(text_list) > 0:
            for item in text_list:
                new_text += (item[0].upper() + item[1:])
            status = True
    else:
        return

    if status:
        print(new_text)
        set_text(new_text)
    

# 加载配置
cfg = {}
with open("./cfg.json", encoding="utf8") as f:
    cfg = json.load(f)
replace_key = cfg["replace_key"]
replace_type = cfg["replace_type"]
replace_len = cfg["replace_len"]
print_key = cfg["print_key"]

# 开始监听
print("begin")
with keyboard.Listener(on_press=on_press) as lsn:
    lsn.join()
