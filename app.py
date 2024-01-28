import os
import shutil
from datetime import datetime

SOURCE_DIR = 'C:/Users/원본파일.txt'  # 원본 파일 경로. 확장자 포함
TARGET_FOLDER = 'C:/Users/backup' # 복사될 폴더의 위치 
FILE_NAME = '파일.txt' #만들어질 파일 이름. 확장자 포함


today = datetime.now().strftime("%y%m%d")
target = os.path.join(TARGET_FOLDER, today) 

if not os.path.exists(target):
    os.makedirs(target)

src = SOURCE_DIR 
file = os.path.join(target, FILE_NAME)

shutil.copy(src, file)

