# coding: utf-8

import sys,os
sys.path.append(os.pardir)

from crawler import crawl_web
crawl_web('https://ja.wikipedia.org')