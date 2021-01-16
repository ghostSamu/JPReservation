# -*- coding: utf-8 -*-

# Scrapy settings for PostReservation project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'PostReservation'

SPIDER_MODULES = ['PostReservation.spiders']
NEWSPIDER_MODULE = 'PostReservation.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'PostReservation (+http://www.yourdomain.com)'

# Obey robots.txt rules
SPLASH_URL = 'http://localhost:8050'

DUPEFILTER_CLASS='scrapy_splash.SplashAwareDu' \
                 'peFilter'

ROBOTSTXT_OBEY = False

# USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'

USER_AGENT = 'MOZilla/5.0(x11; Linux x86_64; rv:7.0.1)Gecko/20100101 Firefox/7.7'



DEFAULT_REQUEST_HEADERS = {
  # 'method':'POST',
  # 'Accept': 'application/json, text/plain, */*',
  'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'accept-encoding':'gzip, deflate, br',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
  'Connection': 'keep-alive',
  # 'Content-Length':'0',
  'Cache-Control' : 'max-age=0',
  # 'Content-Type' : 'application/x-www-form-urlencoded',
  'Host' : 'ppt.mfa.gov.cn',
  # 'If-Modified-Since' : 'Mon, 21 Dec 2020 17:59:50 GMT',
  # 'origin':'https://ppt.mfa.gov.cn',
  # 'referer':'https://ppt.mfa.gov.cn/appom/',
  # 'sec-fetch-des':'empty',
  'sec-fetch-des':'document',
  # 'sec-fetch-mode':'cors',
  'sec-fetch-mode':'navigate',
  # 'sec-fetch-site':'same-site',
  'sec-fetch-site':'same-origin',
  'Sec-Fetch-User' : '?1',
  'Upgrade-Insecure-Requests':'1',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
  # 'x-client':'Browser/8.7.6 api/8.6',
}
DOWNLOAD_DELAY = 1
RANDOMIZE_DOWNLOAD_DELAY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   # 'PostReservation.middlewares.PostreservationSpiderMiddleware': 543,
   'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,

}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'PostReservation.middlewares.PostreservationDownloaderMiddleware': 543,
   # 'splash_jd.middlewares.SplashJdDownloaderMiddleware': 543,
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,

}



# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'PostReservation.pipelines.PostreservationPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
