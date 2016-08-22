#coding=utf8
import requests
from requests import Session, Request
import lxml
from bs4 import BeautifulSoup
import pymongo
from multiprocessing import Pool,Process
import time

BASE_URL = 'https://www.sec.gov/Archives/edgar/monthly/'
conn = pymongo.MongoClient("127.0.0.1", 27017, connect=False)
consur = conn.secCom


def downUrlRetrieve(dirName, url, fileName, files):
    '''
    下载URL
    '''
    print "downloading with requests"
    try:
        r = requests.get(url)
        import os
        fileDir = os.path.join(os.path.expanduser("~"), 'Desktop/10k/%s'%(dirName,))
        if not os.path.exists(fileDir):
            os.makedirs(fileDir)
            print '创建目录。。', fileDir
        desktopPath = os.path.join(os.path.expanduser("~"), 'Desktop/10k/%s/%s'%(dirName, fileName,))
        print '-------------' + desktopPath
        print  time.strftime('%Y-%m-%d %X', time.localtime( time.time() ) )
        with open(desktopPath, "wb") as code:
            code.write(r.content)
    except Exception,e :
        print e
        print "+++++++++++++++++++++++++++++++++++++"
        consur.fail.insert(files)
        print '错误!插入数据库'



pool = Pool(5)
noFiles = 0
itemCount = 0
dirCount = 0
for path in consur.xmltest.find():
    dirCount += 1
    try:
        files = path['files']
        for file in files:
            itemCount += 1
            if path['description'] == '10-K':
                suff = file['fileName'].split('.')[-1]
                if  suff == 'xml' or suff =='xsd' or suff == 'cal' or suff == 'lab' or suff == 'pre':
                    pool.apply_async(downUrlRetrieve, args=(path['period']+'#'+ path['companyName'].strip(' DE '),file['url'],file['fileName'], files))

    except Exception ,e:
        print e
        print '不存在files数据项'
        noFiles += 1

pool.close()
pool.join()

print noFiles, itemCount, dirCount
