from crawler import crawl_web
from indexing import look_up

index = []

def search(environment, seedBase):
  crawl_web(environment, index, seedBase, 10, 1)
  return look_up(index, 'Google')

print(search('Wikipedia', 'Esther_Wojcicki'))