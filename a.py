import time
import os
ISOTIMEFORMAT='%Y.%m.%d-%H'
# print(time.strftime( ISOTIMEFORMAT, time.localtime() ))
root = 'e:/workSpace/待传/'
pre = 'dingdingjinfu_'
time = time.strftime( ISOTIMEFORMAT, time.localtime() )
ft = input("1-正式;2-测试\n")
if ft=='1':
    ft = '正式'
else :
    ft = '测试'
path = root + pre + time + '_王磊_'+ft+'/dingdingjinfu/'
try:
    os.makedirs(path)
    path =  'd:/SoftWare/SystemSW/TotalCommanderPortable/tc900x64/TOTALCMD64.EXE /O /T /L ' + path
    os.system(path)
except Exception as e:
    print('文件已存在!')
os.system('pause')
