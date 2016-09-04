"""Change view files from vid;;title to vid only. Seems unnecessary"""
from __future__ import absolute_import

import os
from os import path
from subprocess import call
import sys
sys.path.append('/home/yandong/projects/youtube')

from recco.lib import util

MAX = 10000


def run():
    cnt = 0
    for prefix in os.listdir(util.VIEW_DIR):
        if cnt > MAX: break
        for f in os.listdir(util.VIEW_DIR + '/' + prefix):
            vid = f[:-4]
            print vid
            views = util.loadViewsFromDisk(vid)
            # print views
            # videos = youtube.Youtube.parseYoutubePage(html)
            # util.saveViewsToDisk(vid, videos)
            cnt += 1
            if cnt % 1000 == 0:
                print cnt
                # util.saveVideoMetas(youtube.x_video_meta)
    # print youtube.x_video_meta
    # util.saveVideoMetas(youtube.x_video_meta)

if __name__ == '__main__':
    # move_view_files()
    run()
