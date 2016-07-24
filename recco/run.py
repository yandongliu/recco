from __future__ import absolute_import

import sys
sys.path.append('/home/yandong/projects/youtube')

from recco.lib.scraper import Scraper


if __name__ == '__main__':
    vid = 'RgKAFK5djSk'  # see you again
    vid = 'ocDo3ySyHSI'  # qian li zhi wai
    vid = '450p7goxZqg'  # all of me
    vid = 'CnI_LuCJ4Ek'  # i got a woman
    scraper = Scraper(vid)
    scraper.scrape()
