from fetcher import get_page
from indexing import add_page_to_index

def get_next_url(page):
  start_link = page.find('<a href=')
  if start_link == -1: 
      return None, 0
  start_quote = page.find('"', start_link)
  end_quote = page.find('"', start_quote + 1)
  url = page[start_quote + 1:end_quote]
  return url, end_quote

def mergeLists(p,q):
  for e in q:
      if e not in p:
          p.append(e)

def get_all_links_from_content(page):
  links = []
  while True:
      url,endpos = get_next_url(page)
      if url:
          links.append(url)
          page = page[endpos:]
      else:
          break
  return links

def crawl_web(index, seed, max_pages, max_depth):
  tocrawl = [seed]
  next_depth = []
  crawled = []
  count = 0
  depth = 0
  while tocrawl and count < max_pages and depth < max_depth:
      count += 1
      page = tocrawl.pop()
      if page not in crawled:
          page_content = get_page(page)
          links = get_all_links_from_content(page_content)
          add_page_to_index(index, page, page_content)
          mergeLists(next_depth, links)
          crawled.append(page)
      if not tocrawl:
          tocrawl, next_depth = next_depth, []
          depth = depth + 1
  return index
