from __future__ import absolute_import

import os
import sys
sys.path.append('/home/yandong/projects/youtube')

from recco.lib import util, youtube

MAX = 10000000

def run():
    cnt = 0
    for prefix in os.listdir(util.HTML_DIR):
        if cnt > MAX: break
        for f in os.listdir(util.HTML_DIR + '/' + prefix):
            vid = f[:-5]
            print vid
            html = util.loadHTMLFromDisk(vid)
            videos = youtube.Youtube.parseYoutubePage(html)
            util.saveViewsToDisk(vid, videos)
            cnt += 1
            if cnt % 1000 == 0:
                print cnt
                util.saveVideoMetas(youtube.x_video_meta)
    # print youtube.x_video_meta
    util.saveVideoMetas(youtube.x_video_meta)

def debug(vid):
    html = util.loadHTMLFromDisk(vid)
    # print html
    youtube.Youtube.parseYoutubePage(html)

if __name__ == '__main__':
    debug('nCGrisXaGC4')
    run()
