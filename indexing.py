def add_keyword_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            if url not in entry[1]:
                entry[1].append(url)
            return
    index.append([keyword, [url]])

def add_page_to_index(index, url, content):
  query = content.split()
  for word in query:
    add_keyword_to_index(index, word, url)

def look_up(index, keyword):
    for word in index:
        if word[0] == keyword:
            return word[1]
    return []