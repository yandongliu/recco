import os
import sys
import random
import time
import urllib2

from bs4 import BeautifulSoup

URL_PREFIX= 'https://www.youtube.com/watch?v='
DATA_DIR = os.path.join(os.path.dirname(__file__), '../../data')
VIEW_DIR = os.path.join(DATA_DIR, 'view')
HTML_DIR = os.path.join(DATA_DIR, 'html')


def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        print 'making dir', d
        os.makedirs(d)

def getVidFolderPrefix(vid):
    if len(vid) > 2:
        prefix = vid[:2]
        return prefix
    else:
        return vid

def saveHTMLToDisk(vid, html):
    fn = '{}/{}/{}.html'.format(HTML_DIR, getVidFolderPrefix(vid), vid)
    ensure_dir(fn)
    with open(fn, 'w') as f:
        f.write(html)

def loadHTMLFromDisk(vid):
    s = None
    with open('{}/{}/{}.html'.format(HTML_DIR, getVidFolderPrefix(vid), vid), 'r') as f:
        s = f.read()
    return s

def saveToDisk(vid, videos):
    fn = '{}/{}/{}.txt'.format(VIEW_DIR, getVidFolderPrefix(vid), vid)
    ensure_dir(fn)
    with open(fn, 'w') as f:
        for v_, t_ in videos:
            print v_, t_
            f.write('{};;{}\n'.format(v_, t_.encode('utf8')))

def loadFromDisk(vid):
    ret = []
    with open('{}/{}/{}.txt'.format(VIEW_DIR, getVidFolderPrefix(vid), vid), 'r') as f:
        for l in f.read().strip().split('\n'):
            print '-'*10, l
            v, t = l.strip().split(';;', 1)
            ret.append((v,t))
    return ret

def doesVidExist(vid):
    path = '{}/{}/{}.txt'.format(VIEW_DIR, getVidFolderPrefix(vid), vid)
    return os.path.isfile(path) 

def downloadFromUrl(url):
    response = urllib2.urlopen(url)
    html = response.read()
    return html

def readFromFile(fn):
    with open(fn, 'r') as f:
        s = f.read()
    return s

def downloadForVideo(vid):
    html = downloadFromUrl(URL_PREFIX + vid)
    saveHTMLToDisk(vid, html)
    return html

def waitRandomly(x=5, y=20):
    slep = random.randint(x,y)
    print 'waiting', slep, 'seconds'
    time.sleep(slep)


if __name__ == '__main__':
    print loadFromDisk('0KSOMA3QBU0')
