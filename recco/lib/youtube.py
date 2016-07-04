import re

from bs4 import BeautifulSoup

p_vid = '/watch\?v=(.*)'


class Youtube(object):

    @staticmethod
    def parseYoutubePage(html):
        ret = []
        parsed_html = BeautifulSoup(html, "html.parser")
        views = parsed_html.find_all('a', class_='spf-link')
        for v in views:
            if 'content-link' in v['class']:
                # print v['href'], v['title']
                m = re.match(p_vid, v['href'])
                if m:
                    ret.append((m.group(1), v['title']))
        return ret


def scrapeVideo(vid):
    print 'scraping', vid
    if doesVidExist(vid):
        print 'video exists', vid
        try:
            videos = loadFromDisk(vid)
        except Exception as ex:
            print 'Error in loading videos from disk', vid, ex
            raise
    else:
        html = downloadForVideo(vid)
        videos = parseYoutubePage(html)
        waitRandomly()
        saveToDisk(vid, videos)
    print videos

    for vid, _ in videos:
        scrapeVideo(vid)
        # html_ = downloadForVideo(vid)
        # videos_ = parseYoutubePage(html_)
        # saveToDisk(vid, videos)
        # waitRandomly()
