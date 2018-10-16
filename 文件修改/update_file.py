"""
实现文件修改的两种方式
"""
# 占内存
f_name = '员工信息（utf-8）.txt'
old_str = '杜姗姗'
new_str = '杜  姗'
f = open(f_name, 'r+', encoding='utf-8')
data = f.read()
if old_str in data:
    data = data.replace(old_str, new_str)
f.truncate(0)
f.write(data)
f.close()


# 占硬盘
import os
f_name = '员工信息（utf-8）.txt'
f_new_name = '员工信息（utf-8）new.txt'
old_str = '杜姗姗'
new_str = '杜  姗'
f = open(f_name, 'r', encoding='utf-8')
f_new = open(f_new_name, 'w', encoding='utf-8')
for line in f:
    if old_str in line:
        line = line.replace(old_str, new_str)
    f_new.write(line)
f.close()
f_new.close()
os.remove(f_name)
os.rename(f_new_name, f_name)
