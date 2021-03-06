#coding=utf8
import os
import codecs

class MDSort():
    def __init__(self):
        self.global_sortkeys = {}
        self.path = 'propertyList.txt'
        self.doSomething(self.path)

    def doSomething(self, path):
        list = self.reverseFile(path)
        for idx in range(len(list)):
            self.global_sortkeys[list[idx]] = idx

    @classmethod
    def reverseFile(self, filePath):
        '''
        遍历文件
        :param filePath: 文件路径
        :return: 句子列表
        '''
        sentenceList = []
        with codecs.open(filePath, 'r', 'utf8') as file:
            for line in file.readlines():
                line = line.strip()
                sentenceList.append(line)
        return sentenceList

    def sortTag(self, list):
        try:
            return sorted(list, lambda x,y:cmp(self.global_sortkeys[x],self.global_sortkeys[y]))
        except Exception, e:
            print 'sortTag....error'
            print list
            print e


if __name__ == "__main__":
    list = ["Rg", "month", "gwhub", "day", "year"]





