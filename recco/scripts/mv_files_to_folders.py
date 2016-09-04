from __future__ import absolute_import

import os
from os import path
from subprocess import call
import sys
sys.path.append('/home/yandong/projects/youtube')
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from recco.lib import util


def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        print 'making dir', d
        os.makedirs(d)

def move_view_files():
    for f in os.listdir(util.VIEW_DIR):
        if path.isfile(path.join(util.VIEW_DIR, f)):
            ensure_dir(util.VIEW_DIR + '/' + util.getVidFolderPrefix(f) + '/' + f)
            print 'mv', util.VIEW_DIR + '/' + f, util.VIEW_DIR + '/' + util.getVidFolderPrefix(f) + '/' + f
            call(['mv', util.VIEW_DIR + '/' + f, util.VIEW_DIR + '/' + util.getVidFolderPrefix(f) + '/' + f])


def move_html_files():
    for f in os.listdir(util.HTML_DIR):
        if path.isfile(path.join(util.HTML_DIR, f)):
            ensure_dir(util.HTML_DIR + '/' + util.getVidFolderPrefix(f) + '/' + f)
            print 'mv', util.HTML_DIR + '/' + f, util.HTML_DIR + '/' + util.getVidFolderPrefix(f) + '/' + f
            call(['mv', util.HTML_DIR + '/' + f, util.HTML_DIR + '/' + util.getVidFolderPrefix(f) + '/' + f])


if __name__ == '__main__':
    # move_view_files()
    move_html_files()
