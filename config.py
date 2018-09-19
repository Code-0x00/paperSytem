import json
import os
import platform


def config_get():
    if not os.path.exists('.config'):
        default_config={}
        system = platform.system()
        if system=='Linux':
            default_config['file_dir_path']= '/home/xhq/Papers/'
            default_config['chrome_path']="evince"
        elif system=='Windows':
            default_config['file_dir_path']= 'C:/XLIB/Papers/'
            default_config['chrome_path']="C:/Users/xhq/AppData/Local/Google/Chrome/Application/chrome.exe"
        else:
            default_config['file_dir_path'] = './'
            default_config['chrome_path'] = "./"
        json.dump(default_config, '.config')
        return default_config
    current_config = json.load('.config')
    return current_config
