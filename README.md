# clip_board_to_val_name

# 剪切板内容替换成变量名

## 使用方法
运行后按f8会自动把剪切板内容替换成变量名

## 支持配置
cfg.json
replace_key: 替换的快捷键  
replace_type: 替换类型 1、aa_bb => AaBb  
replace_len: 替换的字符串长度上限

## 关于exe
可以直接使用打包好的main.exe  
大佬也可以修改代码后自行打包  
pyinstaller -F 文件名.py  
pyinstaller -F main.py  
