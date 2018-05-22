def look_up(index, keyword):
    if keyword in index:
        return index[keyword]
    return []

def record_user_click(index, keyword, url):
    urls = look_up(index, keyword)
    if urls:
        for entry in urls:
            if entry[0] == url:
                entry[1] = entry[1]+1

def add_keyword_to_index(index, keyword, url):
    if keyword in index:
        if url not in index[keyword]:
            index[keyword].append(url)
            return
    index[keyword] = []

def space_ranks(graph):
    d = 0.8
    numloops = 10

    ranks = {}
    npages = len(graph)

    for page in graph:
        ranks[page] = 1.0 / npages
    
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    newrank = newrank + d * (ranks[node] / len(graph[node]))
            newranks[page] = newrank
        ranks = newranks
    return ranks

def add_page_to_index(index, url, content):
  query = content.split()
  for word in query:
    add_keyword_to_index(index, word, url)
