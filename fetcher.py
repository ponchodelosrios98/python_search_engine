from bs4 import BeautifulSoup
import urllib.request

def get_page(environment, url, limit):
    links = []
    counter = 0
    try:
        page = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(page.decode('utf-8'), 'html.parser')
        body = soup.find("div", {"class":"mw-parser-output"})
        text = ''
        for paragraph in body.find_all('p'):
            text += paragraph.get_text()
            for link in paragraph.find_all('a'):
                if '#' not in link.get('href') and counter <= limit:
                    links.append('https://wikipedia.org' + link.get('href'))
                    counter += 1
        return links, text
    except:
        return links, ""
    return links, ""