from icrawler import ImageDownloader
from icrawler.builtin import GoogleImageCrawler


class CustomLinkPrinter(ImageDownloader):
    file_urls = []

    def get_filename(self, task, default_ext):
        file_idx = self.fetched_num + self.file_idx_offset
        return '{:04d}.{}'.format(file_idx, default_ext)

    def download(self, task, default_ext, timeout=5, max_retry=3, overwrite=False, **kwargs):
        file_url = task['file_url']
        filename = self.get_filename(task, default_ext)

        task['success'] = True
        task['filename'] = filename

        if not self.signal.get('reach_max_num'):
            self.file_urls.append(file_url)

        self.fetched_num += 1

        if self.reach_max_num():
            self.signal.set(reach_max_num=True)

        return


def get_img_url(req):
    google_crawler = GoogleImageCrawler(downloader_cls=CustomLinkPrinter)
    google_crawler.downloader.file_urls = []
    google_crawler.crawl(keyword=req, max_num=10)
    file_urls = google_crawler.downloader.file_urls

    if file_urls:
        return file_urls


def main():
    print(get_img_url('raid заточка'))


if __name__ == '__main__':
    main()
