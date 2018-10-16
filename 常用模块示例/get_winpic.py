"""
自动抓取Windows聚焦图片
"""
import os
import time
import shutil

old_path = r'C:\Users\13928\AppData\Local\Packages' \
           r'\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'
new_path = r'C:\Users\13928\Desktop'
os.chdir(old_path)
pic_list = os.listdir(old_path)
# print(pic_list)
pic_list_sorted = sorted(pic_list, key=lambda x: os.stat(x)[-2])
new_name = time.strftime('%Y%m%d%H%M')
for i in pic_list_sorted[-7:]:
    shutil.copyfile(i, new_path+'/'+new_name+'.jpg')
    new_name = str(int(new_name)+1)
