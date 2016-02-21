# coding: utf-8

import urllib.request, lxml.html, re

def get_page_html(url) :
	try :
		with urllib.request.urlopen(url) as response :
			return bytes(response.read()).decode()
	except :
		return ''

def get_next_target(page) :
	start_link = page.find('href=')

	if start_link == -1 :
		return None, 0

	start_quote = page.find('"', start_link)
	end_quote	= page.find('"', start_quote + 1)
	url 		= page[start_quote + 1:end_quote] 

	return url, end_quote

def get_all_links(page) :
	links = []

	while True :
		url, endposition = get_next_target(page)

		if not url :
			break

		links.append(url)
		page = page[endposition:]
		html = get_page_html(url)
		print(url)

	return links

def union(p, q) :
	for e in q :
		if e not in p :
			p.append(e)
	return p

def crawl_web(seed):
	tocrawl = [seed]
	crawled = []

	while tocrawl:
		page = tocrawl.pop()

		if page not in crawled:
			union(tocrawl, get_all_links(get_page_html(page)))
			crawled.append(page)

	return crawled