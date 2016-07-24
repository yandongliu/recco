from recco.lib import util
from recco.lib.youtube import Youtube


class Scraper(object):
    def __init__(self, vid):
        self.queue = []
        self.queue.append(vid)

    def scrape(self):
        while(len(self.queue) > 0):
            vid = self.queue.pop(0)
            if util.doesVidExist(vid):
                print 'video exists', vid
                videos = util.loadViewsFromDisk(vid)
            else:
                print 'downloading video', vid
                html = util.downloadForVideo(vid)
                videos = Youtube.parseYoutubePage(html)
                if videos:
                    util.saveViewsToDisk(vid, videos)
                    util.waitRandomly()
            for v, _ in videos:
                if v not in self.queue:
                    self.queue.append(v)
