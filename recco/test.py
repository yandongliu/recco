from __future__ import absolute_import

import sys

from lib.util import Util, URL_PREFIX
from lib.youtube import Youtube

def debug_loadHTMLFromDisk(fn):
    print fn
    ret = []
    with open(fn, 'r') as f:
        try:
            for l in f.read().strip().split('\n'):
                v, t = l.strip().split(';;', 1)
                ret.append((v,t))
        except Exception as ex:
            print fn, ex
    return ret


# html = Util.downloadForVideo('exdhL2AMZ3Q')
html = Util.loadHTMLFromDisk(sys.argv[1])
print html
videos = Youtube.parseYoutubePage(html)
print videos
