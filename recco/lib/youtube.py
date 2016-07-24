import re

from bs4 import BeautifulSoup

p_vid = '/watch\?v=(.*)'
p_views = '([\d,]+) views'

x_video_meta = {}


class Youtube(object):

    @classmethod
    def parseYoutubePage(cls, html):
        """Parse HTML content and return [(vid, title, view_count)]"""
        ret = []
        parsed_html = BeautifulSoup(html, "html.parser")
        views = parsed_html.find_all('a', class_='spf-link')
        for v in views:
            if 'content-link' in v['class']:
                view_count = v.find('span', class_='view-count').text[0:-6]
                m = re.match(p_vid, v['href'])
                if m:
                    ret.append((m.group(1), v['title'], view_count))
                    x_video_meta[m.group(1)] =  (v['title'], view_count)
        return ret

    @staticmethod
    def getViewCount(html, parsed=False):
        if not parsed:
            html = BeautifulSoup(html, "html.parser")
        views = html.find_all('div', class_='watch-view-count')
        for v in views:
            m = re.match(p_views, v.text)
            if m:
                return int(m.group(1).replace(',', ''))
        return 0

if __name__ == '__main__':
    import sys
    sys.path.append('.')
    from recco.lib import util
    html = util.loadHTMLFromDisk('450p7goxZqg')
    print Youtube.parseYoutubePage(html)
