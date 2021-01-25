#coding:utf-8
import os
import linecache
def get_content(path):
    '''
    读取缓存中的文件内容，以字符串的方式返回
    :param path:
    :return:
    '''
    if os.path.exists(path):
        content=""
        cache_data=linecache.getlines(path)
        for line in range(len(cache_data)):
            content +=cache_data[line]
        return content
    else:
        print('the path[{}] is not exit!'.format(path))

def main():
    path='C:\\Users\\TEST\\Desktop\\sn.txt'
    content=get_content(path)
    print(content)

if __name__ == '__main__':
    main()







