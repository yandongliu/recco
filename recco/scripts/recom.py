from __future__ import absolute_import

from collections import defaultdict
import os
from os import path
import sys

import numpy as np

sys.path.append('/home/yandong/projects/youtube')
from recco.lib import util
from recco.lib.youtube import Youtube


DEBUG = True
MAX = 100

def loadAllVideos():
    x_coviews = defaultdict(list)
    x_title_vid = {}
    for prefix in os.listdir(util.VIEW_DIR):
        if len(x_coviews) > MAX: break
        for f in os.listdir(util.VIEW_DIR + '/' + prefix):
            vid = f[:-4]
            print vid
            # x_coviews[vid] = []
            try:
                objs = util.loadViewsFromDisk(vid)
                # for vid, title in objs:
                #    x_coviews[vid].append((vid, title))
                # print vids
                # print x_coviews[vid]
                # html = util.loadHTMLFromDisk(vid)
                # videos = Youtube.parseYoutubePage(html)
                # views = Youtube.getViewCount(html)
                # x[vid] = videos
                x_coviews[vid] = objs
            except Exception as ex:
                print ex
    return x_coviews


if __name__ == '__main__':
    vid = 'RgKAFK5djSk'
    x_vid, x_title = util.loadVideoMetas()
    print x_vid[vid]
    # print len(x_vid)
    print util.loadViewsFromDisk(vid)
    # print len(x_title)
    # for vid in x_coviews:
    #    print vid, x_coviews[vid]

