#coding=utf8
import requests
from requests import Session, Request
from multiprocessing import Pool,Process
import time
import re
import os
import urllib
import wget
import random
import os
BASE_URL = 'http://www.hotelaah.com/liren/index.html'

IPANDPORT = []
# 获取代理列表
def getTheRemoteAgent():
    listUrl = os.path.join(os.path.expanduser('~'), 'Desktop/proxy_list.txt')
    f = open(listUrl, "r")
    for line in f:
        IPANDPORT.append(line)
    f.close()

def downUrlRetrieve(dirPath, url, fileName):
    '''
    下载URL
    '''
    print "downloading with requests"
    index = random.randint(0, len(IPANDPORT) - 1)
    proxy = {'http': 'http://%s' % IPANDPORT[index].strip()}
    print proxy

    try:
        r = requests.get(url, proxy=proxy)
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)
            print '创建目录。。', dirPath
        desktopPath = os.path.join(dirPath, fileName)

        if os.path.exists(desktopPath):
            print '文件名重复'
            desktopPath = desktopPath + '_1.doc'
        print '-------------' + desktopPath
        print  time.strftime('%Y-%m-%d %X', time.localtime( time.time() ) )
        with open(desktopPath, "wb") as code:
            # code.write(MDCompressFile.gzip_compress(r.content))
            code.write(r.content)
    except Exception,e :
        print e
        print '出错了..'


if __name__ == "__main__":

    targetURL = 'http://www.csrc.gov.cn/pub/newsite/fxjgb/scgkfxfkyj/'
    fileURL = os.path.join(os.path.expanduser('~'), 'Desktop/files.txt')
    dirPath = os.path.join(os.path.expanduser('~'), 'Desktop/files')
    getTheRemoteAgent()

    pool = Pool(5)
    import codecs
    with codecs.open(fileURL, encoding='utf8') as file:
        for line in file.readlines():
            arr = line.strip().split('##')
            fileURL = arr[0]
            fileName = arr[-1]
            print fileURL, fileName
            pool.apply_async(downUrlRetrieve, args=(dirPath,targetURL +'/'+ fileURL, fileName))
    pool.close()
    pool.join()

