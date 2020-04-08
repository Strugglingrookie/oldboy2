#coding=utf-8
import os,datetime,sys

log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"logs")

def log(level,content,where):
    now = str(datetime.datetime.today())
    today = str(datetime.datetime.today().date())
    filePath = os.path.join(log_path,'log_'+today+'.log')
    isErr = False
    try:
        content = content.decode("utf-8")
    except:
        isErr = True
    if isErr:
        try:
            content = content.decode(sys.getfilesystemencoding())
        except:
            pass
    with open(filePath,'a') as f:
        f.write(('[%s][%s]%s [IN %s]\n'%(level,now,content,where)).encode(sys.getfilesystemencoding()))

def error(msg,where='unknown'):
    log('ERROR',msg,where)

def info(msg,where='unknown'):
    log('INFO', msg, where)

def warning(msg,where='unknown'):
    log('WARNING', msg, where)


if __name__=='__main__':
    error('你的文件没有访问权限！','line 15-line 19')
    info('访问http://www.baidu.com')
    warning('删除/x/y/z成功！')