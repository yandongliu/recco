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

def _getVidFolderPrefix(vid):
    if len(vid) > 2:
        prefix = vid[:2]
        return prefix
    else:
        return vid

def saveHTMLToDisk(vid, html):
    fn = '{}/{}/{}.html'.format(HTML_DIR, _getVidFolderPrefix(vid), vid)
    ensure_dir(fn)
    with open(fn, 'w') as f:
        f.write(html)

def loadHTMLFromDisk(vid):
    s = None
    with open('{}/{}/{}.html'.format(HTML_DIR, _getVidFolderPrefix(vid), vid), 'r') as f:
        s = f.read()
    return s

def saveViewsToDisk(vid, videos):
    """Save video's co-views to disk
    :param [(vid, title, view-count)] videos:
    """
    fn = '{}/{}/{}.txt'.format(VIEW_DIR, _getVidFolderPrefix(vid), vid)
    ensure_dir(fn)
    with open(fn, 'w') as f:
        for v_, t_, c_ in videos:
            print v_, t_, c_
            f.write('{};;{};;{}\n'.format(v_, t_.encode('utf8'), c_))

def saveVideoMetas(metas):
    """Save video metas for disk
    :param dict(video, [title, count]) metas"""
    fn = '{}/{}.txt'.format(DATA_DIR, 'video_meta.txt')
    with open(fn, 'w') as f:
        for vid in metas:
            title, count = metas[vid]
            f.write('{};;{};;{}\n'.format(vid, title.encode('utf8'), count))

def loadViewsFromDisk(vid):
    """Load co-views for a video id"""
    ret = []
    with open('{}/{}/{}.txt'.format(VIEW_DIR, _getVidFolderPrefix(vid), vid), 'r') as f:
        for l in f.read().strip().split('\n'):
            # print '-'*10, l
            v, t = l.strip().split(';;', 1)
            ret.append((v,t))
    return ret

def doesVidExist(vid):
    path = '{}/{}/{}.txt'.format(VIEW_DIR, _getVidFolderPrefix(vid), vid)
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
    print loadViewsFromDisk('0KSOMA3QBU0')
