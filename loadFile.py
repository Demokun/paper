import os
filePath = 'D:\data'
os.listdir(filePath)
for info in os.listdir(filePath):
    domain = os.path.abspath(filePath)
    info = os.path.join(domain,info)
    info = open(info,'r')
    print(info.read())
    info.close()