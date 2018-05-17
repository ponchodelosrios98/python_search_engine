from bs4 import BeautifulSoup
import urllib.request

def get_page(url):
    try:
        page = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(page.decode('utf-8'), 'html.parser')
        return str(soup.body.get_text())
    except:
        return ""
    return ""