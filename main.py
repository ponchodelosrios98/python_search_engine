from time import clock
from crawler import crawl_web
from indexing import look_up, space_ranks

index = {}
graph = {}

def search(environment, seedBase):
  start = clock()
  crawl_web(environment, index, graph, seedBase, 25, 1)
  result = look_up(index, 'PayPal,')
  endTime = clock() - start
  return endTime, result

request = search('Wikipedia', 'Elon_Musk')
print(space_ranks(graph))