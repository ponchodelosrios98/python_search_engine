from crawler import crawl_web
from indexing import look_up

index = []

crawl_web(index, 'https://www.nowports.com', 4, 4)
print(look_up(index, 'servicio'))