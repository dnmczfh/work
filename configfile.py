#读写配置文件
import os
import configparser

# 记录配置文件的全路径名
cfgFile = os.path.abspath('path4.ini')
config = configparser.ConfigParser()
config.read(cfgFile)

# 从配置文件中读取设置信息
if os.path.isfile(cfgFile):  # 判断文件是否存在
    # 从文件中读取配置信息
    try:
        currentPath = config['Path']['Target']
        Select = config['Path']['Select']
        FileName = config['File']['Name']
    except NameError as e:
        print('配置信息未定义:', e)
    except Exception as e:
        print('错误信息:', e)
else:
    print(cfgFile, '不存在')
    config.add_section('Path')
    config['Path']['Target'] = os.getcwd()
    config['Path']['Select'] = 'Y'
    config.add_section('File')
    config['File']['Name'] = 'file_list.xlsx'
    config.write(open(cfgFile, "w"))
    print(cfgFile, '已经重新生成')

