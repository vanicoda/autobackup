import os
import shutil
from datetime import datetime
import configparser

config = configparser.ConfigParser()
config.read('settings.ini')

source_dir = config['settings']['SOURCE_DIR']
target_folder = config['settings']['TARGET_FOLDER']
file_name = config['settings']['FILE_NAME']
date_format = config['settings']['DATE_FORMAT']

today = datetime.now().strftime(date_format)
target = os.path.join(target_folder, today) 

if not os.path.exists(target):
    os.makedirs(target)

src = source_dir 
file = os.path.join(target, file_name)

shutil.copy(src, file)

